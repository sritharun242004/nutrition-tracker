import os
import json
import numpy as np
from utils.nutrition_data import NUTRITION_DB, IMAGENET_FOOD_MAP, get_food_info

# Try to import TensorFlow
TF_AVAILABLE = False
try:
    import tensorflow as tf
    from tensorflow.keras.applications import MobileNetV2
    from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
    from tensorflow.keras.preprocessing import image as keras_image
    TF_AVAILABLE = True
    print("[INFO] TensorFlow loaded successfully.")
except ImportError:
    print("[WARN] TensorFlow not available. Using demo mode.")

_model = None


def load_model():
    global _model
    if TF_AVAILABLE and _model is None:
        print("[INFO] Loading MobileNetV2 model...")
        _model = MobileNetV2(weights='imagenet', include_top=True)
        print("[INFO] Model loaded.")
    return _model


def detect_food(image_path):
    """
    Detect food in image and return nutritional info.
    Returns: dict with food_name, confidence, nutrition, all_predictions
    """
    if not TF_AVAILABLE:
        return _demo_detection(image_path)

    try:
        model = load_model()
        if model is None:
            return _demo_detection(image_path)

        # Load and preprocess image
        img = keras_image.load_img(image_path, target_size=(224, 224))
        img_array = keras_image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Predict
        predictions = model.predict(img_array, verbose=0)
        decoded = decode_predictions(predictions, top=10)[0]

        # Filter for food items
        food_results = []
        for _, label, confidence in decoded:
            label_lower = label.lower().replace(',', '').strip()
            # Check direct mapping
            if label_lower in IMAGENET_FOOD_MAP:
                food_name = IMAGENET_FOOD_MAP[label_lower]
                food_results.append((food_name, float(confidence), label))
                continue
            # Check partial match in label
            for key in IMAGENET_FOOD_MAP:
                if key in label_lower:
                    food_name = IMAGENET_FOOD_MAP[key]
                    food_results.append((food_name, float(confidence), label))
                    break
            # Check if label matches any food in nutrition db
            for food_key in NUTRITION_DB:
                if food_key in label_lower or label_lower in food_key:
                    food_results.append((food_key, float(confidence), label))
                    break

        if food_results:
            best = food_results[0]
            food_name, confidence, raw_label = best
            nutrition = get_food_info(food_name)
            return {
                "success": True,
                "food_name": food_name.title(),
                "confidence": round(confidence * 100, 1),
                "raw_label": raw_label,
                "nutrition": nutrition,
                "all_predictions": [
                    {"label": lbl.replace('_', ' ').title(), "confidence": round(conf * 100, 1)}
                    for _, lbl, conf in decoded[:5]
                ]
            }
        else:
            # No food detected - return top prediction
            top_label = decoded[0][1].replace('_', ' ').title()
            return {
                "success": False,
                "food_name": "Unknown Food",
                "confidence": 0,
                "raw_label": top_label,
                "nutrition": None,
                "message": f"Could not identify food. Top prediction: {top_label}",
                "all_predictions": [
                    {"label": lbl.replace('_', ' ').title(), "confidence": round(conf * 100, 1)}
                    for _, lbl, conf in decoded[:5]
                ]
            }

    except Exception as e:
        print(f"[ERROR] Food detection failed: {e}")
        return _demo_detection(image_path)


def _demo_detection(image_path):
    """Demo mode - return sample result based on filename."""
    filename = os.path.basename(image_path).lower()

    # Try to match filename to food
    for food_key in NUTRITION_DB:
        if food_key.replace(' ', '_') in filename or food_key in filename:
            nutrition = NUTRITION_DB[food_key]
            return {
                "success": True,
                "food_name": food_key.title(),
                "confidence": 82.5,
                "raw_label": food_key,
                "nutrition": nutrition,
                "demo_mode": True,
                "all_predictions": [
                    {"label": food_key.title(), "confidence": 82.5},
                    {"label": "Similar Food", "confidence": 10.2},
                ]
            }

    # Default demo result
    demo_food = "pizza"
    return {
        "success": True,
        "food_name": "Pizza",
        "confidence": 75.0,
        "raw_label": "pizza",
        "nutrition": NUTRITION_DB[demo_food],
        "demo_mode": True,
        "message": "Demo mode: TensorFlow not installed. Showing sample result.",
        "all_predictions": [
            {"label": "Pizza", "confidence": 75.0},
            {"label": "Flatbread", "confidence": 15.0},
            {"label": "Cheese Food", "confidence": 10.0},
        ]
    }


def manual_food_lookup(food_name):
    """Look up food by name manually."""
    food_name = food_name.lower().strip()
    nutrition = get_food_info(food_name)
    if nutrition:
        return {
            "success": True,
            "food_name": food_name.title(),
            "confidence": 100.0,
            "nutrition": nutrition,
            "manual": True,
            "all_predictions": [{"label": food_name.title(), "confidence": 100.0}]
        }
    return {
        "success": False,
        "food_name": food_name,
        "message": f"Food '{food_name}' not found in database.",
        "suggestions": [k for k in NUTRITION_DB.keys() if food_name[:3] in k][:5]
    }

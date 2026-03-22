import os
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'saved')
DIABETES_MODEL_PATH = os.path.join(MODEL_DIR, 'diabetes_model.pkl')
OBESITY_MODEL_PATH = os.path.join(MODEL_DIR, 'obesity_model.pkl')
HYPERTENSION_MODEL_PATH = os.path.join(MODEL_DIR, 'hypertension_model.pkl')

_models = {}


def _generate_training_data():
    """Generate synthetic training data based on medical guidelines."""
    np.random.seed(42)
    n = 2000

    # Features: age, bmi, blood_sugar, activity_score, diet_quality, family_history, weight, height
    age = np.random.randint(18, 80, n)
    bmi = np.random.uniform(15, 45, n)
    blood_sugar = np.random.uniform(3.5, 12.0, n)  # mmol/L fasting
    activity_score = np.random.randint(1, 5, n)    # 1=sedentary, 4=very active
    diet_quality = np.random.randint(1, 5, n)       # 1=poor, 4=excellent
    family_history = np.random.randint(0, 2, n)    # 0=no, 1=yes
    systolic_bp = np.random.uniform(90, 200, n)
    cholesterol = np.random.uniform(3.0, 8.0, n)   # mmol/L

    X = np.column_stack([age, bmi, blood_sugar, activity_score, diet_quality,
                         family_history, systolic_bp, cholesterol])

    # --- Diabetes labels (based on medical criteria) ---
    diabetes_risk = np.zeros(n)
    for i in range(n):
        score = 0
        if blood_sugar[i] >= 7.0:
            score += 3   # Very high blood sugar
        elif blood_sugar[i] >= 5.6:
            score += 2   # Pre-diabetic range
        if bmi[i] >= 30:
            score += 2
        elif bmi[i] >= 25:
            score += 1
        if age[i] >= 45:
            score += 1
        if family_history[i]:
            score += 2
        if activity_score[i] <= 1:
            score += 1
        if diet_quality[i] <= 2:
            score += 1
        diabetes_risk[i] = min(score, 5)

    y_diabetes = np.where(diabetes_risk >= 4, 2,    # High
                 np.where(diabetes_risk >= 2, 1, 0))  # Moderate, Low

    # --- Obesity labels ---
    obesity_risk = np.zeros(n)
    for i in range(n):
        if bmi[i] >= 35:
            obesity_risk[i] = 2   # High
        elif bmi[i] >= 25:
            obesity_risk[i] = 1   # Moderate
        else:
            obesity_risk[i] = 0   # Low

    y_obesity = obesity_risk.astype(int)

    # --- Hypertension labels ---
    hypertension_risk = np.zeros(n)
    for i in range(n):
        score = 0
        if systolic_bp[i] >= 140:
            score += 3
        elif systolic_bp[i] >= 130:
            score += 2
        elif systolic_bp[i] >= 120:
            score += 1
        if bmi[i] >= 30:
            score += 1
        if age[i] >= 55:
            score += 1
        if activity_score[i] <= 1:
            score += 1
        if diet_quality[i] <= 2:
            score += 1
        if family_history[i]:
            score += 1
        hypertension_risk[i] = min(score, 5)

    y_hypertension = np.where(hypertension_risk >= 4, 2,
                     np.where(hypertension_risk >= 2, 1, 0))

    return X, y_diabetes, y_obesity, y_hypertension


def _train_and_save_models():
    """Train models on synthetic data and save to disk."""
    os.makedirs(MODEL_DIR, exist_ok=True)
    print("[INFO] Training disease prediction models...")

    X, y_diabetes, y_obesity, y_hypertension = _generate_training_data()

    for name, y, path in [
        ("Diabetes", y_diabetes, DIABETES_MODEL_PATH),
        ("Obesity", y_obesity, OBESITY_MODEL_PATH),
        ("Hypertension", y_hypertension, HYPERTENSION_MODEL_PATH),
    ]:
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('clf', RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced'))
        ])
        pipeline.fit(X, y)
        joblib.dump(pipeline, path)
        print(f"[INFO] {name} model saved.")


def _load_model(name, path):
    """Load or train a model."""
    if name not in _models:
        if not os.path.exists(path):
            _train_and_save_models()
        try:
            _models[name] = joblib.load(path)
        except Exception as e:
            print(f"[ERROR] Failed to load {name} model: {e}")
            _train_and_save_models()
            _models[name] = joblib.load(path)
    return _models[name]


def predict_disease_risk(user, blood_sugar=5.5, systolic_bp=120, cholesterol=4.5):
    """
    Predict disease risk for a user.
    Returns dict with risk levels and details for each disease.
    """
    # Map activity level to numeric score
    activity_map = {'sedentary': 1, 'light': 2, 'moderate': 3, 'active': 4, 'very_active': 4}
    activity_score = activity_map.get(user.activity_level, 3)

    # Diet quality based on health goal
    goal_quality = {
        'heart_health': 4, 'diabetes_management': 4, 'muscle_gain': 3,
        'maintenance': 3, 'weight_loss': 3
    }
    diet_quality = goal_quality.get(user.health_goal, 3)

    # Determine family history from medical conditions
    family_history = 1 if any(cond in str(user.medical_conditions).lower()
                               for cond in ['diabetes', 'hypertension', 'heart', 'family']) else 0

    features = np.array([[
        user.age, user.bmi, blood_sugar, activity_score,
        diet_quality, family_history, systolic_bp, cholesterol
    ]])

    risk_labels = {0: "Low", 1: "Moderate", 2: "High"}
    risk_colors = {0: "success", 1: "warning", 2: "danger"}
    risk_scores = {0: 20, 1: 55, 2: 85}

    results = {}

    # Diabetes prediction
    try:
        d_model = _load_model('diabetes', DIABETES_MODEL_PATH)
        d_pred = d_model.predict(features)[0]
        d_proba = d_model.predict_proba(features)[0]
        results['diabetes'] = {
            "risk_level": risk_labels[d_pred],
            "risk_color": risk_colors[d_pred],
            "risk_score": risk_scores[d_pred],
            "probability": round(float(max(d_proba)) * 100, 1),
            "factors": _get_diabetes_factors(user, blood_sugar),
            "advice": _get_diabetes_advice(d_pred, user)
        }
    except Exception as e:
        results['diabetes'] = _fallback_risk(user, 'diabetes')

    # Obesity prediction
    try:
        o_model = _load_model('obesity', OBESITY_MODEL_PATH)
        o_pred = o_model.predict(features)[0]
        o_proba = o_model.predict_proba(features)[0]
        results['obesity'] = {
            "risk_level": risk_labels[o_pred],
            "risk_color": risk_colors[o_pred],
            "risk_score": risk_scores[o_pred],
            "probability": round(float(max(o_proba)) * 100, 1),
            "factors": _get_obesity_factors(user),
            "advice": _get_obesity_advice(o_pred, user)
        }
    except Exception as e:
        results['obesity'] = _fallback_risk(user, 'obesity')

    # Hypertension prediction
    try:
        h_model = _load_model('hypertension', HYPERTENSION_MODEL_PATH)
        h_pred = h_model.predict(features)[0]
        h_proba = h_model.predict_proba(features)[0]
        results['hypertension'] = {
            "risk_level": risk_labels[h_pred],
            "risk_color": risk_colors[h_pred],
            "risk_score": risk_scores[h_pred],
            "probability": round(float(max(h_proba)) * 100, 1),
            "factors": _get_hypertension_factors(user, systolic_bp),
            "advice": _get_hypertension_advice(h_pred, user)
        }
    except Exception as e:
        results['hypertension'] = _fallback_risk(user, 'hypertension')

    return results


def _fallback_risk(user, disease):
    """Rule-based fallback prediction."""
    bmi = user.bmi
    if disease == 'diabetes':
        level = 2 if bmi >= 30 else (1 if bmi >= 25 else 0)
    elif disease == 'obesity':
        level = 2 if bmi >= 35 else (1 if bmi >= 25 else 0)
    else:
        level = 1 if bmi >= 25 else 0

    labels = {0: "Low", 1: "Moderate", 2: "High"}
    colors = {0: "success", 1: "warning", 2: "danger"}
    scores = {0: 20, 1: 55, 2: 85}

    return {
        "risk_level": labels[level],
        "risk_color": colors[level],
        "risk_score": scores[level],
        "probability": scores[level],
        "factors": ["BMI assessment", "Age factor", "Lifestyle evaluation"],
        "advice": ["Maintain a balanced diet", "Exercise regularly", "Regular health checkups"]
    }


def _get_diabetes_factors(user, blood_sugar):
    factors = []
    if user.bmi >= 25:
        factors.append(f"BMI of {user.bmi} (overweight/obese range)")
    if blood_sugar >= 5.6:
        factors.append(f"Elevated fasting blood sugar ({blood_sugar} mmol/L)")
    if user.age >= 45:
        factors.append(f"Age {user.age} — increased risk after 45")
    if user.activity_level == 'sedentary':
        factors.append("Sedentary lifestyle reduces insulin sensitivity")
    if not factors:
        factors.append("No major risk factors detected")
    return factors[:4]


def _get_diabetes_advice(risk, user):
    if risk == 2:
        return ["Consult an endocrinologist immediately", "Monitor blood sugar daily",
                "Adopt a low-carb, high-fiber diet", "Aim for 150 min/week of exercise"]
    elif risk == 1:
        return ["Schedule a blood glucose test", "Reduce sugar and refined carbs",
                "Increase physical activity", "Maintain healthy body weight"]
    else:
        return ["Maintain your healthy lifestyle", "Annual blood sugar screening recommended",
                "Continue balanced nutrition and exercise"]


def _get_obesity_factors(user):
    factors = []
    bmi = user.bmi
    if bmi >= 30:
        factors.append(f"BMI of {bmi} falls in the obese range")
    elif bmi >= 25:
        factors.append(f"BMI of {bmi} falls in the overweight range")
    if user.activity_level in ['sedentary', 'light']:
        factors.append("Low physical activity level")
    if user.health_goal not in ['weight_loss']:
        factors.append("Current goal may not address weight management")
    if user.age > 40:
        factors.append("Metabolic rate slows with age")
    if not factors:
        factors.append("BMI is within healthy range")
    return factors[:4]


def _get_obesity_advice(risk, user):
    if risk == 2:
        return ["Consult a dietitian for a medically supervised plan", "Set realistic weight loss goals (0.5-1kg/week)",
                "Track all food intake daily", "Build strength with resistance training"]
    elif risk == 1:
        return ["Reduce daily caloric intake by 300-500 calories", "Increase cardio exercise 3-4x per week",
                "Eat more fiber and protein to feel full", "Limit processed foods and added sugars"]
    else:
        return ["Maintain your current healthy weight", "Continue balanced diet and regular exercise",
                "Annual weight and BMI tracking recommended"]


def _get_hypertension_factors(user, systolic_bp):
    factors = []
    if systolic_bp >= 130:
        factors.append(f"Blood pressure {systolic_bp} mmHg (elevated)")
    if user.bmi >= 25:
        factors.append(f"Excess body weight increases blood pressure")
    if user.age >= 55:
        factors.append(f"Risk increases significantly after age 55")
    if user.activity_level == 'sedentary':
        factors.append("Physical inactivity contributes to high BP")
    if not factors:
        factors.append("No major risk factors detected")
    return factors[:4]


def _get_hypertension_advice(risk, user):
    if risk == 2:
        return ["Consult a cardiologist for BP management", "Restrict sodium intake below 1500mg/day",
                "Take BP medication if prescribed", "Avoid stress, alcohol, and smoking"]
    elif risk == 1:
        return ["Monitor blood pressure weekly", "Reduce salt and processed food intake",
                "Practice stress reduction techniques (yoga, meditation)", "Increase aerobic exercise"]
    else:
        return ["Maintain heart-healthy diet and lifestyle", "Regular BP monitoring (annually)",
                "Limit alcohol and avoid smoking"]

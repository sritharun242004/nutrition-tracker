# Nutritional database - values per 100g unless specified
# Columns: calories, protein(g), carbs(g), fat(g), fiber(g), sugar(g), sodium(mg)

NUTRITION_DB = {
    "pizza": {
        "calories": 266, "protein": 11.4, "carbs": 32.9, "fat": 9.8,
        "fiber": 2.3, "sugar": 3.6, "sodium": 586,
        "serving": "1 slice (107g)", "category": "Fast Food"
    },
    "burger": {
        "calories": 295, "protein": 17.1, "carbs": 24.1, "fat": 14.0,
        "fiber": 1.3, "sugar": 5.0, "sodium": 497,
        "serving": "1 burger (150g)", "category": "Fast Food"
    },
    "cheeseburger": {
        "calories": 303, "protein": 17.5, "carbs": 24.8, "fat": 14.8,
        "fiber": 1.3, "sugar": 5.2, "sodium": 534,
        "serving": "1 burger (160g)", "category": "Fast Food"
    },
    "hot dog": {
        "calories": 290, "protein": 10.9, "carbs": 22.9, "fat": 17.4,
        "fiber": 1.0, "sugar": 4.0, "sodium": 670,
        "serving": "1 hot dog (98g)", "category": "Fast Food"
    },
    "french fries": {
        "calories": 312, "protein": 3.4, "carbs": 41.4, "fat": 14.7,
        "fiber": 3.8, "sugar": 0.5, "sodium": 210,
        "serving": "Medium (117g)", "category": "Fast Food"
    },
    "fried chicken": {
        "calories": 260, "protein": 23.8, "carbs": 7.6, "fat": 15.3,
        "fiber": 0.4, "sugar": 0.0, "sodium": 415,
        "serving": "1 piece (140g)", "category": "Fast Food"
    },
    "spaghetti": {
        "calories": 158, "protein": 5.8, "carbs": 30.9, "fat": 0.9,
        "fiber": 1.8, "sugar": 0.6, "sodium": 1,
        "serving": "1 cup cooked (140g)", "category": "Pasta & Grains"
    },
    "pasta": {
        "calories": 158, "protein": 5.8, "carbs": 30.9, "fat": 0.9,
        "fiber": 1.8, "sugar": 0.6, "sodium": 1,
        "serving": "1 cup cooked (140g)", "category": "Pasta & Grains"
    },
    "rice": {
        "calories": 130, "protein": 2.7, "carbs": 28.2, "fat": 0.3,
        "fiber": 0.4, "sugar": 0.0, "sodium": 1,
        "serving": "1 cup cooked (186g)", "category": "Pasta & Grains"
    },
    "bread": {
        "calories": 265, "protein": 9.0, "carbs": 49.4, "fat": 3.2,
        "fiber": 2.7, "sugar": 5.3, "sodium": 491,
        "serving": "1 slice (28g)", "category": "Bakery"
    },
    "bagel": {
        "calories": 245, "protein": 9.8, "carbs": 47.9, "fat": 1.5,
        "fiber": 2.1, "sugar": 5.0, "sodium": 443,
        "serving": "1 bagel (98g)", "category": "Bakery"
    },
    "pretzel": {
        "calories": 380, "protein": 9.0, "carbs": 80.4, "fat": 3.0,
        "fiber": 2.9, "sugar": 3.0, "sodium": 1029,
        "serving": "1 pretzel (60g)", "category": "Snacks"
    },
    "banana": {
        "calories": 89, "protein": 1.1, "carbs": 22.8, "fat": 0.3,
        "fiber": 2.6, "sugar": 12.2, "sodium": 1,
        "serving": "1 medium (118g)", "category": "Fruits"
    },
    "apple": {
        "calories": 52, "protein": 0.3, "carbs": 13.8, "fat": 0.2,
        "fiber": 2.4, "sugar": 10.4, "sodium": 1,
        "serving": "1 medium (182g)", "category": "Fruits"
    },
    "orange": {
        "calories": 47, "protein": 0.9, "carbs": 11.8, "fat": 0.1,
        "fiber": 2.4, "sugar": 9.4, "sodium": 0,
        "serving": "1 medium (131g)", "category": "Fruits"
    },
    "mango": {
        "calories": 60, "protein": 0.8, "carbs": 15.0, "fat": 0.4,
        "fiber": 1.6, "sugar": 13.7, "sodium": 1,
        "serving": "1 cup sliced (165g)", "category": "Fruits"
    },
    "grapes": {
        "calories": 69, "protein": 0.7, "carbs": 18.1, "fat": 0.2,
        "fiber": 0.9, "sugar": 15.5, "sodium": 2,
        "serving": "1 cup (92g)", "category": "Fruits"
    },
    "strawberry": {
        "calories": 32, "protein": 0.7, "carbs": 7.7, "fat": 0.3,
        "fiber": 2.0, "sugar": 4.9, "sodium": 1,
        "serving": "1 cup (152g)", "category": "Fruits"
    },
    "pineapple": {
        "calories": 50, "protein": 0.5, "carbs": 13.1, "fat": 0.1,
        "fiber": 1.4, "sugar": 9.9, "sodium": 1,
        "serving": "1 cup chunks (165g)", "category": "Fruits"
    },
    "watermelon": {
        "calories": 30, "protein": 0.6, "carbs": 7.6, "fat": 0.2,
        "fiber": 0.4, "sugar": 6.2, "sodium": 1,
        "serving": "1 cup (154g)", "category": "Fruits"
    },
    "broccoli": {
        "calories": 34, "protein": 2.8, "carbs": 6.6, "fat": 0.4,
        "fiber": 2.6, "sugar": 1.7, "sodium": 33,
        "serving": "1 cup chopped (91g)", "category": "Vegetables"
    },
    "carrot": {
        "calories": 41, "protein": 0.9, "carbs": 9.6, "fat": 0.2,
        "fiber": 2.8, "sugar": 4.7, "sodium": 69,
        "serving": "1 medium (61g)", "category": "Vegetables"
    },
    "spinach": {
        "calories": 23, "protein": 2.9, "carbs": 3.6, "fat": 0.4,
        "fiber": 2.2, "sugar": 0.4, "sodium": 79,
        "serving": "1 cup raw (30g)", "category": "Vegetables"
    },
    "tomato": {
        "calories": 18, "protein": 0.9, "carbs": 3.9, "fat": 0.2,
        "fiber": 1.2, "sugar": 2.6, "sodium": 5,
        "serving": "1 medium (123g)", "category": "Vegetables"
    },
    "cucumber": {
        "calories": 15, "protein": 0.7, "carbs": 3.6, "fat": 0.1,
        "fiber": 0.5, "sugar": 1.7, "sodium": 2,
        "serving": "1 cup sliced (119g)", "category": "Vegetables"
    },
    "mushroom": {
        "calories": 22, "protein": 3.1, "carbs": 3.3, "fat": 0.3,
        "fiber": 1.0, "sugar": 2.0, "sodium": 5,
        "serving": "1 cup (96g)", "category": "Vegetables"
    },
    "bell pepper": {
        "calories": 31, "protein": 1.0, "carbs": 7.2, "fat": 0.3,
        "fiber": 2.5, "sugar": 3.7, "sodium": 4,
        "serving": "1 medium (119g)", "category": "Vegetables"
    },
    "corn": {
        "calories": 96, "protein": 3.4, "carbs": 21.0, "fat": 1.5,
        "fiber": 2.4, "sugar": 4.5, "sodium": 15,
        "serving": "1 ear (90g)", "category": "Vegetables"
    },
    "potato": {
        "calories": 77, "protein": 2.0, "carbs": 17.5, "fat": 0.1,
        "fiber": 2.1, "sugar": 0.8, "sodium": 6,
        "serving": "1 medium (150g)", "category": "Vegetables"
    },
    "mashed potato": {
        "calories": 113, "protein": 2.0, "carbs": 17.0, "fat": 4.2,
        "fiber": 1.5, "sugar": 1.5, "sodium": 333,
        "serving": "1 cup (210g)", "category": "Vegetables"
    },
    "chicken breast": {
        "calories": 165, "protein": 31.0, "carbs": 0.0, "fat": 3.6,
        "fiber": 0.0, "sugar": 0.0, "sodium": 74,
        "serving": "1 piece (172g)", "category": "Protein"
    },
    "salmon": {
        "calories": 208, "protein": 20.4, "carbs": 0.0, "fat": 13.4,
        "fiber": 0.0, "sugar": 0.0, "sodium": 59,
        "serving": "1 fillet (154g)", "category": "Seafood"
    },
    "tuna": {
        "calories": 144, "protein": 23.7, "carbs": 0.0, "fat": 4.9,
        "fiber": 0.0, "sugar": 0.0, "sodium": 43,
        "serving": "3 oz (85g)", "category": "Seafood"
    },
    "egg": {
        "calories": 155, "protein": 12.6, "carbs": 1.1, "fat": 10.6,
        "fiber": 0.0, "sugar": 1.1, "sodium": 124,
        "serving": "1 large egg (50g)", "category": "Protein"
    },
    "milk": {
        "calories": 61, "protein": 3.2, "carbs": 4.8, "fat": 3.3,
        "fiber": 0.0, "sugar": 5.1, "sodium": 44,
        "serving": "1 cup (244g)", "category": "Dairy"
    },
    "cheese": {
        "calories": 402, "protein": 24.9, "carbs": 1.3, "fat": 33.1,
        "fiber": 0.0, "sugar": 0.5, "sodium": 621,
        "serving": "1 oz (28g)", "category": "Dairy"
    },
    "yogurt": {
        "calories": 59, "protein": 10.2, "carbs": 3.6, "fat": 0.4,
        "fiber": 0.0, "sugar": 3.2, "sodium": 36,
        "serving": "1 cup (245g)", "category": "Dairy"
    },
    "ice cream": {
        "calories": 207, "protein": 3.5, "carbs": 23.6, "fat": 11.0,
        "fiber": 0.7, "sugar": 21.2, "sodium": 80,
        "serving": "1/2 cup (66g)", "category": "Desserts"
    },
    "chocolate": {
        "calories": 546, "protein": 5.0, "carbs": 60.0, "fat": 31.3,
        "fiber": 7.0, "sugar": 48.0, "sodium": 24,
        "serving": "1 oz (28g)", "category": "Desserts"
    },
    "cake": {
        "calories": 347, "protein": 4.3, "carbs": 53.4, "fat": 13.8,
        "fiber": 0.9, "sugar": 34.0, "sodium": 282,
        "serving": "1 slice (64g)", "category": "Desserts"
    },
    "oatmeal": {
        "calories": 68, "protein": 2.4, "carbs": 12.0, "fat": 1.4,
        "fiber": 1.7, "sugar": 0.0, "sodium": 48,
        "serving": "1 cup cooked (234g)", "category": "Breakfast"
    },
    "pancake": {
        "calories": 227, "protein": 6.4, "carbs": 38.2, "fat": 5.9,
        "fiber": 1.4, "sugar": 8.3, "sodium": 477,
        "serving": "2 medium pancakes (130g)", "category": "Breakfast"
    },
    "sandwich": {
        "calories": 250, "protein": 12.0, "carbs": 30.0, "fat": 9.0,
        "fiber": 2.0, "sugar": 4.0, "sodium": 520,
        "serving": "1 sandwich (180g)", "category": "Lunch"
    },
    "salad": {
        "calories": 20, "protein": 1.3, "carbs": 3.7, "fat": 0.3,
        "fiber": 1.5, "sugar": 2.0, "sodium": 10,
        "serving": "1 cup (85g)", "category": "Vegetables"
    },
    "soup": {
        "calories": 74, "protein": 3.8, "carbs": 8.5, "fat": 2.8,
        "fiber": 1.2, "sugar": 3.2, "sodium": 800,
        "serving": "1 cup (244g)", "category": "Soups"
    },
    "coffee": {
        "calories": 2, "protein": 0.3, "carbs": 0.0, "fat": 0.0,
        "fiber": 0.0, "sugar": 0.0, "sodium": 5,
        "serving": "1 cup (240ml)", "category": "Beverages"
    },
    "orange juice": {
        "calories": 45, "protein": 0.7, "carbs": 10.4, "fat": 0.2,
        "fiber": 0.2, "sugar": 8.4, "sodium": 1,
        "serving": "1 cup (248ml)", "category": "Beverages"
    },
    "burrito": {
        "calories": 206, "protein": 8.1, "carbs": 26.7, "fat": 8.0,
        "fiber": 2.7, "sugar": 1.0, "sodium": 411,
        "serving": "1 burrito (140g)", "category": "Mexican"
    },
    "sushi": {
        "calories": 143, "protein": 7.0, "carbs": 18.4, "fat": 3.6,
        "fiber": 0.5, "sugar": 4.1, "sodium": 217,
        "serving": "6 pieces (156g)", "category": "Asian"
    },
    "noodles": {
        "calories": 138, "protein": 4.5, "carbs": 25.2, "fat": 2.3,
        "fiber": 1.8, "sugar": 0.6, "sodium": 182,
        "serving": "1 cup cooked (160g)", "category": "Asian"
    },
    "dosa": {
        "calories": 168, "protein": 3.4, "carbs": 30.0, "fat": 4.0,
        "fiber": 1.5, "sugar": 0.5, "sodium": 310,
        "serving": "1 medium dosa (80g)", "category": "Indian"
    },
    "idli": {
        "calories": 58, "protein": 2.1, "carbs": 11.4, "fat": 0.4,
        "fiber": 0.5, "sugar": 0.3, "sodium": 130,
        "serving": "2 idlis (80g)", "category": "Indian"
    },
    "roti": {
        "calories": 297, "protein": 9.7, "carbs": 57.1, "fat": 3.3,
        "fiber": 8.5, "sugar": 0.4, "sodium": 395,
        "serving": "1 roti (40g)", "category": "Indian"
    },
    "biryani": {
        "calories": 176, "protein": 8.0, "carbs": 24.5, "fat": 5.7,
        "fiber": 1.5, "sugar": 2.0, "sodium": 450,
        "serving": "1 cup (200g)", "category": "Indian"
    },
    "dal": {
        "calories": 116, "protein": 7.0, "carbs": 17.4, "fat": 2.7,
        "fiber": 5.0, "sugar": 1.5, "sodium": 200,
        "serving": "1 cup (200g)", "category": "Indian"
    },
    # ── Indian Foods ──────────────────────────────────────
    "sambar": {
        "calories": 55, "protein": 3.5, "carbs": 8.0, "fat": 1.5,
        "fiber": 3.0, "sugar": 2.0, "sodium": 350,
        "serving": "1 cup (200g)", "category": "Indian"
    },
    "chutney": {
        "calories": 60, "protein": 1.5, "carbs": 10.0, "fat": 2.0,
        "fiber": 2.0, "sugar": 5.0, "sodium": 200,
        "serving": "2 tbsp (40g)", "category": "Indian"
    },
    "chapati": {
        "calories": 104, "protein": 3.1, "carbs": 18.0, "fat": 2.5,
        "fiber": 2.3, "sugar": 0.4, "sodium": 150,
        "serving": "1 chapati (40g)", "category": "Indian"
    },
    "paratha": {
        "calories": 260, "protein": 5.0, "carbs": 35.0, "fat": 11.0,
        "fiber": 3.0, "sugar": 1.0, "sodium": 380,
        "serving": "1 paratha (80g)", "category": "Indian"
    },
    "paneer": {
        "calories": 265, "protein": 18.3, "carbs": 1.2, "fat": 20.8,
        "fiber": 0.0, "sugar": 1.2, "sodium": 28,
        "serving": "100g", "category": "Indian"
    },
    "palak paneer": {
        "calories": 148, "protein": 8.5, "carbs": 8.0, "fat": 9.5,
        "fiber": 3.0, "sugar": 2.5, "sodium": 380,
        "serving": "1 cup (200g)", "category": "Indian"
    },
    "butter chicken": {
        "calories": 194, "protein": 16.5, "carbs": 7.0, "fat": 11.5,
        "fiber": 1.0, "sugar": 4.0, "sodium": 500,
        "serving": "1 cup (200g)", "category": "Indian"
    },
    "chicken curry": {
        "calories": 165, "protein": 16.0, "carbs": 5.0, "fat": 9.0,
        "fiber": 1.5, "sugar": 2.0, "sodium": 420,
        "serving": "1 cup (200g)", "category": "Indian"
    },
    "rajma": {
        "calories": 127, "protein": 8.7, "carbs": 22.8, "fat": 0.5,
        "fiber": 6.4, "sugar": 0.3, "sodium": 200,
        "serving": "1 cup cooked (177g)", "category": "Indian"
    },
    "chole": {
        "calories": 164, "protein": 8.9, "carbs": 27.4, "fat": 2.6,
        "fiber": 7.6, "sugar": 4.8, "sodium": 400,
        "serving": "1 cup (164g)", "category": "Indian"
    },
    "khichdi": {
        "calories": 130, "protein": 5.5, "carbs": 24.0, "fat": 2.0,
        "fiber": 2.5, "sugar": 1.0, "sodium": 320,
        "serving": "1 cup (200g)", "category": "Indian"
    },
    "upma": {
        "calories": 150, "protein": 3.5, "carbs": 25.0, "fat": 4.5,
        "fiber": 2.0, "sugar": 1.5, "sodium": 280,
        "serving": "1 cup (180g)", "category": "Indian"
    },
    "poha": {
        "calories": 180, "protein": 3.0, "carbs": 35.0, "fat": 3.5,
        "fiber": 1.8, "sugar": 2.0, "sodium": 250,
        "serving": "1 cup (180g)", "category": "Indian"
    },
    "pulao": {
        "calories": 160, "protein": 3.5, "carbs": 30.0, "fat": 3.0,
        "fiber": 1.5, "sugar": 1.5, "sodium": 350,
        "serving": "1 cup (200g)", "category": "Indian"
    },
    "halwa": {
        "calories": 260, "protein": 3.5, "carbs": 38.0, "fat": 11.0,
        "fiber": 1.5, "sugar": 25.0, "sodium": 80,
        "serving": "1 serving (100g)", "category": "Indian Desserts"
    },
    "gulab jamun": {
        "calories": 387, "protein": 7.5, "carbs": 52.0, "fat": 17.0,
        "fiber": 0.5, "sugar": 42.0, "sodium": 120,
        "serving": "2 pieces (80g)", "category": "Indian Desserts"
    },
    "rasgulla": {
        "calories": 186, "protein": 3.5, "carbs": 41.0, "fat": 0.8,
        "fiber": 0.0, "sugar": 38.0, "sodium": 50,
        "serving": "2 pieces (100g)", "category": "Indian Desserts"
    },
    "lassi": {
        "calories": 107, "protein": 5.5, "carbs": 16.0, "fat": 2.5,
        "fiber": 0.0, "sugar": 14.0, "sodium": 75,
        "serving": "1 glass (250ml)", "category": "Indian Beverages"
    },
    "chai": {
        "calories": 60, "protein": 2.5, "carbs": 7.5, "fat": 2.5,
        "fiber": 0.0, "sugar": 7.0, "sodium": 30,
        "serving": "1 cup (200ml)", "category": "Indian Beverages"
    },
    "pav bhaji": {
        "calories": 220, "protein": 5.0, "carbs": 35.0, "fat": 7.5,
        "fiber": 4.0, "sugar": 5.0, "sodium": 550,
        "serving": "1 serving (200g)", "category": "Indian Street Food"
    },
    "vada pav": {
        "calories": 290, "protein": 6.0, "carbs": 45.0, "fat": 10.0,
        "fiber": 3.5, "sugar": 3.0, "sodium": 480,
        "serving": "1 piece (120g)", "category": "Indian Street Food"
    },
    "bhel puri": {
        "calories": 180, "protein": 4.5, "carbs": 35.0, "fat": 3.5,
        "fiber": 3.0, "sugar": 4.0, "sodium": 380,
        "serving": "1 cup (100g)", "category": "Indian Street Food"
    },
    "masala dosa": {
        "calories": 206, "protein": 4.5, "carbs": 32.0, "fat": 7.0,
        "fiber": 2.0, "sugar": 2.0, "sodium": 380,
        "serving": "1 dosa (120g)", "category": "Indian"
    },
    "uthappam": {
        "calories": 130, "protein": 3.5, "carbs": 22.0, "fat": 3.5,
        "fiber": 1.5, "sugar": 1.5, "sodium": 280,
        "serving": "1 medium (90g)", "category": "Indian"
    },
    "medu vada": {
        "calories": 200, "protein": 6.0, "carbs": 22.0, "fat": 10.0,
        "fiber": 2.5, "sugar": 0.5, "sodium": 320,
        "serving": "2 vadas (90g)", "category": "Indian"
    },
    "lemon rice": {
        "calories": 155, "protein": 2.8, "carbs": 28.5, "fat": 4.0,
        "fiber": 1.2, "sugar": 0.8, "sodium": 290,
        "serving": "1 cup (180g)", "category": "Indian"
    },
    "aloo gobi": {
        "calories": 98, "protein": 3.0, "carbs": 15.0, "fat": 3.5,
        "fiber": 3.5, "sugar": 3.0, "sodium": 280,
        "serving": "1 cup (180g)", "category": "Indian"
    },
    "matar paneer": {
        "calories": 175, "protein": 9.5, "carbs": 12.0, "fat": 10.0,
        "fiber": 3.0, "sugar": 3.0, "sodium": 380,
        "serving": "1 cup (200g)", "category": "Indian"
    },
    "fish curry": {
        "calories": 155, "protein": 18.0, "carbs": 4.5, "fat": 7.5,
        "fiber": 1.0, "sugar": 2.0, "sodium": 450,
        "serving": "1 cup (200g)", "category": "Indian"
    },
    "mutton curry": {
        "calories": 218, "protein": 18.5, "carbs": 5.0, "fat": 13.5,
        "fiber": 1.0, "sugar": 1.5, "sodium": 480,
        "serving": "1 cup (200g)", "category": "Indian"
    },
    # ── End Indian Foods ──────────────────────────────────
    "almonds": {
        "calories": 579, "protein": 21.2, "carbs": 21.7, "fat": 49.9,
        "fiber": 12.5, "sugar": 4.4, "sodium": 1,
        "serving": "1 oz (28g)", "category": "Nuts & Seeds"
    },
    "peanut butter": {
        "calories": 588, "protein": 25.1, "carbs": 20.1, "fat": 50.4,
        "fiber": 6.0, "sugar": 9.2, "sodium": 459,
        "serving": "2 tbsp (32g)", "category": "Nuts & Seeds"
    },
}

# ImageNet food class mapping to our nutrition database
IMAGENET_FOOD_MAP = {
    "pizza": "pizza",
    "cheeseburger": "cheeseburger",
    "hotdog": "hot dog",
    "hot_dog": "hot dog",
    "french_fries": "french fries",
    "mashed_potato": "mashed potato",
    "head_cabbage": "salad",
    "broccoli": "broccoli",
    "cauliflower": "salad",
    "cucumber": "cucumber",
    "mushroom": "mushroom",
    "orange": "orange",
    "lemon": "orange",
    "pineapple": "pineapple",
    "banana": "banana",
    "strawberry": "strawberry",
    "ice_cream": "ice cream",
    "bagel": "bagel",
    "pretzel": "pretzel",
    "burrito": "burrito",
    "carbonara": "pasta",
    "espresso": "coffee",
    "eggnog": "milk",
    "guacamole": "salad",
    "potpie": "soup",
    "meat_loaf": "chicken breast",
    "chocolate_sauce": "chocolate",
}

# Healthy food recommendations by goal
GOAL_FOODS = {
    "weight_loss": {
        "recommended": ["salad", "broccoli", "spinach", "chicken breast", "salmon", "yogurt", "apple", "oatmeal"],
        "avoid": ["pizza", "burger", "french fries", "ice cream", "cake", "chocolate"],
        "description": "Focus on low-calorie, high-protein foods with plenty of vegetables"
    },
    "muscle_gain": {
        "recommended": ["chicken breast", "salmon", "egg", "milk", "yogurt", "oatmeal", "almonds", "tuna"],
        "avoid": ["chips", "soda", "candy", "ice cream"],
        "description": "Prioritize high-protein foods with complex carbohydrates"
    },
    "maintenance": {
        "recommended": ["rice", "pasta", "chicken breast", "egg", "banana", "apple", "salad", "oatmeal"],
        "avoid": ["excessive fast food", "sugary drinks"],
        "description": "Balanced diet with varied food groups"
    },
    "diabetes_management": {
        "recommended": ["salad", "broccoli", "spinach", "chicken breast", "salmon", "oatmeal", "almonds"],
        "avoid": ["pizza", "burger", "french fries", "ice cream", "cake", "chocolate", "rice"],
        "description": "Low glycemic index foods, high in fiber and protein"
    },
    "heart_health": {
        "recommended": ["salmon", "oatmeal", "almonds", "spinach", "broccoli", "apple", "orange"],
        "avoid": ["fried chicken", "pizza", "cheese", "burger"],
        "description": "Focus on omega-3 rich foods, fruits, and vegetables"
    }
}

# Meal plan templates
MEAL_PLANS = {
    "weight_loss": {
        "breakfast": ["Oatmeal with berries (300 cal)", "Greek yogurt with fruits (250 cal)", "Scrambled eggs with spinach (280 cal)"],
        "lunch": ["Grilled chicken salad (350 cal)", "Vegetable soup with bread (300 cal)", "Tuna sandwich (320 cal)"],
        "dinner": ["Baked salmon with broccoli (400 cal)", "Chicken stir-fry with vegetables (380 cal)", "Lentil soup with roti (350 cal)"],
        "snacks": ["Apple (80 cal)", "Almonds - 1 oz (160 cal)", "Carrot sticks with hummus (100 cal)"]
    },
    "muscle_gain": {
        "breakfast": ["Oatmeal with protein powder (450 cal)", "Eggs with whole grain toast (400 cal)", "Greek yogurt with granola (420 cal)"],
        "lunch": ["Grilled chicken with rice (550 cal)", "Tuna pasta salad (500 cal)", "Turkey sandwich with avocado (480 cal)"],
        "dinner": ["Salmon with sweet potato (600 cal)", "Beef stir-fry with brown rice (580 cal)", "Chicken curry with roti (550 cal)"],
        "snacks": ["Peanut butter on toast (300 cal)", "Protein shake with banana (350 cal)", "Almonds and cheese (280 cal)"]
    },
    "maintenance": {
        "breakfast": ["Oatmeal with fruits (350 cal)", "Eggs and toast (320 cal)", "Idli with sambar (300 cal)"],
        "lunch": ["Rice with dal and vegetables (450 cal)", "Chicken wrap (400 cal)", "Pasta with tomato sauce (420 cal)"],
        "dinner": ["Grilled chicken with salad (400 cal)", "Fish curry with rice (450 cal)", "Vegetable biryani (400 cal)"],
        "snacks": ["Fruits (100 cal)", "Yogurt (150 cal)", "Nuts (160 cal)"]
    }
}


def get_food_info(food_name):
    """Get nutritional info for a food item."""
    food_name = food_name.lower().strip()
    # Direct match
    if food_name in NUTRITION_DB:
        return NUTRITION_DB[food_name]
    # Partial match
    for key in NUTRITION_DB:
        if food_name in key or key in food_name:
            return NUTRITION_DB[key]
    return None


def get_all_foods():
    """Get list of all foods in database."""
    return list(NUTRITION_DB.keys())


def get_foods_by_category(category):
    """Get foods filtered by category."""
    return {k: v for k, v in NUTRITION_DB.items() if v.get("category") == category}

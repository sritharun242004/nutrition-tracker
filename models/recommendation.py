from utils.nutrition_data import NUTRITION_DB, GOAL_FOODS, MEAL_PLANS
import random


def get_recommendations(user):
    """Generate personalized diet recommendations based on user profile."""
    bmi = user.bmi
    goal = user.health_goal
    daily_calories = user.daily_calorie_need()

    # Macronutrient distribution based on goal
    macros = _calculate_macros(daily_calories, goal)

    # Get meal plan
    plan_key = goal if goal in MEAL_PLANS else 'maintenance'
    meal_plan = MEAL_PLANS[plan_key]

    # Get food recommendations
    goal_key = goal if goal in GOAL_FOODS else 'maintenance'
    food_recs = GOAL_FOODS[goal_key]

    # Generate specific food suggestions with nutritional details
    recommended_foods = []
    for food_name in food_recs['recommended'][:8]:
        if food_name in NUTRITION_DB:
            info = NUTRITION_DB[food_name].copy()
            info['name'] = food_name.title()
            recommended_foods.append(info)

    # Foods to avoid
    avoid_foods = []
    for food_name in food_recs.get('avoid', [])[:6]:
        if food_name in NUTRITION_DB:
            info = NUTRITION_DB[food_name].copy()
            info['name'] = food_name.title()
            avoid_foods.append(info)

    # Health tips based on BMI and goal
    tips = _generate_tips(bmi, goal, user.age, user.activity_level)

    # Water intake recommendation
    water_intake = round(user.weight * 0.033, 1)  # 33ml per kg

    return {
        "daily_calories": daily_calories,
        "macros": macros,
        "meal_plan": meal_plan,
        "recommended_foods": recommended_foods,
        "avoid_foods": avoid_foods,
        "tips": tips,
        "water_intake": water_intake,
        "description": food_recs.get('description', ''),
        "bmi": bmi,
        "bmi_category": user.bmi_category,
        "goal": goal.replace('_', ' ').title()
    }


def _calculate_macros(calories, goal):
    """Calculate macronutrient targets in grams."""
    if goal == 'weight_loss':
        protein_pct, carb_pct, fat_pct = 0.35, 0.40, 0.25
    elif goal == 'muscle_gain':
        protein_pct, carb_pct, fat_pct = 0.30, 0.45, 0.25
    elif goal == 'diabetes_management':
        protein_pct, carb_pct, fat_pct = 0.30, 0.35, 0.35
    elif goal == 'heart_health':
        protein_pct, carb_pct, fat_pct = 0.25, 0.50, 0.25
    else:  # maintenance
        protein_pct, carb_pct, fat_pct = 0.25, 0.50, 0.25

    return {
        "protein": round((calories * protein_pct) / 4),   # 4 cal/g
        "carbs": round((calories * carb_pct) / 4),         # 4 cal/g
        "fat": round((calories * fat_pct) / 9),             # 9 cal/g
        "protein_pct": round(protein_pct * 100),
        "carbs_pct": round(carb_pct * 100),
        "fat_pct": round(fat_pct * 100),
        "fiber": 25 if goal != 'muscle_gain' else 30
    }


def _generate_tips(bmi, goal, age, activity_level):
    """Generate personalized health tips."""
    tips = []

    # BMI-based tips
    if bmi < 18.5:
        tips.append("Your BMI indicates you are underweight. Focus on nutrient-dense, calorie-rich foods.")
        tips.append("Eat 5-6 smaller meals throughout the day to increase caloric intake.")
    elif 18.5 <= bmi < 25:
        tips.append("Your BMI is in the healthy range. Maintain this with balanced nutrition and regular exercise.")
        tips.append("Focus on food quality rather than restriction.")
    elif 25 <= bmi < 30:
        tips.append("Your BMI indicates you are slightly overweight. Consider reducing calorie intake by 300-500 calories daily.")
        tips.append("Increase physical activity — aim for 150 minutes of moderate exercise per week.")
    else:
        tips.append("Your BMI indicates obesity. Consult a healthcare provider for personalized guidance.")
        tips.append("Start with small, sustainable changes — reduce portion sizes and add light exercise.")

    # Goal-specific tips
    if goal == 'weight_loss':
        tips.append("Eat protein at every meal to stay full and preserve muscle mass.")
        tips.append("Fill half your plate with non-starchy vegetables at each meal.")
        tips.append("Avoid liquid calories — drink water, herbal teas instead of sugary drinks.")
    elif goal == 'muscle_gain':
        tips.append("Consume 1.6-2.2g of protein per kg of body weight daily.")
        tips.append("Eat a protein-rich snack within 30 minutes post-workout.")
        tips.append("Don't skip carbohydrates — they fuel your workouts and recovery.")
    elif goal == 'diabetes_management':
        tips.append("Choose low glycemic index (GI) foods to manage blood sugar levels.")
        tips.append("Eat at regular intervals to prevent blood sugar spikes and crashes.")
        tips.append("Limit refined carbohydrates and added sugars.")
    elif goal == 'heart_health':
        tips.append("Include omega-3 rich foods like salmon, walnuts, and flaxseeds regularly.")
        tips.append("Reduce sodium intake — aim for less than 2300mg per day.")
        tips.append("Increase soluble fiber intake from oats, beans, and fruits.")

    # Age-based tips
    if age > 50:
        tips.append("After 50, focus on calcium and vitamin D for bone health.")
        tips.append("Include more anti-inflammatory foods like berries, leafy greens, and olive oil.")

    # Activity-based tips
    if activity_level == 'sedentary':
        tips.append("Try to incorporate at least 30 minutes of walking daily.")
        tips.append("Take short movement breaks every hour if you have a desk job.")

    return tips[:6]  # Return max 6 tips


def analyze_food_log(food_logs, daily_calories):
    """Analyze food intake history and provide insights."""
    if not food_logs:
        return {"message": "No food logs found. Start logging your meals!"}

    total_calories = sum(log.calories for log in food_logs)
    total_protein = sum(log.protein for log in food_logs)
    total_carbs = sum(log.carbs for log in food_logs)
    total_fat = sum(log.fat for log in food_logs)
    total_fiber = sum(log.fiber for log in food_logs)

    calorie_diff = total_calories - daily_calories
    status = "on track"
    if calorie_diff > 200:
        status = "over target"
    elif calorie_diff < -200:
        status = "under target"

    return {
        "total_calories": round(total_calories),
        "total_protein": round(total_protein, 1),
        "total_carbs": round(total_carbs, 1),
        "total_fat": round(total_fat, 1),
        "total_fiber": round(total_fiber, 1),
        "calorie_target": daily_calories,
        "calorie_diff": round(calorie_diff),
        "status": status,
        "remaining_calories": max(0, round(daily_calories - total_calories))
    }

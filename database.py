from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    # Profile fields
    age = db.Column(db.Integer, default=25)
    weight = db.Column(db.Float, default=70.0)   # kg
    height = db.Column(db.Float, default=170.0)  # cm
    gender = db.Column(db.String(10), default='male')
    activity_level = db.Column(db.String(20), default='moderate')
    health_goal = db.Column(db.String(30), default='maintenance')
    medical_conditions = db.Column(db.String(200), default='none')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Relationships
    food_logs = db.relationship('FoodLog', backref='user', lazy=True)
    health_metrics = db.relationship('HealthMetric', backref='user', lazy=True)

    @property
    def bmi(self):
        if self.height and self.weight and self.height > 0:
            h_m = self.height / 100
            return round(self.weight / (h_m * h_m), 1)
        return 0.0

    @property
    def bmi_category(self):
        bmi = self.bmi
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal Weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def daily_calorie_need(self):
        """Harris-Benedict equation."""
        if self.gender == 'male':
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        else:
            bmr = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)

        activity_multipliers = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very_active': 1.9
        }
        multiplier = activity_multipliers.get(self.activity_level, 1.55)
        tdee = bmr * multiplier

        # Adjust based on goal
        if self.health_goal == 'weight_loss':
            tdee -= 500  # 500 cal deficit
        elif self.health_goal == 'muscle_gain':
            tdee += 300  # 300 cal surplus

        return round(tdee)


class FoodLog(db.Model):
    __tablename__ = 'food_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    food_name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Float, default=0)
    protein = db.Column(db.Float, default=0)
    carbs = db.Column(db.Float, default=0)
    fat = db.Column(db.Float, default=0)
    fiber = db.Column(db.Float, default=0)
    sugar = db.Column(db.Float, default=0)
    sodium = db.Column(db.Float, default=0)
    quantity = db.Column(db.Float, default=100)  # grams
    meal_type = db.Column(db.String(20), default='meal')  # breakfast/lunch/dinner/snack
    image_path = db.Column(db.String(200), default='')
    date_logged = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.String(200), default='')


class HealthMetric(db.Model):
    __tablename__ = 'health_metrics'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    systolic_bp = db.Column(db.Integer, default=120)
    diastolic_bp = db.Column(db.Integer, default=80)
    blood_sugar = db.Column(db.Float, default=5.5)  # mmol/L fasting
    date_recorded = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.String(200), default='')


class ContactMessage(db.Model):
    __tablename__ = 'contact_messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)

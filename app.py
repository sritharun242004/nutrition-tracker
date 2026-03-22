import os
import json
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from database import db, User, FoodLog, HealthMetric, ContactMessage
from models.food_detection import detect_food, manual_food_lookup
from models.recommendation import get_recommendations, analyze_food_log
from models.disease_prediction import predict_disease_risk
from utils.nutrition_data import NUTRITION_DB, get_all_foods

# ── App setup ──────────────────────────────────────────────────────────────
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = 'foodhealth2024secretkey!@#'
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://neondb_owner:npg_NtUXZqM0JIh7'
    '@ep-falling-leaf-amtuw6e8-pooler.c-5.us-east-1.aws.neon.tech'
    '/neondb?sslmode=require'
)
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'connect_args': {'sslmode': 'require'}
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login to access this page.'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ── Routes: Public ─────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        if name and email and subject and message:
            msg = ContactMessage(name=name, email=email, subject=subject, message=message)
            db.session.add(msg)
            db.session.commit()
            flash('Thank you! Your message has been sent.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all fields.', 'danger')
    return render_template('contact.html')


# ── Routes: Auth ───────────────────────────────────────────────────────────

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm_password', '')

        if not all([username, email, password, confirm]):
            flash('Please fill all fields.', 'danger')
            return render_template('register.html')
        if password != confirm:
            flash('Passwords do not match.', 'danger')
            return render_template('register.html')
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return render_template('register.html')
        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'danger')
            return render_template('register.html')

        user = User(
            username=username,
            email=email,
            password=generate_password_hash(password),
            age=int(request.form.get('age', 25)),
            weight=float(request.form.get('weight', 70)),
            height=float(request.form.get('height', 170)),
            gender=request.form.get('gender', 'male'),
            activity_level=request.form.get('activity_level', 'moderate'),
            health_goal=request.form.get('health_goal', 'maintenance'),
            medical_conditions=request.form.get('medical_conditions', 'none')
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f'Welcome, {username}! Your account has been created.', 'success')
        return redirect(url_for('dashboard'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        remember = bool(request.form.get('remember'))
        user = User.query.filter_by(email=email).first()
        pw_ok = user and check_password_hash(user.password, password)

        if pw_ok:
            login_user(user, remember=remember)
            next_page = request.args.get('next')
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(next_page or url_for('dashboard'))
        flash('Invalid email or password.', 'danger')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


# ── Routes: Dashboard ──────────────────────────────────────────────────────

@app.route('/dashboard')
@login_required
def dashboard():
    # Today's food logs
    today = datetime.utcnow().date()
    today_logs = FoodLog.query.filter(
        FoodLog.user_id == current_user.id,
        FoodLog.date_logged >= datetime.combine(today, datetime.min.time())
    ).all()

    daily_calories = current_user.daily_calorie_need()
    today_analysis = analyze_food_log(today_logs, daily_calories)

    # Last 7 days calorie data for chart
    cal_data = []
    labels = []
    for i in range(6, -1, -1):
        day = datetime.utcnow().date() - timedelta(days=i)
        logs = FoodLog.query.filter(
            FoodLog.user_id == current_user.id,
            FoodLog.date_logged >= datetime.combine(day, datetime.min.time()),
            FoodLog.date_logged < datetime.combine(day + timedelta(days=1), datetime.min.time())
        ).all()
        cal_data.append(round(sum(l.calories for l in logs)))
        labels.append(day.strftime('%a'))

    # Recent food logs (last 5)
    recent_logs = FoodLog.query.filter_by(user_id=current_user.id)\
        .order_by(FoodLog.date_logged.desc()).limit(5).all()

    return render_template('dashboard.html',
        today_logs=today_logs,
        today_analysis=today_analysis,
        daily_calories=daily_calories,
        cal_data=json.dumps(cal_data),
        cal_labels=json.dumps(labels),
        recent_logs=recent_logs
    )


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.age = int(request.form.get('age', current_user.age))
        current_user.weight = float(request.form.get('weight', current_user.weight))
        current_user.height = float(request.form.get('height', current_user.height))
        current_user.gender = request.form.get('gender', current_user.gender)
        current_user.activity_level = request.form.get('activity_level', current_user.activity_level)
        current_user.health_goal = request.form.get('health_goal', current_user.health_goal)
        current_user.medical_conditions = request.form.get('medical_conditions', current_user.medical_conditions)
        db.session.commit()

        # Log health metric
        metric = HealthMetric(
            user_id=current_user.id,
            weight=current_user.weight,
            bmi=current_user.bmi
        )
        db.session.add(metric)
        db.session.commit()

        flash('Profile updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('profile.html')


# ── Routes: Food Detection ─────────────────────────────────────────────────

@app.route('/detect', methods=['GET', 'POST'])
@login_required
def detect():
    result = None
    if request.method == 'POST':
        # Manual food search
        if 'manual_food' in request.form:
            food_name = request.form.get('manual_food', '').strip()
            if food_name:
                result = manual_food_lookup(food_name)

        # Image upload
        elif 'food_image' in request.files:
            file = request.files['food_image']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                result = detect_food(filepath)
                result['image_path'] = f'/uploads/{filename}'
            else:
                flash('Please upload a valid image file (PNG, JPG, JPEG).', 'warning')

    all_foods = get_all_foods()
    return render_template('food_detection.html', result=result, all_foods=all_foods)


@app.route('/log_food', methods=['POST'])
@login_required
def log_food():
    """Log detected or manually entered food."""
    food_name = request.form.get('food_name', '').strip()
    quantity = float(request.form.get('quantity', 100))
    meal_type = request.form.get('meal_type', 'meal')
    image_path = request.form.get('image_path', '')

    from utils.nutrition_data import get_food_info
    nutrition = get_food_info(food_name)
    if not nutrition:
        flash('Food not found in database.', 'danger')
        return redirect(url_for('detect'))

    factor = quantity / 100.0
    log = FoodLog(
        user_id=current_user.id,
        food_name=food_name,
        calories=round(nutrition['calories'] * factor, 1),
        protein=round(nutrition['protein'] * factor, 1),
        carbs=round(nutrition['carbs'] * factor, 1),
        fat=round(nutrition['fat'] * factor, 1),
        fiber=round(nutrition['fiber'] * factor, 1),
        sugar=round(nutrition['sugar'] * factor, 1),
        sodium=round(nutrition['sodium'] * factor, 1),
        quantity=quantity,
        meal_type=meal_type,
        image_path=image_path
    )
    db.session.add(log)
    db.session.commit()
    flash(f'{food_name.title()} ({quantity}g) logged successfully!', 'success')
    return redirect(url_for('detect'))


# ── Routes: Recommendations ────────────────────────────────────────────────

@app.route('/recommend')
@login_required
def recommend():
    recs = get_recommendations(current_user)
    return render_template('recommendations.html', recs=recs)


# ── Routes: Disease Risk ───────────────────────────────────────────────────

@app.route('/disease-risk', methods=['GET', 'POST'])
@login_required
def disease_risk():
    risk_results = None
    blood_sugar = 5.5
    systolic_bp = 120
    cholesterol = 4.5

    if request.method == 'POST':
        blood_sugar = float(request.form.get('blood_sugar', 5.5))
        systolic_bp = float(request.form.get('systolic_bp', 120))
        cholesterol = float(request.form.get('cholesterol', 4.5))

        risk_results = predict_disease_risk(
            current_user,
            blood_sugar=blood_sugar,
            systolic_bp=systolic_bp,
            cholesterol=cholesterol
        )

    return render_template('disease_risk.html',
        risk_results=risk_results,
        blood_sugar=blood_sugar,
        systolic_bp=systolic_bp,
        cholesterol=cholesterol
    )


# ── Routes: History ────────────────────────────────────────────────────────

@app.route('/history')
@login_required
def history():
    # Get filter params
    days = int(request.args.get('days', 7))
    meal_filter = request.args.get('meal', 'all')

    start_date = datetime.utcnow() - timedelta(days=days)
    query = FoodLog.query.filter(
        FoodLog.user_id == current_user.id,
        FoodLog.date_logged >= start_date
    )
    if meal_filter != 'all':
        query = query.filter_by(meal_type=meal_filter)

    logs = query.order_by(FoodLog.date_logged.desc()).all()

    # Group by date
    grouped = {}
    for log in logs:
        date_key = log.date_logged.strftime('%Y-%m-%d')
        if date_key not in grouped:
            grouped[date_key] = {'date': log.date_logged.strftime('%B %d, %Y'), 'logs': [], 'totals': {
                'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0
            }}
        grouped[date_key]['logs'].append(log)
        grouped[date_key]['totals']['calories'] += log.calories
        grouped[date_key]['totals']['protein'] += log.protein
        grouped[date_key]['totals']['carbs'] += log.carbs
        grouped[date_key]['totals']['fat'] += log.fat

    # Round totals
    for date_key in grouped:
        for k in grouped[date_key]['totals']:
            grouped[date_key]['totals'][k] = round(grouped[date_key]['totals'][k], 1)

    daily_calories = current_user.daily_calorie_need()
    total_logs = sum(len(v['logs']) for v in grouped.values())

    return render_template('history.html',
        grouped=grouped,
        days=days,
        meal_filter=meal_filter,
        daily_calories=daily_calories,
        total_logs=total_logs
    )


@app.route('/delete_log/<int:log_id>', methods=['POST'])
@login_required
def delete_log(log_id):
    log = FoodLog.query.filter_by(id=log_id, user_id=current_user.id).first_or_404()
    db.session.delete(log)
    db.session.commit()
    flash('Food entry deleted.', 'success')
    return redirect(url_for('history'))


# ── Routes: Report ─────────────────────────────────────────────────────────

@app.route('/report')
@login_required
def report():
    # Last 30 days
    start_date = datetime.utcnow() - timedelta(days=30)
    logs = FoodLog.query.filter(
        FoodLog.user_id == current_user.id,
        FoodLog.date_logged >= start_date
    ).order_by(FoodLog.date_logged.asc()).all()

    daily_calories = current_user.daily_calorie_need()
    analysis = analyze_food_log(logs, daily_calories * 30)

    # Daily breakdown for chart
    daily_data = {}
    for log in logs:
        date_key = log.date_logged.strftime('%Y-%m-%d')
        if date_key not in daily_data:
            daily_data[date_key] = 0
        daily_data[date_key] += log.calories

    # Top foods consumed
    food_counts = {}
    for log in logs:
        name = log.food_name.lower()
        food_counts[name] = food_counts.get(name, 0) + 1
    top_foods = sorted(food_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    # Disease risk
    risk_results = predict_disease_risk(current_user)

    recs = get_recommendations(current_user)

    return render_template('report.html',
        logs=logs,
        analysis=analysis,
        daily_calories=daily_calories,
        daily_data=json.dumps(list(daily_data.values())),
        daily_labels=json.dumps(list(daily_data.keys())),
        top_foods=top_foods,
        risk_results=risk_results,
        recs=recs,
        report_date=datetime.utcnow().strftime('%B %d, %Y'),
        start_date=start_date.strftime('%B %d'),
        end_date=datetime.utcnow().strftime('%B %d, %Y')
    )


# ── API endpoints ──────────────────────────────────────────────────────────

@app.route('/api/foods/search')
@login_required
def api_food_search():
    q = request.args.get('q', '').lower().strip()
    if len(q) < 2:
        return jsonify([])
    results = [k for k in NUTRITION_DB.keys() if q in k][:10]
    return jsonify(results)


@app.route('/api/food/info/<food_name>')
@login_required
def api_food_info(food_name):
    from utils.nutrition_data import get_food_info
    info = get_food_info(food_name)
    if info:
        return jsonify({"success": True, "food_name": food_name, "nutrition": info})
    return jsonify({"success": False, "message": "Food not found"}), 404


# ── Static file helper ─────────────────────────────────────────────────────

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    from flask import send_from_directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# ── Init DB ────────────────────────────────────────────────────────────────

def create_tables():
    with app.app_context():
        db.create_all()
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        print("[INFO] Database tables created.")
        _seed_demo_user()


def _seed_demo_user():
    """Create a demo user if not already present."""
    from datetime import datetime, timedelta
    import random
    if User.query.filter_by(email='demo@foodhealth.com').first():
        return  # already seeded

    demo = User(
        username='demo',
        email='demo@foodhealth.com',
        password=generate_password_hash('demo123', method='pbkdf2:sha256'),
        age=25, weight=72.0, height=175.0,
        gender='male', activity_level='moderate',
        health_goal='weight_loss', medical_conditions='none'
    )
    db.session.add(demo)
    db.session.flush()  # get demo.id before commit

    # Seed 7 days of sample food logs
    sample_meals = [
        ('oatmeal', 200, 'breakfast'), ('banana', 120, 'breakfast'),
        ('rice', 180, 'lunch'), ('chicken breast', 150, 'lunch'), ('salad', 100, 'lunch'),
        ('salmon', 150, 'dinner'), ('broccoli', 120, 'dinner'),
        ('almonds', 30, 'snack'), ('apple', 150, 'snack'),
        ('dosa', 100, 'breakfast'), ('idli', 120, 'breakfast'),
        ('dal', 200, 'lunch'), ('roti', 80, 'dinner'),
        ('biryani', 200, 'lunch'), ('chai', 200, 'snack'),
    ]
    from utils.nutrition_data import get_food_info
    for i in range(7):
        day = datetime.utcnow() - timedelta(days=i)
        # 3-4 entries per day
        for food_name, qty, meal in random.sample(sample_meals, 4):
            info = get_food_info(food_name)
            if not info:
                continue
            f = qty / 100.0
            log = FoodLog(
                user_id=demo.id,
                food_name=food_name,
                calories=round(info['calories'] * f, 1),
                protein=round(info['protein'] * f, 1),
                carbs=round(info['carbs'] * f, 1),
                fat=round(info['fat'] * f, 1),
                fiber=round(info['fiber'] * f, 1),
                sugar=round(info['sugar'] * f, 1),
                sodium=round(info['sodium'] * f, 1),
                quantity=qty, meal_type=meal,
                date_logged=day
            )
            db.session.add(log)

    db.session.commit()
    print("[INFO] Demo user created → email: demo@foodhealth.com | password: demo123")


if __name__ == '__main__':
    create_tables()
    app.run(debug=True, host='0.0.0.0', port=5001)

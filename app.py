from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from functools import wraps
import jinja2
from markupsafe import Markup
from models import db, User, StateInfo, NECArticle, TheoryTopic, CalculationTutorial, PracticeQuestion, QuizResult

# Admin required decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.username != 'admin':
            flash('You must be an admin to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config')
    
    # Initialize database with app
    db.init_app(app)
    
    # Add custom Jinja2 filters
    @app.template_filter('nl2br')
    def nl2br_filter(s):
        if s:
            s = s.replace('\n', '<br>')
            return Markup(s)
        return s
    
    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Define routes
    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            
            # Basic validation
            if not all([username, email, password, confirm_password]):
                flash('All fields are required', 'error')
                return render_template('register.html')
            
            if password != confirm_password:
                flash('Passwords do not match', 'error')
                return render_template('register.html')
            
            # Check if username or email already exists
            if User.query.filter_by(username=username).first():
                flash('Username already exists', 'error')
                return render_template('register.html')
            
            if User.query.filter_by(email=email).first():
                flash('Email already registered', 'error')
                return render_template('register.html')
            
            # Create new user
            user = User(username=username, email=email)
            user.set_password(password)
            
            # Add and commit to database
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        
        return render_template('register.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            # Find user by username
            user = User.query.filter_by(username=username).first()
            
            # Check if user exists and password is correct
            if user and user.check_password(password):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('home'))
            else:
                flash('Invalid username or password', 'error')
        
        return render_template('login.html')
    
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('You have been logged out', 'success')
        return redirect(url_for('home'))
    
    @app.route('/profile')
    @login_required
    def profile():
        return render_template('profile.html')
    
    # States routes for public access
    @app.route('/states/')
    def states_list():
        states = StateInfo.query.order_by(StateInfo.state_name).all()
        return render_template('states_list.html', states=states)
    
    @app.route('/states/<int:state_id>/')
    def state_detail(state_id):
        state = StateInfo.query.get_or_404(state_id)
        return render_template('state_detail.html', state=state)
    
    # NEC Articles routes for public access
    @app.route('/nec_articles/')
    def nec_articles_list():
        articles = NECArticle.query.order_by(NECArticle.article_number).all()
        return render_template('nec_list.html', articles=articles)
    
    @app.route('/nec_articles/<int:article_id>/')
    def nec_article_detail(article_id):
        article = NECArticle.query.get_or_404(article_id)
        return render_template('nec_detail.html', article=article)
    
    # Theory Topics routes for public access
    @app.route('/theory/')
    def theory_list():
        topics = TheoryTopic.query.order_by(TheoryTopic.title).all()
        # Group by category if needed
        categories = {}
        for topic in topics:
            category = topic.category or 'Uncategorized'
            if category not in categories:
                categories[category] = []
            categories[category].append(topic)
        return render_template('theory_list.html', topics=topics, categories=categories)
    
    @app.route('/theory/<int:topic_id>/')
    def theory_detail(topic_id):
        topic = TheoryTopic.query.get_or_404(topic_id)
        return render_template('theory_detail.html', topic=topic)
    
    # Calculation Tutorials routes for public access
    @app.route('/calculations/')
    def calculations_list():
        tutorials = CalculationTutorial.query.order_by(CalculationTutorial.title).all()
        return render_template('calculations_list.html', tutorials=tutorials)
    
    @app.route('/calculations/<int:tutorial_id>/')
    def calculation_detail(tutorial_id):
        tutorial = CalculationTutorial.query.get_or_404(tutorial_id)
        return render_template('calculation_detail.html', tutorial=tutorial)
    
    # Quiz routes for public access
    @app.route('/quiz/')
    def quiz_launcher():
        # Get all distinct topics from practice questions
        topics = db.session.query(PracticeQuestion.topic).distinct().all()
        topics = [topic[0] for topic in topics]  # Convert result to simple list
        topics.sort()  # Sort alphabetically
        return render_template('quiz_launcher.html', topics=topics)
    
    @app.route('/quiz/<topic_name>/')
    def quiz_interface(topic_name):
        import random
        # Get up to 10 random questions for the selected topic
        questions = PracticeQuestion.query.filter_by(topic=topic_name).all()
        
        if not questions:
            flash(f"No questions found for topic: {topic_name}", "error")
            return redirect(url_for('quiz_launcher'))
            
        # Randomize and limit to 10 questions
        if len(questions) > 10:
            questions = random.sample(questions, 10)
        
        # Convert SQLAlchemy objects to dictionaries for JSON serialization
        questions_data = []
        for q in questions:
            questions_data.append({
                'id': q.id,
                'question_text': q.question_text,
                'topic': q.topic,
                'difficulty': q.difficulty,
                'option_a': q.option_a,
                'option_b': q.option_b,
                'option_c': q.option_c,
                'option_d': q.option_d,
                'correct_option': q.correct_option,
                'explanation': q.explanation,
                'nec_reference': q.nec_reference
            })
            
        return render_template('quiz_interface.html', questions=questions_data, topic=topic_name)
    
    @app.route('/submit_quiz/<topic_name>/', methods=['POST'])
    @login_required
    def submit_quiz(topic_name):
        # Get submitted answers from JSON request
        data = request.get_json()
        answers = data.get('answers', [])
        
        # Initialize score
        score = 0
        total_questions = len(answers)
        
        # Check each answer against the correct answer in the database
        for answer in answers:
            # Skip if null or missing data
            if not answer or 'question_id' not in answer or 'selected_option' not in answer:
                continue
                
            question_id = answer['question_id']
            selected_option = answer['selected_option']
            
            # Get the question from database
            question = PracticeQuestion.query.get(question_id)
            
            # Skip if question not found
            if not question:
                continue
                
            # Check if the selected option is correct
            if selected_option == question.correct_option:
                score += 1
        
        # Save result to database
        if total_questions > 0:
            quiz_result = QuizResult(
                user_id=current_user.id,
                topic=topic_name,
                score=score,
                total_questions=total_questions
            )
            db.session.add(quiz_result)
            db.session.commit()
        
        # Calculate percentage for response
        percentage = round((score / total_questions) * 100) if total_questions > 0 else 0
        
        # Return the result as JSON
        return jsonify({
            'score': score,
            'total_questions': total_questions,
            'percentage': percentage
        })
    
    @app.route('/my_progress/')
    @login_required
    def my_progress():
        # Get all quiz results for the current user, ordered by most recent first
        results = QuizResult.query.filter_by(user_id=current_user.id).order_by(QuizResult.timestamp.desc()).all()
        return render_template('my_progress.html', results=results)
    
    # Admin blueprint
    admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
    
    @admin_bp.route('/')
    @admin_required
    def dashboard():
        states = StateInfo.query.all()
        return render_template('admin/dashboard.html', states=states)
    
    @admin_bp.route('/add_state', methods=['GET', 'POST'])
    @admin_required
    def add_state():
        if request.method == 'POST':
            state_name = request.form.get('state_name')
            
            # Basic validation
            if not state_name:
                flash('State name is required', 'error')
                return render_template('admin/add_edit_state.html', is_edit=False)
            
            # Check if state already exists
            if StateInfo.query.filter_by(state_name=state_name).first():
                flash('State already exists', 'error')
                return render_template('admin/add_edit_state.html', is_edit=False)
            
            # Create new state info
            state = StateInfo(
                state_name=state_name,
                license_types=request.form.get('license_types'),
                experience_reqs=request.form.get('experience_reqs'),
                application_info_link=request.form.get('application_info_link'),
                tested_nec_version=request.form.get('tested_nec_version'),
                exam_details=request.form.get('exam_details'),
                official_board_link=request.form.get('official_board_link')
            )
            
            # Add and commit to database
            db.session.add(state)
            db.session.commit()
            
            flash('State added successfully', 'success')
            return redirect(url_for('admin.dashboard'))
        
        return render_template('admin/add_edit_state.html', is_edit=False)
    
    @admin_bp.route('/edit_state/<int:state_id>', methods=['GET', 'POST'])
    @admin_required
    def edit_state(state_id):
        state = StateInfo.query.get_or_404(state_id)
        
        if request.method == 'POST':
            state_name = request.form.get('state_name')
            
            # Basic validation
            if not state_name:
                flash('State name is required', 'error')
                return render_template('admin/add_edit_state.html', is_edit=True, state=state)
            
            # Check if state name changed and new name already exists
            existing_state = StateInfo.query.filter_by(state_name=state_name).first()
            if existing_state and existing_state.id != state_id:
                flash('State name already exists', 'error')
                return render_template('admin/add_edit_state.html', is_edit=True, state=state)
            
            # Update state info
            state.state_name = state_name
            state.license_types = request.form.get('license_types')
            state.experience_reqs = request.form.get('experience_reqs')
            state.application_info_link = request.form.get('application_info_link')
            state.tested_nec_version = request.form.get('tested_nec_version')
            state.exam_details = request.form.get('exam_details')
            state.official_board_link = request.form.get('official_board_link')
            
            # Commit to database
            db.session.commit()
            
            flash('State updated successfully', 'success')
            return redirect(url_for('admin.dashboard'))
        
        return render_template('admin/add_edit_state.html', is_edit=True, state=state)
    
    @admin_bp.route('/delete_state/<int:state_id>', methods=['POST'])
    @admin_required
    def delete_state(state_id):
        state = StateInfo.query.get_or_404(state_id)
        
        # Delete and commit to database
        db.session.delete(state)
        db.session.commit()
        
        flash('State deleted successfully', 'success')
        return redirect(url_for('admin.dashboard'))
    
    # NEC Articles Admin Routes
    @admin_bp.route('/nec_articles/')
    @admin_required
    def nec_articles():
        articles = NECArticle.query.order_by(NECArticle.article_number).all()
        return render_template('admin/nec_articles_list.html', articles=articles)
    
    @admin_bp.route('/add_nec_article', methods=['GET', 'POST'])
    @admin_required
    def add_nec_article():
        if request.method == 'POST':
            article_number = request.form.get('article_number')
            title = request.form.get('title')
            content = request.form.get('content')
            summary = request.form.get('summary')
            
            # Basic validation
            if not all([article_number, title, content]):
                flash('Article number, title, and content are required', 'error')
                return render_template('admin/add_edit_nec_article.html', is_edit=False)
            
            # Create new NEC article
            article = NECArticle(
                article_number=article_number,
                title=title,
                content=content,
                summary=summary
            )
            
            # Add and commit to database
            db.session.add(article)
            db.session.commit()
            
            flash('NEC Article added successfully', 'success')
            return redirect(url_for('admin.nec_articles'))
        
        return render_template('admin/add_edit_nec_article.html', is_edit=False)
    
    @admin_bp.route('/edit_nec_article/<int:article_id>', methods=['GET', 'POST'])
    @admin_required
    def edit_nec_article(article_id):
        article = NECArticle.query.get_or_404(article_id)
        
        if request.method == 'POST':
            article_number = request.form.get('article_number')
            title = request.form.get('title')
            content = request.form.get('content')
            summary = request.form.get('summary')
            
            # Basic validation
            if not all([article_number, title, content]):
                flash('Article number, title, and content are required', 'error')
                return render_template('admin/add_edit_nec_article.html', is_edit=True, article=article)
            
            # Update article
            article.article_number = article_number
            article.title = title
            article.content = content
            article.summary = summary
            
            # Commit to database
            db.session.commit()
            
            flash('NEC Article updated successfully', 'success')
            return redirect(url_for('admin.nec_articles'))
        
        return render_template('admin/add_edit_nec_article.html', is_edit=True, article=article)
    
    @admin_bp.route('/delete_nec_article/<int:article_id>', methods=['POST'])
    @admin_required
    def delete_nec_article(article_id):
        article = NECArticle.query.get_or_404(article_id)
        
        # Delete and commit to database
        db.session.delete(article)
        db.session.commit()
        
        flash('NEC Article deleted successfully', 'success')
        return redirect(url_for('admin.nec_articles'))
    
    # Theory Topics Admin Routes
    @admin_bp.route('/theory_topics/')
    @admin_required
    def theory_topics():
        topics = TheoryTopic.query.order_by(TheoryTopic.title).all()
        return render_template('admin/theory_topics_list.html', topics=topics)
    
    @admin_bp.route('/add_theory_topic', methods=['GET', 'POST'])
    @admin_required
    def add_theory_topic():
        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            category = request.form.get('category')
            
            # Basic validation
            if not all([title, content]):
                flash('Title and content are required', 'error')
                return render_template('admin/add_edit_theory_topic.html', is_edit=False)
            
            # Check if topic already exists
            if TheoryTopic.query.filter_by(title=title).first():
                flash('Topic with this title already exists', 'error')
                return render_template('admin/add_edit_theory_topic.html', is_edit=False)
            
            # Create new theory topic
            topic = TheoryTopic(
                title=title,
                content=content,
                category=category
            )
            
            # Add and commit to database
            db.session.add(topic)
            db.session.commit()
            
            flash('Theory Topic added successfully', 'success')
            return redirect(url_for('admin.theory_topics'))
        
        return render_template('admin/add_edit_theory_topic.html', is_edit=False)
    
    @admin_bp.route('/edit_theory_topic/<int:topic_id>', methods=['GET', 'POST'])
    @admin_required
    def edit_theory_topic(topic_id):
        topic = TheoryTopic.query.get_or_404(topic_id)
        
        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            category = request.form.get('category')
            
            # Basic validation
            if not all([title, content]):
                flash('Title and content are required', 'error')
                return render_template('admin/add_edit_theory_topic.html', is_edit=True, topic=topic)
            
            # Check if title changed and new title already exists
            existing_topic = TheoryTopic.query.filter_by(title=title).first()
            if existing_topic and existing_topic.id != topic_id:
                flash('Topic with this title already exists', 'error')
                return render_template('admin/add_edit_theory_topic.html', is_edit=True, topic=topic)
            
            # Update topic
            topic.title = title
            topic.content = content
            topic.category = category
            
            # Commit to database
            db.session.commit()
            
            flash('Theory Topic updated successfully', 'success')
            return redirect(url_for('admin.theory_topics'))
        
        return render_template('admin/add_edit_theory_topic.html', is_edit=True, topic=topic)
    
    @admin_bp.route('/delete_theory_topic/<int:topic_id>', methods=['POST'])
    @admin_required
    def delete_theory_topic(topic_id):
        topic = TheoryTopic.query.get_or_404(topic_id)
        
        # Delete and commit to database
        db.session.delete(topic)
        db.session.commit()
        
        flash('Theory Topic deleted successfully', 'success')
        return redirect(url_for('admin.theory_topics'))
    
    # Calculation Tutorials Admin Routes
    @admin_bp.route('/calc_tutorials/')
    @admin_required
    def calc_tutorials():
        tutorials = CalculationTutorial.query.order_by(CalculationTutorial.title).all()
        return render_template('admin/calc_tutorials_list.html', tutorials=tutorials)
    
    @admin_bp.route('/add_calc_tutorial', methods=['GET', 'POST'])
    @admin_required
    def add_calc_tutorial():
        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            related_nec_articles = request.form.get('related_nec_articles')
            
            # Basic validation
            if not all([title, content]):
                flash('Title and content are required', 'error')
                return render_template('admin/add_edit_calc_tutorial.html', is_edit=False)
            
            # Check if tutorial already exists
            if CalculationTutorial.query.filter_by(title=title).first():
                flash('Tutorial with this title already exists', 'error')
                return render_template('admin/add_edit_calc_tutorial.html', is_edit=False)
            
            # Create new calculation tutorial
            tutorial = CalculationTutorial(
                title=title,
                content=content,
                related_nec_articles=related_nec_articles
            )
            
            # Add and commit to database
            db.session.add(tutorial)
            db.session.commit()
            
            flash('Calculation Tutorial added successfully', 'success')
            return redirect(url_for('admin.calc_tutorials'))
        
        return render_template('admin/add_edit_calc_tutorial.html', is_edit=False)
    
    @admin_bp.route('/edit_calc_tutorial/<int:tutorial_id>', methods=['GET', 'POST'])
    @admin_required
    def edit_calc_tutorial(tutorial_id):
        tutorial = CalculationTutorial.query.get_or_404(tutorial_id)
        
        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            related_nec_articles = request.form.get('related_nec_articles')
            
            # Basic validation
            if not all([title, content]):
                flash('Title and content are required', 'error')
                return render_template('admin/add_edit_calc_tutorial.html', is_edit=True, tutorial=tutorial)
            
            # Check if title changed and new title already exists
            existing_tutorial = CalculationTutorial.query.filter_by(title=title).first()
            if existing_tutorial and existing_tutorial.id != tutorial_id:
                flash('Tutorial with this title already exists', 'error')
                return render_template('admin/add_edit_calc_tutorial.html', is_edit=True, tutorial=tutorial)
            
            # Update tutorial
            tutorial.title = title
            tutorial.content = content
            tutorial.related_nec_articles = related_nec_articles
            
            # Commit to database
            db.session.commit()
            
            flash('Calculation Tutorial updated successfully', 'success')
            return redirect(url_for('admin.calc_tutorials'))
        
        return render_template('admin/add_edit_calc_tutorial.html', is_edit=True, tutorial=tutorial)
    
    @admin_bp.route('/delete_calc_tutorial/<int:tutorial_id>', methods=['POST'])
    @admin_required
    def delete_calc_tutorial(tutorial_id):
        tutorial = CalculationTutorial.query.get_or_404(tutorial_id)
        
        # Delete and commit to database
        db.session.delete(tutorial)
        db.session.commit()
        
        flash('Calculation Tutorial deleted successfully', 'success')
        return redirect(url_for('admin.calc_tutorials'))
    
    # Practice Questions Admin Routes
    @admin_bp.route('/questions/')
    @admin_required
    def questions():
        # Get filter by topic if provided
        topic_filter = request.args.get('topic')
        
        if topic_filter:
            questions = PracticeQuestion.query.filter_by(topic=topic_filter).order_by(PracticeQuestion.id.desc()).all()
        else:
            questions = PracticeQuestion.query.order_by(PracticeQuestion.id.desc()).all()
        
        # Get all unique topics for filter dropdown
        topics = db.session.query(PracticeQuestion.topic).distinct().all()
        topics = [topic[0] for topic in topics]
        
        return render_template('admin/questions_list.html', questions=questions, topics=topics, current_topic=topic_filter)
    
    @admin_bp.route('/add_question', methods=['GET', 'POST'])
    @admin_required
    def add_question():
        if request.method == 'POST':
            question_text = request.form.get('question_text')
            option_a = request.form.get('option_a')
            option_b = request.form.get('option_b')
            option_c = request.form.get('option_c')
            option_d = request.form.get('option_d')
            correct_option = request.form.get('correct_option')
            explanation = request.form.get('explanation')
            nec_reference = request.form.get('nec_reference')
            topic = request.form.get('topic')
            
            # Basic validation
            if not all([question_text, option_a, option_b, option_c, option_d, correct_option, topic]):
                flash('All fields except explanation and NEC reference are required', 'error')
                return render_template('admin/add_edit_question.html', is_edit=False)
            
            # Create new practice question
            question = PracticeQuestion(
                question_text=question_text,
                option_a=option_a,
                option_b=option_b,
                option_c=option_c,
                option_d=option_d,
                correct_option=correct_option,
                explanation=explanation,
                nec_reference=nec_reference,
                topic=topic
            )
            
            # Add and commit to database
            db.session.add(question)
            db.session.commit()
            
            flash('Practice question added successfully', 'success')
            return redirect(url_for('admin.questions'))
        
        return render_template('admin/add_edit_question.html', is_edit=False)
    
    @admin_bp.route('/edit_question/<int:question_id>', methods=['GET', 'POST'])
    @admin_required
    def edit_question(question_id):
        question = PracticeQuestion.query.get_or_404(question_id)
        
        if request.method == 'POST':
            question_text = request.form.get('question_text')
            option_a = request.form.get('option_a')
            option_b = request.form.get('option_b')
            option_c = request.form.get('option_c')
            option_d = request.form.get('option_d')
            correct_option = request.form.get('correct_option')
            explanation = request.form.get('explanation')
            nec_reference = request.form.get('nec_reference')
            topic = request.form.get('topic')
            
            # Basic validation
            if not all([question_text, option_a, option_b, option_c, option_d, correct_option, topic]):
                flash('All fields except explanation and NEC reference are required', 'error')
                return render_template('admin/add_edit_question.html', is_edit=True, question=question)
            
            # Update question
            question.question_text = question_text
            question.option_a = option_a
            question.option_b = option_b
            question.option_c = option_c
            question.option_d = option_d
            question.correct_option = correct_option
            question.explanation = explanation
            question.nec_reference = nec_reference
            question.topic = topic
            
            # Commit to database
            db.session.commit()
            
            flash('Practice question updated successfully', 'success')
            return redirect(url_for('admin.questions'))
        
        return render_template('admin/add_edit_question.html', is_edit=True, question=question)
    
    @admin_bp.route('/delete_question/<int:question_id>', methods=['POST'])
    @admin_required
    def delete_question(question_id):
        question = PracticeQuestion.query.get_or_404(question_id)
        
        # Delete and commit to database
        db.session.delete(question)
        db.session.commit()
        
        flash('Practice question deleted successfully', 'success')
        return redirect(url_for('admin.questions'))
    
    # Register blueprints
    app.register_blueprint(admin_bp)
    
    return app

# Create the application instance
app = create_app()

# When running directly, create database tables and start the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5004) 
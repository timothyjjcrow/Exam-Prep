from flask import Flask, render_template, request, jsonify, Blueprint, send_from_directory
import os
import tempfile
import random

# Conditionally import the proper models
if os.environ.get('VERCEL'):
    from vercel_models import db, StateInfo, NECArticle, TheoryTopic, CalculationTutorial, PracticeQuestion
else:
    from models import db, StateInfo, NECArticle, TheoryTopic, CalculationTutorial, PracticeQuestion

from markupsafe import Markup

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    
    # Special configuration for Vercel environment
    if os.environ.get('VERCEL'):
        # Use in-memory SQLite for Vercel
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'vercel-deployment-key')
        # Set track modifications to False to avoid warning
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        # Serve static files correctly in Vercel
        @app.route('/static/<path:path>')
        def serve_static(path):
            return send_from_directory('static', path)
    else:
        # Local configuration
        app.config.from_object('config')
        # Set track modifications to False to avoid warning
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database with app
    db.init_app(app)
    
    # Add custom Jinja2 filters
    @app.template_filter('nl2br')
    def nl2br_filter(s):
        if s:
            s = s.replace('\n', '<br>')
            return Markup(s)
        return s
    
    # Define routes
    @app.route('/')
    def home():
        return render_template('vercel_home.html')
    
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
    
    # Quiz routes for public access (but without saving results)
    @app.route('/quiz/')
    def quiz_launcher():
        # Get all distinct topics from practice questions
        topics = db.session.query(PracticeQuestion.topic).distinct().all()
        topics = [topic[0] for topic in topics]  # Convert result to simple list
        topics.sort()  # Sort alphabetically
        return render_template('vercel_quiz_launcher.html', topics=topics)
    
    @app.route('/quiz/<topic_name>/')
    def quiz_interface(topic_name):
        # Get up to 10 random questions for the selected topic
        questions = PracticeQuestion.query.filter_by(topic=topic_name).all()
        
        if not questions:
            return render_template('vercel_quiz_launcher.html', 
                                  topics=[], 
                                  error_message=f"No questions found for topic: {topic_name}")
            
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
            
        return render_template('vercel_quiz_interface.html', questions=questions_data, topic=topic_name)
    
    # Public quiz submission endpoint (just returns score, doesn't save to database)
    @app.route('/submit_quiz/<topic_name>/', methods=['POST'])
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
        
        # Calculate percentage for response
        percentage = round((score / total_questions) * 100) if total_questions > 0 else 0
        
        # Return the result as JSON
        return jsonify({
            'score': score,
            'total_questions': total_questions,
            'percentage': percentage
        })

    return app

# For local development
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5005) 
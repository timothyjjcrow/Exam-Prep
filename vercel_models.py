from flask_sqlalchemy import SQLAlchemy
import datetime

# Initialize SQLAlchemy
db = SQLAlchemy()

class BaseUser():
    """Base user model without UserMixin for Vercel deployment"""
    id = None
    username = None
    email = None
    password_hash = None
    date_registered = None

class TheoryTopic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<TheoryTopic {self.title}>'

class StateInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(100), unique=True, nullable=False)
    license_types = db.Column(db.Text)
    experience_reqs = db.Column(db.Text)
    application_info_link = db.Column(db.String(255))
    tested_nec_version = db.Column(db.String(50))
    exam_details = db.Column(db.Text)
    official_board_link = db.Column(db.String(255))
    
    def __repr__(self):
        return f'<StateInfo {self.state_name}>'

class NECArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_number = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)
    
    def __repr__(self):
        return f'<NECArticle {self.article_number} - {self.title}>'

class CalculationTutorial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    related_nec_articles = db.Column(db.String(255))
    
    def __repr__(self):
        return f'<CalculationTutorial {self.title}>'

class PracticeQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(20), default='medium', nullable=False)
    option_a = db.Column(db.Text, nullable=False)
    option_b = db.Column(db.Text, nullable=False)
    option_c = db.Column(db.Text, nullable=False)
    option_d = db.Column(db.Text, nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)
    explanation = db.Column(db.Text)
    nec_reference = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return f'<PracticeQuestion {self.id}: {self.question_text[:30]}...>'

# QuizResult class removed as it's not needed for Vercel deployment 
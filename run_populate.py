from app import app
from populate_quiz import populate_questions

with app.app_context():
    populate_questions() 
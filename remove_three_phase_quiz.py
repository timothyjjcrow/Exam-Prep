import sys
import os
from flask import Flask

# Add the parent directory to sys.path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app, db
from models import PracticeQuestion

def remove_three_phase_quiz():
    """Removes all questions related to 3-Phase Power Systems from the database."""
    try:
        # Find all questions with the 3-Phase Power Systems topic
        questions = PracticeQuestion.query.filter_by(topic="3-Phase Power Systems").all()
        
        if not questions:
            print("No questions found for the topic '3-Phase Power Systems'.")
            return False
        
        # Display how many questions will be deleted
        count = len(questions)
        print(f"Found {count} questions for topic '3-Phase Power Systems'.")
        
        # Delete all questions with this topic
        for question in questions:
            db.session.delete(question)
        
        # Commit the changes
        db.session.commit()
        print(f"Successfully removed {count} questions from the '3-Phase Power Systems' quiz.")
        return True
    
    except Exception as e:
        db.session.rollback()
        print(f"Error removing 3-Phase Power Systems quiz: {str(e)}")
        return False

def main():
    """Main function to create app context and run the removal function."""
    try:
        app = create_app()
        with app.app_context():
            remove_three_phase_quiz()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
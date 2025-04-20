from app import app
from models import db, PracticeQuestion

with app.app_context():
    # Check Boxes and Enclosures topic
    topic = "Boxes and Enclosures"
    count = PracticeQuestion.query.filter_by(topic=topic).count()
    
    print(f"Questions for topic '{topic}': {count}")
    
    if count > 0:
        questions = PracticeQuestion.query.filter_by(topic=topic).all()
        
        print("\nFirst 5 questions:")
        for i, q in enumerate(questions[:5]):
            print(f"{i+1}. {q.question_text[:100]}...")
        
        print("\nLast 5 questions:")
        for i, q in enumerate(questions[-5:]):
            print(f"{i+1}. {q.question_text[:100]}...") 
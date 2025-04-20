from app import app
from models import db, PracticeQuestion

with app.app_context():
    # Get all distinct topics
    topics = db.session.query(PracticeQuestion.topic).distinct().all()
    topics = [topic[0] for topic in topics]
    
    print('Available topics:')
    for topic in topics:
        print(f'- {topic}')
    
    print('\nQuestion counts per topic:')
    for topic in topics:
        count = PracticeQuestion.query.filter_by(topic=topic).count()
        print(f'- {topic}: {count} questions')
        
    print('\nTotal questions:', PracticeQuestion.query.count()) 
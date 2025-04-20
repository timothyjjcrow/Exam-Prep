from app import app
import requests
import json
import re

with app.app_context():
    from models import db, PracticeQuestion
    
    # Get all unique topics
    topics = db.session.query(PracticeQuestion.topic).distinct().all()
    topics = [topic[0] for topic in topics]
    
    # Check actual server responses
    print("Checking number of questions displayed for each topic...")
    for topic in topics[:5]:  # Just check first 5 to save time
        url = f"http://127.0.0.1:5004/quiz/{topic.replace(' ', '%20')}/"
        response = requests.get(url)
        
        # Use regex to find quizQuestions array
        pattern = r'const quizQuestions = (\[.*?\]);'
        match = re.search(pattern, response.text, re.DOTALL)
        
        if match:
            questions_str = match.group(1)
            try:
                questions = json.loads(questions_str)
                print(f"Topic '{topic}': {len(questions)} questions displayed in quiz")
            except json.JSONDecodeError:
                print(f"Topic '{topic}': Could not parse questions array")
        else:
            print(f"Topic '{topic}': Could not find questions array") 
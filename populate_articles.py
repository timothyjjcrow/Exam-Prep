#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime

# Add the parent directory to the path so we can import the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from circuit_breaker_app import app, db
from circuit_breaker_app.models import NECArticle, TheoryTopic

def populate_nec_articles(json_data):
    """
    Populate the database with NEC articles from the JSON data.
    Check if articles already exist to avoid duplicates.
    """
    articles_added = 0
    articles_skipped = 0
    
    print("Populating NEC Articles...")
    
    for article_data in json_data.get('NECArticlesReference', []):
        # Check if article already exists
        existing_article = NECArticle.query.filter_by(
            article_number=article_data['article_number']).first()
        
        if existing_article:
            print(f"Skipping existing article: {article_data['article_number']} - {article_data['title']}")
            articles_skipped += 1
            continue
        
        # Create new article
        new_article = NECArticle(
            article_number=article_data['article_number'],
            title=article_data['title'],
            summary=article_data['summary'],
            content=article_data['content'],
            created_at=datetime.utcnow()
        )
        
        db.session.add(new_article)
        articles_added += 1
        print(f"Added article: {article_data['article_number']} - {article_data['title']}")
    
    try:
        db.session.commit()
        print(f"Successfully added {articles_added} NEC articles ({articles_skipped} skipped)")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding NEC articles: {e}")

def populate_theory_topics(json_data):
    """
    Populate the database with electrical theory topics from the JSON data.
    Check if topics already exist to avoid duplicates.
    """
    topics_added = 0
    topics_skipped = 0
    
    print("Populating Electrical Theory Topics...")
    
    for topic_data in json_data.get('generalElectricalTheoryTopics', []):
        # Check if topic already exists
        existing_topic = TheoryTopic.query.filter_by(
            title=topic_data['title']).first()
        
        if existing_topic:
            print(f"Skipping existing topic: {topic_data['title']}")
            topics_skipped += 1
            continue
        
        # Create new topic
        new_topic = TheoryTopic(
            title=topic_data['title'],
            category=topic_data['category'],
            content=topic_data['content'],
            created_at=datetime.utcnow()
        )
        
        db.session.add(new_topic)
        topics_added += 1
        print(f"Added topic: {topic_data['title']}")
    
    try:
        db.session.commit()
        print(f"Successfully added {topics_added} theory topics ({topics_skipped} skipped)")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding theory topics: {e}")

def main():
    # Use with app context to access database
    with app.app_context():
        try:
            # Load the JSON data
            json_file_path = 'electrical_content.json'
            if not os.path.exists(json_file_path):
                # Check in parent directory too
                json_file_path = os.path.join('..', 'electrical_content.json')
            
            with open(json_file_path, 'r') as file:
                json_data = json.load(file)
            
            # Populate NEC articles
            populate_nec_articles(json_data)
            
            # Populate electrical theory topics
            populate_theory_topics(json_data)
            
            print("Data population complete!")
            
        except FileNotFoundError:
            print(f"Error: Could not find the JSON file at {json_file_path}")
        except json.JSONDecodeError:
            print("Error: The JSON file is not valid")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 
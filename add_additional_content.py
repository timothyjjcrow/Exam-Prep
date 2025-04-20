#!/usr/bin/env python3
import json
from app import create_app, db
from models import NECArticle, TheoryTopic

# New data in the different format
DATA = {
  "NEC_articles": [
    {
      "article_number": 90,
      "title": "Introduction",
      "summary": """Establishes the purpose, scope, and general arrangement of the NEC. It explains that the Code's purpose is to safeguard people and property from electrical hazards and that it is not intended as a design manual or an untrained person's instruction guide.""",
      "high_frequency": False
    },
    {
      "article_number": 100,
      "title": "Definitions",
      "summary": """Contains official definitions of technical terms that are fundamental to interpreting the NEC properly. Article 100 provides definitions for terms used in two or more articles (for example, the precise meaning of a "dwelling unit" or an "outlet" in Code language). Understanding these definitions is critical, as many Code requirements and exam questions rely on the exact NEC terminology.""",
      "high_frequency": False
    },
    {
      "article_number": 110,
      "title": "Requirements for Electrical Installations",
      "summary": """Covers general installation requirements for all electrical equipment and installations. This article ensures that equipment is installed safely: it must be approved (listed and labeled for the purpose), used according to manufacturer instructions, and installed in a neat and workmanlike manner. Article 110 also covers provisions like adequate working space around electrical equipment (such as the clearances required in front of panels per 110.26) and proper markings.""",
      "high_frequency": False
    },
    {
      "article_number": 200,
      "title": "Use and Identification of Grounded Conductors",
      "summary": """Provides rules for the neutral or grounded conductors, including how they must be identified and used. Grounded circuit conductors (neutrals) must have proper color coding or marking (typically continuous white or gray on small conductors), and larger neutrals can be re-identified at terminations.""",
      "high_frequency": False
    },
    {
      "article_number": 210,
      "title": "Branch Circuits",
      "summary": """Covers the requirements for branch circuits—the circuits that extend from the last overcurrent device to outlets (lighting, receptacles, appliances). This article is extensive and especially important for dwelling wiring.""",
      "high_frequency": True
    },
    {
      "article_number": 215,
      "title": "Feeders",
      "summary": """Covers feeder circuits, which carry power from the service equipment or main panel to downstream distribution panels or disconnects. It provides rules for sizing feeder conductors and their overcurrent protection so that feeders safely carry the calculated load.""",
      "high_frequency": False
    },
    {
      "article_number": 220,
      "title": "Branch-Circuit, Feeder, and Service Load Calculations",
      "summary": """Provides the methods for calculating electrical loads on branch circuits, feeders, and services. It details how to compute the total load of a building or circuit by accounting for all lighting, receptacle, appliance, and motor loads, often with demand factors to allow realistic sizing.""",
      "high_frequency": True
    },
    {
      "article_number": 225,
      "title": "Outside Branch Circuits and Feeders",
      "summary": """Covers branch circuits and feeders run outdoors, such as conductors between buildings or to outdoor equipment. It includes rules for overhead spans and underground runs outside structures.""",
      "high_frequency": False
    },
    {
      "article_number": 430,
      "title": "Motors, Motor Circuits, and Controllers",
      "summary": """This extensive article covers motors and motor-operated equipment, including how to size wires, fuses/breakers, and overloads for motor circuits. Motors have high inrush currents on start-up, so the Code allows branch-circuit protection to be much larger than normal.""",
      "high_frequency": True
    }
  ],
  "Theory_topics": [
    {
      "title": "Basic Electrical Units and Ohm's Law",
      "category": "Foundational",
      "explanation": """This topic introduces the fundamental electrical quantities: Voltage (V), Current (I), and Resistance (R). Voltage is the electrical pressure that pushes current through a circuit (measured in volts), current is the flow of electric charge (measured in amperes), and resistance is the opposition to current flow (measured in ohms).""",
      "equations": [
        "V = I * R",
        "I = V / R",
        "R = V / I"
      ]
    },
    {
      "title": "Series Circuits",
      "category": "Foundational",
      "explanation": """In a series circuit, components are connected end-to-end so that there is only one path for current to flow. Consequently, the same current flows through each component in the series. The total resistance of series components is the sum of their individual resistances.""",
      "equations": [
        "R_total = R_1 + R_2 + ... + R_n",
        "I_1 = I_2 = ... = I_total",
        "V_total = V_1 + V_2 + ... + V_n"
      ]
    },
    {
      "title": "Parallel Circuits",
      "category": "Foundational",
      "explanation": """In a parallel circuit, components are connected across the same two points, providing multiple paths for current. In a parallel configuration, the voltage across each branch is the same (equal to the source voltage), while the total current is the sum of the currents through each branch.""",
      "equations": [
        "1/R_total = 1/R_1 + 1/R_2 + ... + 1/R_n",
        "V_1 = V_2 = ... = V_source",
        "I_total = I_1 + I_2 + ... + I_n"
      ]
    },
    {
      "title": "Electrical Power and Energy",
      "category": "Foundational",
      "explanation": """Electrical power is the rate at which electrical energy is transferred or consumed, measured in watts (W). In DC or purely resistive AC circuits, power can be calculated as P = V × I (voltage times current).""",
      "equations": [
        "P = V * I",
        "P = I^2 * R",
        "P = V^2 / R",
        "E = P * t"
      ]
    }
  ]
}

def format_nec_content(article):
    """Format NEC article content for database storage"""
    html_content = f"""
    <h3>Article {article['article_number']} - {article['title']}</h3>
    <p>{article['summary']}</p>
    """
    
    if article.get('high_frequency', False):
        html_content += "<p><strong>Note:</strong> This is a high-frequency topic that appears regularly on exams.</p>"
        
    return html_content

def format_theory_content(topic):
    """Format theory topic content for database storage"""
    html_content = f"""
    <h3>{topic['title']}</h3>
    <p>{topic['explanation']}</p>
    """
    
    if topic.get('equations'):
        html_content += "<h4>Key Equations:</h4><ul>"
        for equation in topic['equations']:
            html_content += f"<li><code>{equation}</code></li>"
        html_content += "</ul>"
        
    return html_content

def populate_additional_nec_articles():
    """Populate the database with additional NEC articles"""
    articles_added = 0
    articles_skipped = 0
    
    print("Populating Additional NEC Articles...")
    
    for article_data in DATA.get('NEC_articles', []):
        # Check if article already exists
        existing_article = NECArticle.query.filter_by(
            article_number=article_data['article_number']).first()
        
        if existing_article:
            # Update existing article with any new information
            if existing_article.title != article_data['title'] or existing_article.summary != article_data['summary']:
                existing_article.title = article_data['title']
                existing_article.summary = article_data['summary']
                existing_article.content = format_nec_content(article_data)
                db.session.add(existing_article)
                print(f"Updated existing article: {article_data['article_number']} - {article_data['title']}")
                articles_added += 1
            else:
                print(f"Skipping unchanged article: {article_data['article_number']} - {article_data['title']}")
                articles_skipped += 1
            continue
        
        # Create new article
        new_article = NECArticle(
            article_number=article_data['article_number'],
            title=article_data['title'],
            summary=article_data['summary'],
            content=format_nec_content(article_data)
        )
        
        db.session.add(new_article)
        articles_added += 1
        print(f"Added article: {article_data['article_number']} - {article_data['title']}")
    
    try:
        db.session.commit()
        print(f"Successfully added/updated {articles_added} NEC articles ({articles_skipped} skipped)")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding NEC articles: {e}")

def populate_additional_theory_topics():
    """Populate the database with additional theory topics"""
    topics_added = 0
    topics_skipped = 0
    
    print("Populating Additional Theory Topics...")
    
    for topic_data in DATA.get('Theory_topics', []):
        # Check if topic already exists
        existing_topic = TheoryTopic.query.filter_by(
            title=topic_data['title']).first()
        
        if existing_topic:
            # Update existing topic with any new information
            if existing_topic.category != topic_data['category']:
                existing_topic.category = topic_data['category']
                existing_topic.content = format_theory_content(topic_data)
                db.session.add(existing_topic)
                print(f"Updated existing topic: {topic_data['title']}")
                topics_added += 1
            else:
                print(f"Skipping unchanged topic: {topic_data['title']}")
                topics_skipped += 1
            continue
        
        # Create new topic
        new_topic = TheoryTopic(
            title=topic_data['title'],
            category=topic_data['category'],
            content=format_theory_content(topic_data)
        )
        
        db.session.add(new_topic)
        topics_added += 1
        print(f"Added topic: {topic_data['title']}")
    
    try:
        db.session.commit()
        print(f"Successfully added/updated {topics_added} theory topics ({topics_skipped} skipped)")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding theory topics: {e}")

def main():
    # Create app and push context
    app = create_app()
    with app.app_context():
        try:
            # Populate NEC articles
            populate_additional_nec_articles()
            
            # Populate electrical theory topics
            populate_additional_theory_topics()
            
            print("Additional data population complete!")
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 
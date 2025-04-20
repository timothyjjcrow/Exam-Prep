from models import db, TheoryTopic, NECArticle, StateInfo, PracticeQuestion, CalculationTutorial

def initialize_db(app):
    """Initialize the in-memory database with essential data for the read-only version"""
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Add basic theory topics
        if TheoryTopic.query.count() == 0:
            theory_topics = [
                {
                    "title": "Basic Electrical Theory",
                    "category": "Foundational Electrical Theory",
                    "content": """<p>Electrical theory is built on a foundation of fundamental concepts that explain how electricity works and how it can be controlled.</p>
                    <p>At its core is the understanding of three basic electrical quantities: Voltage (V), Current (I), and Resistance (R).</p>"""
                },
                {
                    "title": "Ohm's Law",
                    "category": "Foundational Electrical Theory",
                    "content": """<p>Ohm's Law states that the current flowing through a conductor between two points is directly proportional to the voltage across the two points and inversely proportional to the resistance between them.</p>
                    <p>Key equation: V = I × R</p>"""
                }
            ]
            
            for topic_data in theory_topics:
                topic = TheoryTopic(**topic_data)
                db.session.add(topic)
            
            db.session.commit()
        
        # Add sample NEC articles
        if NECArticle.query.count() == 0:
            nec_articles = [
                {
                    "article_number": "100",
                    "title": "Definitions",
                    "content": """<p>This article contains definitions essential to the proper application of the NEC.</p>""",
                    "summary": "Provides definitions of terms used throughout the code."
                },
                {
                    "article_number": "110",
                    "title": "Requirements for Electrical Installations",
                    "content": """<p>This article covers general requirements for electrical installations.</p>""",
                    "summary": "General requirements for electrical installations, including examination, installation, and use of equipment."
                }
            ]
            
            for article_data in nec_articles:
                article = NECArticle(**article_data)
                db.session.add(article)
            
            db.session.commit()
        
        # Add sample state info
        if StateInfo.query.count() == 0:
            states = [
                {
                    "state_name": "California",
                    "license_types": "C-10 Electrical Contractor",
                    "experience_reqs": "4 years of journeyman-level experience",
                    "tested_nec_version": "2020 NEC"
                },
                {
                    "state_name": "Texas",
                    "license_types": "Master Electrician, Journeyman Electrician",
                    "experience_reqs": "Master: 2 years as journeyman. Journeyman: 8,000 hours",
                    "tested_nec_version": "2020 NEC"
                }
            ]
            
            for state_data in states:
                state = StateInfo(**state_data)
                db.session.add(state)
            
            db.session.commit()
        
        # Add sample practice questions
        if PracticeQuestion.query.count() == 0:
            questions = [
                {
                    "question_text": "What is the current in a circuit with 120V and 60Ω resistance?",
                    "topic": "Ohm's Law",
                    "difficulty": "easy",
                    "option_a": "0.5A",
                    "option_b": "2A",
                    "option_c": "60A",
                    "option_d": "120A",
                    "correct_option": "b",
                    "explanation": "Using Ohm's Law: I = V/R = 120V/60Ω = 2A"
                },
                {
                    "question_text": "What is the minimum size of equipment grounding conductor required for a 100A circuit?",
                    "topic": "Grounding and Bonding",
                    "difficulty": "medium",
                    "option_a": "8 AWG",
                    "option_b": "6 AWG",
                    "option_c": "4 AWG",
                    "option_d": "2 AWG",
                    "correct_option": "a",
                    "explanation": "Per NEC Table 250.122, an 8 AWG copper conductor is the minimum size required.",
                    "nec_reference": "Table 250.122"
                }
            ]
            
            for question_data in questions:
                question = PracticeQuestion(**question_data)
                db.session.add(question)
            
            db.session.commit()
        
        # Add sample calculation tutorials
        if CalculationTutorial.query.count() == 0:
            tutorials = [
                {
                    "title": "Voltage Drop Calculations",
                    "content": """<p>Voltage drop calculations are important for ensuring proper operation of electrical equipment.</p>
                    <p>The basic formula is: Vd = 2 × L × I × R / 1000 for DC circuits.</p>""",
                    "related_nec_articles": "210, 215"
                }
            ]
            
            for tutorial_data in tutorials:
                tutorial = CalculationTutorial(**tutorial_data)
                db.session.add(tutorial)
            
            db.session.commit()
            
        print("Database initialized with sample data for Vercel deployment") 
import sys
import os
from flask import Flask
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app, db
from models import TheoryTopic

def update_basic_theory_topics():
    """Updates basic electrical theory topics with proper MathJax formatting."""
    
    topics_updated = 0
    topics_added = 0
    
    # Define the basic electrical theory topics with proper MathJax formatting
    basic_topics = [
        {
            "title": "Basic Electrical Theory",
            "category": "Foundational Electrical Theory",
            "content": """<p>Electrical theory is built on a foundation of fundamental concepts that explain how electricity works and how it can be controlled. At its core is the understanding of three basic electrical quantities:</p>
            
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'><strong>Voltage (V):</strong> The electrical pressure or potential difference that drives current through a circuit, measured in volts (V).</li>
    <li class='key-equation'><strong>Current (I):</strong> The flow of electrical charge (electrons) through a conductor, measured in amperes (A).</li>
    <li class='key-equation'><strong>Resistance (R):</strong> The opposition to current flow in a material, measured in ohms (Ω).</li>
  </ul>
</div>

<p>These quantities are related by Ohm's Law, which states that current is directly proportional to voltage and inversely proportional to resistance.</p>

<p>Electrical circuits can be categorized as:</p>
<ul>
  <li><strong>Direct Current (DC):</strong> Current flows in one direction only. Examples include batteries and solar cells.</li>
  <li><strong>Alternating Current (AC):</strong> Current periodically reverses direction. This is the form of electricity delivered to homes and businesses by the utility grid.</li>
</ul>

<p>Understanding these basic principles is essential for safely working with electrical systems, diagnosing problems, and designing effective solutions. Electricians must be able to apply these concepts in practical situations to ensure safety and compliance with electrical codes.</p>"""
        },
        {
            "title": "Ohm's Law",
            "category": "Foundational Electrical Theory",
            "content": """<p>Ohm's Law states that the current flowing through a conductor between two points is directly proportional to the voltage across the two points and inversely proportional to the resistance between them.</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Voltage-Current-Resistance relationship: \\(V = I \\times R\\)</li>
    <li class='key-equation'>Current calculation: \\(I = \\frac{V}{R}\\)</li>
    <li class='key-equation'>Resistance calculation: \\(R = \\frac{V}{I}\\)</li>
  </ul>
</div>

<p>Where:</p>
<ul>
  <li>V = Voltage (in volts, V)</li>
  <li>I = Current (in amperes, A)</li>
  <li>R = Resistance (in ohms, Ω)</li>
</ul>

<p>Ohm's Law is essential for calculating circuit values and designing electrical systems that operate safely and efficiently. It allows electricians to:</p>
<ul>
  <li>Determine how much current will flow in a circuit with known voltage and resistance</li>
  <li>Calculate voltage drops across components</li>
  <li>Size conductors and components appropriately</li>
  <li>Troubleshoot electrical problems by identifying variations from expected values</li>
</ul>

<p>The Ohm's Law wheel or triangle is a common mnemonic device used to remember these relationships, with V at the top, and I and R at the bottom corners.</p>"""
        },
        {
            "title": "Power and Energy in Electrical Circuits",
            "category": "Foundational Electrical Theory",
            "content": """<h3>Electrical Power</h3>
<p>Power is the rate at which energy is transferred or converted. In electrical systems, power is measured in watts (W).</p>

<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Basic power formula: \\(P = V \\times I\\)</li>
    <li class='key-equation'>Power using resistance and current: \\(P = I^2 \\times R\\)</li>
    <li class='key-equation'>Power using voltage and resistance: \\(P = \\frac{V^2}{R}\\)</li>
  </ul>
</div>

<p>Where:</p>
<ul>
  <li>P = Power (in watts, W)</li>
  <li>V = Voltage (in volts, V)</li>
  <li>I = Current (in amperes, A)</li>
  <li>R = Resistance (in ohms, Ω)</li>
</ul>

<h3>Electrical Energy</h3>
<p>Energy is the capacity to do work, measured in watt-hours (Wh) or kilowatt-hours (kWh) in electrical systems.</p>

<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Energy calculation: \\(E = P \\times t\\)</li>
  </ul>
</div>

<p>Where:</p>
<ul>
  <li>E = Energy (in watt-hours, Wh)</li>
  <li>P = Power (in watts, W)</li>
  <li>t = Time (in hours, h)</li>
</ul>

<p>For example: A 100W light bulb operating for 10 hours consumes: 100W × 10h = 1000Wh = 1kWh</p>

<p>Understanding power and energy calculations is essential for:</p>
<ul>
  <li>Sizing electrical systems and components</li>
  <li>Estimating operating costs of electrical equipment</li>
  <li>Ensuring components are rated appropriately for their intended use</li>
  <li>Calculating energy efficiency and conservation measures</li>
</ul>"""
        }
    ]
    
    try:
        for topic_data in basic_topics:
            # Check if the topic already exists
            existing_topic = TheoryTopic.query.filter_by(title=topic_data['title']).first()
            
            if existing_topic:
                # Update existing topic
                existing_topic.category = topic_data['category']
                existing_topic.content = topic_data['content']
                topics_updated += 1
                print(f"Updated existing topic: {topic_data['title']}")
            else:
                # Create new topic
                new_topic = TheoryTopic(
                    title=topic_data['title'],
                    category=topic_data['category'],
                    content=topic_data['content']
                )
                db.session.add(new_topic)
                topics_added += 1
                print(f"Added new topic: {topic_data['title']}")
        
        db.session.commit()
        print(f"Successfully updated basic theory topics. Added: {topics_added}, Updated: {topics_updated}")
        return True
    
    except Exception as e:
        db.session.rollback()
        print(f"Error updating basic theory topics: {str(e)}")
        return False

def main():
    """Main function to create app context and run the update function."""
    try:
        app = create_app()
        with app.app_context():
            update_basic_theory_topics()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
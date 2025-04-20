import sys
import os
from flask import Flask
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app, db
from models import TheoryTopic

def update_foundational_topics():
    """Updates foundational electrical theory topics with proper MathJax formatting."""
    
    topics_updated = 0
    topics_added = 0
    
    # Define the foundational topics with proper MathJax formatting
    foundational_topics = [
        {
            "title": "Basic Electrical Units and Ohm's Law",
            "category": "Foundational Electrical Theory",
            "content": """<p>This topic introduces the fundamental electrical quantities: Voltage (V), Current (I), and Resistance (R). Voltage is the electrical pressure that pushes current through a circuit (measured in volts), current is the flow of electric charge (measured in amperes), and resistance is the opposition to current flow (measured in ohms).</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Voltage: \\(V = I \\times R\\)</li>
    <li class='key-equation'>Current: \\(I = \\frac{V}{R}\\)</li>
    <li class='key-equation'>Resistance: \\(R = \\frac{V}{I}\\)</li>
  </ul>
</div>

<p>Ohm's Law is one of the most important and fundamental relationships in electrical theory. It forms the basis for circuit analysis and is essential knowledge for anyone working in the electrical field.</p>"""
        },
        {
            "title": "Series Circuits",
            "category": "Foundational Electrical Theory",
            "content": """<p>In a series circuit, components are connected end-to-end so that there is only one path for current to flow. Consequently, the same current flows through each component in the series. The total resistance of series components is the sum of their individual resistances.</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Total resistance: \\(R_{total} = R_1 + R_2 + ... + R_n\\)</li>
    <li class='key-equation'>Current: \\(I_1 = I_2 = ... = I_{total}\\)</li>
    <li class='key-equation'>Voltage: \\(V_{total} = V_1 + V_2 + ... + V_n\\)</li>
  </ul>
</div>

<p>In series circuits, if any component fails open, the entire circuit stops working. This principle is used in Christmas lights (older style) where one bad bulb breaks the entire string.</p>"""
        },
        {
            "title": "Parallel Circuits",
            "category": "Foundational Electrical Theory",
            "content": """<p>In a parallel circuit, components are connected across the same two points, providing multiple paths for current. In a parallel configuration, the voltage across each branch is the same (equal to the source voltage), while the total current is the sum of the currents through each branch.</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Total resistance: \\(\\frac{1}{R_{total}} = \\frac{1}{R_1} + \\frac{1}{R_2} + ... + \\frac{1}{R_n}\\)</li>
    <li class='key-equation'>Voltage: \\(V_1 = V_2 = ... = V_{source}\\)</li>
    <li class='key-equation'>Current: \\(I_{total} = I_1 + I_2 + ... + I_n\\)</li>
  </ul>
</div>

<p>Parallel circuits are common in household wiring, where each outlet or light is connected in parallel. This allows each device to operate independently of others.</p>"""
        },
        {
            "title": "Electrical Power and Energy",
            "category": "Foundational Electrical Theory",
            "content": """<p>Electrical power is the rate at which electrical energy is transferred or consumed, measured in watts (W). In DC or purely resistive AC circuits, power can be calculated as P = V × I (voltage times current).</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Power: \\(P = V \\times I\\)</li>
    <li class='key-equation'>Power (using resistance): \\(P = I^2 \\times R\\)</li>
    <li class='key-equation'>Power (using voltage): \\(P = \\frac{V^2}{R}\\)</li>
    <li class='key-equation'>Energy: \\(E = P \\times t\\)</li>
  </ul>
</div>

<p>Energy is power consumed over time, measured in watt-hours (Wh) or kilowatt-hours (kWh). This is what your electric utility bills you for. For example, a 100W light bulb running for 10 hours consumes 1 kWh of energy.</p>"""
        },
        {
            "title": "Voltage Drop Calculations",
            "category": "Foundational Electrical Theory",
            "content": """<p>Voltage drop is the reduction in voltage as current flows through the resistance of conductors. While the NEC doesn't always mandate voltage drop limits in every scenario, it provides recommended practices (often aiming for no more than 3% drop on a branch circuit and 5% overall).</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Voltage drop: \\(V_{drop} = I \\times R_{total}\\)</li>
    <li class='key-equation'>Total resistance: \\(R_{total} = 2 \\times R_{per\\text{-}ft} \\times L\\text{ (for round-trip length)}\\)</li>
    <li class='key-equation'>Percent voltage drop: \\(\\%V_{drop} = \\frac{V_{drop}}{V_{source}} \\times 100\\%\\)</li>
  </ul>
</div>

<p>Excessive voltage drop can cause equipment to malfunction or operate inefficiently. For example, motors may run slower or hotter, and lights may dim. Proper conductor sizing is essential to minimize voltage drop, especially for long runs.</p>"""
        }
    ]
    
    try:
        for topic_data in foundational_topics:
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
        print(f"Successfully updated foundational theory topics. Added: {topics_added}, Updated: {topics_updated}")
        return True
    
    except Exception as e:
        db.session.rollback()
        print(f"Error updating foundational theory topics: {str(e)}")
        return False

def main():
    """Main function to create app context and run the update function."""
    try:
        app = create_app()
        with app.app_context():
            update_foundational_topics()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
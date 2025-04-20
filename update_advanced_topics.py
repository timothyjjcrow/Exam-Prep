import sys
import os
from flask import Flask
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app, db
from models import TheoryTopic

def update_advanced_topics():
    """Updates advanced electrical theory topics with proper MathJax formatting."""
    
    topics_updated = 0
    topics_added = 0
    
    # Define the advanced topics with proper MathJax formatting
    advanced_topics = [
        {
            "title": "AC Reactance and Impedance",
            "category": "Advanced Electrical Theory",
            "content": """<p>In AC circuits, especially those with inductors or capacitors, resistors are not the only opposition to current – we also have reactance. Inductive reactance (X<sub>L</sub>) is the opposition an inductor provides to AC, measured in ohms. It increases with frequency: a coil has X<sub>L</sub> = 2π f L, meaning at higher frequency or with a larger inductance L, it's harder for AC to flow.</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Inductive reactance: \\(X_L = 2\\pi f L\\)</li>
    <li class='key-equation'>Capacitive reactance: \\(X_C = \\frac{1}{2\\pi f C}\\)</li>
    <li class='key-equation'>Impedance: \\(Z = \\sqrt{R^2 + (X_L - X_C)^2}\\)</li>
  </ul>
</div>

<p>Reactance differs from resistance in that it depends on frequency. For inductors, reactance increases with frequency, while for capacitors, it decreases. In AC circuit analysis, impedance (Z) combines both resistance and reactance, providing the total opposition to current flow.</p>"""
        },
        {
            "title": "AC Power and Power Factor",
            "category": "Advanced Electrical Theory",
            "content": """<p>AC power comes in three forms: real power (P) measured in watts (W), reactive power (Q) measured in volt-amperes reactive (VAR), and apparent power (S) measured in volt-amperes (VA). Real power is actual work done (heat, motion, light), whereas reactive power oscillates between source and load.</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Real power: \\(P = V I \\cos\\phi\\)</li>
    <li class='key-equation'>Reactive power: \\(Q = V I \\sin\\phi\\)</li>
    <li class='key-equation'>Power factor: \\(PF = \\frac{P}{S} = \\cos\\phi\\)</li>
    <li class='key-equation'>Apparent power: \\(S = \\sqrt{P^2 + Q^2}\\)</li>
  </ul>
</div>

<p>Power factor is a critical concept in electrical systems. A low power factor (below 0.9) indicates inefficient power use and may incur utility penalties. Power factor correction, often using capacitors, helps bring the power factor closer to unity by offsetting inductive loads like motors.</p>"""
        },
        {
            "title": "Three-Phase Power Systems",
            "category": "Advanced Electrical Theory",
            "content": """<p>Three-phase power systems use three AC voltages, phased 120° apart, to deliver power more efficiently, especially for motors and heavy loads. In a three-phase system, we often talk about line-to-line voltages (e.g., 208 V, 480 V) and line currents.</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Line-to-line voltage related to phase voltage: \\(V_{LL} = \\sqrt{3} \\times V_{LN}\\)</li>
    <li class='key-equation'>Three-phase power: \\(P_{3\\phi} = \\sqrt{3} \\times V_{LL} \\times I_{L} \\times \\cos\\phi\\)</li>
    <li class='key-equation'>Phase current in wye connection: \\(I_{phase} = I_{line}\\)</li>
  </ul>
</div>

<p>These relationships are essential for calculating proper conductor sizing, protection devices, and equipment ratings in three-phase systems.</p>"""
        },
        {
            "title": "Transformers",
            "category": "Advanced Electrical Theory",
            "content": """<p>Transformers are devices that transfer AC power between circuits through electromagnetic induction, usually changing the voltage in the process. Key principles: The ratio of the voltages equals the ratio of the turns on the coils.</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Turns ratio relationship: \\(\\frac{V_p}{V_s} = \\frac{N_p}{N_s} = \\frac{I_s}{I_p}\\)</li>
    <li class='key-equation'>Power relationship: \\(P_{primary} \\approx P_{secondary} = V_p I_p = V_s I_s\\)</li>
    <li class='key-equation'>Secondary current: \\(I_{secondary} = \\frac{V_p}{V_s} I_{primary}\\)</li>
  </ul>
</div>

<p>These equations help electricians size transformers and determine secondary current values. For an ideal transformer (100% efficiency), the power input equals the power output. Real transformers have losses, including core losses (hysteresis and eddy currents) and copper losses (resistive heating in the windings).</p>"""
        },
        {
            "title": "Electric Motors",
            "category": "Advanced Electrical Theory",
            "content": """<p>Electric motors convert electrical energy into mechanical work. For AC motors (like the common three-phase induction motor), several concepts are important: synchronous speed – the speed of the rotating magnetic field, given by 120 * frequency / number of poles.</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Synchronous speed: \\(n_{sync} = \\frac{120 f}{P}\\text{ (speed in RPM)}\\)</li>
    <li class='key-equation'>Power conversion: \\(1 \\text{ hp} = 746 \\text{ W}\\)</li>
    <li class='key-equation'>Torque calculation: \\(T (\\text{lb-ft}) = \\frac{5252 \\times \\text{hp}}{n(\\text{RPM})}\\)</li>
  </ul>
</div>

<p>Understanding these relationships helps electricians properly size motors and their protection devices. Motor efficiency, typically 75-95%, affects the relationship between electrical input power and mechanical output power. The NEC has specific requirements for motor circuit protection based on full-load current.</p>"""
        }
    ]
    
    try:
        for topic_data in advanced_topics:
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
        print(f"Successfully updated advanced theory topics. Added: {topics_added}, Updated: {topics_updated}")
        return True
    
    except Exception as e:
        db.session.rollback()
        print(f"Error updating advanced theory topics: {str(e)}")
        return False

def main():
    """Main function to create app context and run the update function."""
    try:
        app = create_app()
        with app.app_context():
            update_advanced_topics()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
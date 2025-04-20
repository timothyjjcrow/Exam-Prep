import sys
import os
import json
from flask import Flask
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app, db
from models import TheoryTopic

def update_theory_topics():
    """Updates electrical theory topics in the database with new content."""
    topics_added = 0
    topics_updated = 0
    
    updated_topics = [
        {
            "title": "Ohm's Law",
            "category": "Basic Electrical Theory",
            "content": "<p>Ohm's Law states that the current flowing through a conductor between two points is directly proportional to the voltage across the two points and inversely proportional to the resistance between them.</p><p>Expressed mathematically:</p><p><strong>V = I × R</strong></p><p>Where:</p><ul><li>V = Voltage (in volts, V)</li><li>I = Current (in amperes, A)</li><li>R = Resistance (in ohms, Ω)</li></ul><p>This fundamental relationship can be rearranged to find any of the three values:</p><ul><li>To find current: I = V ÷ R</li><li>To find resistance: R = V ÷ I</li></ul><p>Ohm's Law is essential for calculating circuit values and designing electrical systems that operate safely and efficiently.</p>"
        },
        {
            "title": "Series and Parallel Circuits",
            "category": "Basic Electrical Theory",
            "content": "<h3>Series Circuits</h3><p>In a series circuit, components are connected end-to-end, forming a single path for current to flow.</p><p>Key characteristics:</p><ul><li>The same current flows through each component</li><li>The total resistance is the sum of all individual resistances: R<sub>total</sub> = R<sub>1</sub> + R<sub>2</sub> + R<sub>3</sub> + ...</li><li>The total voltage is divided among the components: V<sub>total</sub> = V<sub>1</sub> + V<sub>2</sub> + V<sub>3</sub> + ...</li><li>If one component fails open, the entire circuit stops working</li></ul><h3>Parallel Circuits</h3><p>In a parallel circuit, components are connected across common points, providing multiple paths for current.</p><p>Key characteristics:</p><ul><li>The same voltage appears across each component</li><li>The total current is the sum of currents through each branch: I<sub>total</sub> = I<sub>1</sub> + I<sub>2</sub> + I<sub>3</sub> + ...</li><li>The reciprocal of the total resistance equals the sum of the reciprocals of individual resistances: 1/R<sub>total</sub> = 1/R<sub>1</sub> + 1/R<sub>2</sub> + 1/R<sub>3</sub> + ...</li><li>If one component fails open, the other components continue to operate</li></ul><p>Most practical circuits contain combinations of series and parallel arrangements.</p>"
        },
        {
            "title": "Power and Energy in Electrical Circuits",
            "category": "Basic Electrical Theory",
            "content": "<h3>Electrical Power</h3><p>Power is the rate at which energy is transferred or converted. In electrical systems, power is measured in watts (W).</p><p>The basic power formula is:</p><p><strong>P = V × I</strong></p><p>Where:</p><ul><li>P = Power (in watts, W)</li><li>V = Voltage (in volts, V)</li><li>I = Current (in amperes, A)</li></ul><p>Using Ohm's Law, we can derive alternative power formulas:</p><ul><li>P = I<sup>2</sup> × R (current squared times resistance)</li><li>P = V<sup>2</sup> ÷ R (voltage squared divided by resistance)</li></ul><h3>Electrical Energy</h3><p>Energy is the capacity to do work, measured in watt-hours (Wh) or kilowatt-hours (kWh) in electrical systems.</p><p><strong>Energy = Power × Time</strong></p><p>For example:</p><ul><li>A 100W light bulb operating for 10 hours consumes: 100W × 10h = 1000Wh = 1kWh</li></ul><p>Understanding power and energy calculations is essential for sizing electrical systems, estimating operating costs, and ensuring components are rated appropriately for their intended use.</p>"
        },
        {
            "title": "Magnetism and Electromagnetism",
            "category": "Basic Electrical Theory",
            "content": "<h3>Basic Magnetism</h3><p>Magnetism is the phenomenon associated with magnetic fields, which exert forces on other magnets and magnetic materials.</p><p>Key concepts:</p><ul><li>Magnetic fields are represented by lines of force emerging from the north pole and entering the south pole</li><li>Like poles repel, unlike poles attract</li><li>Magnetic fields can penetrate most materials</li><li>Ferromagnetic materials (iron, nickel, cobalt) can be magnetized</li></ul><h3>Electromagnetism</h3><p>Electromagnetism is the relationship between electricity and magnetism:</p><ul><li>A current-carrying conductor produces a magnetic field around it</li><li>The magnetic field forms concentric circles around the conductor</li><li>The direction of the magnetic field follows the right-hand rule: when the thumb points in the direction of current flow, the fingers curl in the direction of the magnetic field</li></ul><h3>Electromagnetic Induction</h3><p>Electromagnetic induction, discovered by Michael Faraday, is the production of voltage across a conductor when it is exposed to a changing magnetic field.</p><p>Faraday's Law states that the induced electromotive force (EMF) in a circuit is proportional to the rate of change of magnetic flux through the circuit.</p><p>This principle is the foundation for generators, transformers, and many other electrical devices.</p>"
        },
        {
            "title": "Transformers",
            "category": "Basic Electrical Theory",
            "content": "<h3>Basic Transformer Principles</h3><p>A transformer is a device that transfers electrical energy between two or more circuits through electromagnetic induction. It consists of two or more coils of wire wound around a common core.</p><p>Key components:</p><ul><li>Primary winding: Connected to the power source</li><li>Secondary winding: Connected to the load</li><li>Core: Usually made of laminated iron sheets to provide a path for magnetic flux</li></ul><h3>Transformer Operation</h3><p>The operation is based on two principles:</p><ol><li>A changing current in the primary winding creates a changing magnetic field in the core</li><li>This changing magnetic field induces a voltage in the secondary winding</li></ol><h3>Transformer Ratios</h3><p>The ratio of secondary voltage to primary voltage equals the ratio of secondary turns to primary turns:</p><p><strong>V<sub>s</sub>/V<sub>p</sub> = N<sub>s</sub>/N<sub>p</sub></strong></p><p>For an ideal transformer (100% efficiency), power in equals power out:</p><p><strong>V<sub>p</sub> × I<sub>p</sub> = V<sub>s</sub> × I<sub>s</sub></strong></p><p>Therefore:</p><p><strong>I<sub>s</sub>/I<sub>p</sub> = N<sub>p</sub>/N<sub>s</sub></strong></p><h3>Types of Transformers</h3><ul><li>Step-up: Secondary voltage higher than primary (N<sub>s</sub> > N<sub>p</sub>)</li><li>Step-down: Secondary voltage lower than primary (N<sub>s</sub> < N<sub>p</sub>)</li><li>Isolation: Primary and secondary voltages equal (N<sub>s</sub> = N<sub>p</sub>)</li></ul><p>Transformers are essential in power distribution systems, allowing voltage to be increased for efficient transmission and decreased for safe use by consumers.</p>"
        },
        {
            "title": "Electrical Safety Fundamentals",
            "category": "Electrical Safety",
            "content": "<h3>Electrical Hazards</h3><p>Electrical hazards include:</p><ul><li>Electric shock: Current passing through the body</li><li>Burns: Both from electric current and arc flash</li><li>Arc blast: Explosion caused by high-current arcs</li><li>Fire: From heat generated by electrical faults</li><li>Explosions: In environments with flammable materials</li></ul><h3>Shock Prevention</h3><p>Key safety practices include:</p><ol><li>De-energization: Always work on de-energized circuits when possible</li><li>Lockout/Tagout (LOTO): Procedures ensuring equipment remains de-energized during maintenance</li><li>Insulation: Using proper tools with insulated handles</li><li>Grounding: Proper grounding of equipment and systems</li><li>Ground Fault Circuit Interrupters (GFCIs): For wet locations and other hazardous areas</li><li>Personal Protective Equipment (PPE): Including insulating gloves, mats, and appropriate clothing</li></ol><h3>Safe Work Practices</h3><p>Follow these guidelines:</p><ul><li>Never assume a circuit is de-energized—always test before touching</li><li>Use appropriate test equipment rated for the voltage</li><li>Maintain a safe distance from energized parts</li><li>Use the "one hand rule" when possible (keeping one hand behind your back)</li><li>Avoid working on energized equipment when standing on wet surfaces</li><li>Follow all applicable codes and standards, including NFPA 70E</li></ul><p>Remember: No task is so important that it cannot be done safely. When in doubt, stop and seek guidance from a qualified person.</p>"
        },
        {
            "title": "Three-Phase Power Systems",
            "category": "Advanced Electrical Theory",
            "content": "<p>Three-phase power systems use three AC voltages, phased 120° apart, to deliver power more efficiently, especially for motors and heavy loads. In a three-phase system, we often talk about line-to-line voltages (e.g., 208 V, 480 V) and line currents.</p><h3>Key Equations:</h3><div class='math-container'><ul class='equation-list'><li class='key-equation'>Line-to-line voltage related to phase voltage: \\(V_{LL} = \\sqrt{3} \\times V_{LN}\\)</li><li class='key-equation'>Three-phase power: \\(P_{3\\phi} = \\sqrt{3} \\times V_{LL} \\times I_{L} \\times \\cos\\phi\\)</li><li class='key-equation'>Phase current in wye connection: \\(I_{phase} = I_{line}\\)</li></ul></div><p>These relationships are essential for calculating proper conductor sizing, protection devices, and equipment ratings in three-phase systems.</p>"
        }
    ]
    
    try:
        for topic_data in updated_topics:
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
        print(f"Successfully updated theory topics. Added: {topics_added}, Updated: {topics_updated}")
    
    except Exception as e:
        db.session.rollback()
        print(f"Error updating theory topics: {str(e)}")
        return False
    
    return True

def update_three_phase_topic():
    """Updates the Three-Phase Power Systems topic with MathJax formatting."""
    
    try:
        # Check if the topic already exists
        existing_topic = TheoryTopic.query.filter_by(title="Three-Phase Power Systems").first()
        
        three_phase_content = """<p>Three-phase power systems use three AC voltages, phased 120° apart, to deliver power more efficiently, especially for motors and heavy loads. In a three-phase system, we often talk about line-to-line voltages (e.g., 208 V, 480 V) and line currents.</p>
        
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>Line-to-line voltage related to phase voltage: \\(V_{LL} = \\sqrt{3} \\times V_{LN}\\)</li>
    <li class='key-equation'>Three-phase power: \\(P_{3\\phi} = \\sqrt{3} \\times V_{LL} \\times I_{L} \\times \\cos\\phi\\)</li>
    <li class='key-equation'>Phase current in wye connection: \\(I_{phase} = I_{line}\\)</li>
  </ul>
</div>

<p>These relationships are essential for calculating proper conductor sizing, protection devices, and equipment ratings in three-phase systems.</p>"""
        
        if existing_topic:
            # Update existing topic
            existing_topic.category = "Advanced Electrical Theory"
            existing_topic.content = three_phase_content
            print(f"Updated existing Three-Phase Power Systems topic")
        else:
            # Create new topic
            new_topic = TheoryTopic(
                title="Three-Phase Power Systems",
                category="Advanced Electrical Theory",
                content=three_phase_content
            )
            db.session.add(new_topic)
            print(f"Added new Three-Phase Power Systems topic")
        
        db.session.commit()
        print(f"Successfully updated Three-Phase Power Systems topic with MathJax formatting")
        return True
    
    except Exception as e:
        db.session.rollback()
        print(f"Error updating Three-Phase Power Systems topic: {str(e)}")
        return False

def main():
    """Main function to create app context and run the update function."""
    try:
        app = create_app()
        with app.app_context():
            update_theory_topics()
            update_three_phase_topic()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
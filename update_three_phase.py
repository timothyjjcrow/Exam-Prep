import sys
import os
from flask import Flask
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app, db
from models import TheoryTopic

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
            update_three_phase_topic()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
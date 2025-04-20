import sys
import os
from flask import Flask
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app, db
from models import TheoryTopic

def update_additional_topics():
    """Updates additional foundational electrical theory topics with proper MathJax formatting."""
    
    topics_updated = 0
    topics_added = 0
    
    # Define the additional topics with proper MathJax formatting
    additional_topics = [
        {
            "title": "Alternating Current (AC) Fundamentals",
            "category": "Foundational Electrical Theory",
            "content": """<p>Alternating Current (AC) is an electric current that periodically reverses direction, unlike Direct Current (DC) which flows in only one direction. In most power systems, AC follows a sinusoidal wave form – voltage and current rise and fall in a sine wave pattern, switching polarity at a fixed frequency (60 Hz in the US, meaning 60 cycles per second).</p>
            
<h3>Key Equations:</h3>
<div class='math-container'>
  <ul class='equation-list'>
    <li class='key-equation'>RMS voltage: \\(V_{rms} = 0.707 \\times V_{peak}\\)</li>
    <li class='key-equation'>Frequency and period relationship: \\(f = \\frac{1}{T}\\)</li>
    <li class='key-equation'>Instantaneous voltage: \\(v(t) = V_{peak} \\sin(2\\pi f t)\\)</li>
  </ul>
</div>

<p>AC power offers several advantages over DC. It can be easily transformed to higher or lower voltages using transformers, which enables efficient long-distance power transmission at high voltages (reducing losses) and then stepping down to safer voltages for consumer use. The sinusoidal nature of AC also makes rotating machinery (motors and generators) simpler to design and operate.</p>

<p>In the US, residential and commercial power is delivered as single-phase AC at 120/240V, 60Hz. Most of the world uses 230V, 50Hz systems. Three-phase AC power, which uses three conductors with voltages offset by 120 degrees, is common in industrial settings and for transmission due to its greater efficiency and smoother power delivery.</p>"""
        },
        {
            "title": "Grounding vs. Bonding Basics",
            "category": "Foundational Electrical Theory",
            "content": """<p>Grounding and bonding are essential safety principles in electrical systems that are often confused but serve distinct purposes.</p>

<h3>Grounding</h3>
<p>Grounding refers to establishing a connection between electrical systems, circuits, or equipment and the earth (ground). This connection provides a reference point of zero potential and a path for fault currents to flow safely to earth. The primary purposes of grounding include:</p>
<ul>
  <li>Stabilizing voltage levels</li>
  <li>Protecting people and equipment from high voltages due to lightning or utility switching</li>
  <li>Facilitating the operation of overcurrent devices during fault conditions</li>
</ul>

<p>Two key types of grounding are:</p>
<ol>
  <li><strong>System Grounding:</strong> Connecting a conductor of an electrical system (typically the neutral) to earth</li>
  <li><strong>Equipment Grounding:</strong> Connecting non-current-carrying metal parts of equipment to earth</li>
</ol>

<h3>Bonding</h3>
<p>Bonding involves connecting all metallic parts that could become energized to ensure electrical continuity and conductivity between them. The purpose is to create a low-impedance path for fault current, which:</p>
<ul>
  <li>Ensures that all conductive surfaces are at the same potential, minimizing voltage differences</li>
  <li>Allows protective devices (fuses, circuit breakers) to operate quickly during fault conditions</li>
  <li>Reduces shock hazards by preventing potential differences between touchable surfaces</li>
</ul>

<p>The National Electrical Code (NEC) Article 250 covers grounding and bonding requirements in detail, specifying wire sizes, connection methods, and testing procedures. For typical residential services, the main bonding jumper connects the neutral bus to the enclosure of the service panel, while the grounding electrode conductor connects the system to earth, often via ground rods or water pipes.</p>

<p>Remember this key distinction: grounding establishes a connection to earth, while bonding connects conductive parts together to maintain equal potential. Both are critical for electrical safety.</p>"""
        }
    ]
    
    try:
        for topic_data in additional_topics:
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
        print(f"Successfully updated additional theory topics. Added: {topics_added}, Updated: {topics_updated}")
        return True
    
    except Exception as e:
        db.session.rollback()
        print(f"Error updating additional theory topics: {str(e)}")
        return False

def main():
    """Main function to create app context and run the update function."""
    try:
        app = create_app()
        with app.app_context():
            update_additional_topics()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 240 to the database."""
    article_data = {
        "article_number": "240",
        "title": "Overcurrent Protection",
        "summary": "Requirements for overcurrent protection and overcurrent protective devices. Covers the selection and installation of devices that protect conductors and equipment from overcurrents.",
        "content": """
<h3>Scope and Purpose</h3>
<p>Article 240 provides the requirements for selecting and installing overcurrent protection devices (OCPDs) for conductors and equipment. Overcurrent protection is fundamental to electrical safety as it prevents excessive current from causing overheating, insulation damage, and fires.</p>

<h3>Key Definitions and Concepts</h3>
<ul>
    <li><strong>Overcurrent:</strong> Any current in excess of the rated current of equipment or the ampacity of a conductor. May result from overload, short circuit, or ground fault.</li>
    <li><strong>Overload:</strong> Operation of equipment in excess of normal, full-load rating that, when it persists for a sufficient length of time, would cause damage or dangerous overheating.</li>
    <li><strong>Short Circuit:</strong> An abnormal connection (including an arc) of relatively low impedance between two points of different potential.</li>
    <li><strong>Ground Fault:</strong> An unintentional, electrically conducting connection between an ungrounded conductor and the normally non-current-carrying conductors, metallic enclosures, or earth.</li>
</ul>

<h3>Types of Overcurrent Protective Devices</h3>
<p>Article 240 covers various types of overcurrent protective devices, including:</p>
<ul>
    <li><strong>Fuses:</strong> One-time protective devices that melt when current exceeds their rating</li>
    <li><strong>Circuit Breakers:</strong> Reusable protective devices that trip when current exceeds their rating</li>
    <li><strong>Supplementary Overcurrent Protective Devices:</strong> Limited in application and typically used within equipment</li>
</ul>

<h3>General Requirements (Part I)</h3>
<ul>
    <li><strong>240.4 Protection of Conductors:</strong> Conductors must be protected against overcurrent in accordance with their ampacities as specified in 310.15, with specific provisions for small conductors:
        <ul>
            <li>14 AWG copper: 15 amperes</li>
            <li>12 AWG copper: 20 amperes</li>
            <li>10 AWG copper: 30 amperes</li>
            <li>Similar provisions for aluminum and copper-clad aluminum conductors</li>
        </ul>
    </li>
    
    <li><strong>240.6 Standard Ampere Ratings:</strong> Standard ratings for fuses and fixed-trip circuit breakers are 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, and 6000 amperes.</li>
    
    <li><strong>240.8 Fuses or Circuit Breakers in Parallel:</strong> Fuses and circuit breakers shall not be connected in parallel except as permitted under engineering supervision in industrial installations.</li>
    
    <li><strong>240.9 Thermal Devices:</strong> Thermal relays and other devices not designed to open short circuits or ground faults shall not be used for the protection of conductors against overcurrent due to short circuits or ground faults.</li>
    
    <li><strong>240.10 Supplementary Overcurrent Protection:</strong> Supplementary overcurrent protection (such as those used within appliances) is not a substitute for required branch-circuit overcurrent devices.</li>
</ul>

<h3>Location Requirements (Part II)</h3>
<ul>
    <li><strong>240.21 Location in Circuit:</strong> Overcurrent protection shall be provided at the point where the conductor receives its supply, with specific exceptions:
        <ul>
            <li>Taps not exceeding 10 feet (240.21(B)(1))</li>
            <li>Feeder taps not exceeding 25 feet (240.21(B)(2))</li>
            <li>Transformer secondary conductors (240.21(C))</li>
            <li>Service conductors (240.21(D))</li>
        </ul>
    </li>
    
    <li><strong>240.24 Location in or on Premises:</strong>
        <ul>
            <li>OCPDs shall be readily accessible and not exposed to physical damage</li>
            <li>Not located in bathrooms or near easily ignitable material</li>
            <li>Not located in the vicinity of easily ignitable material, such as in clothes closets</li>
            <li>Located where occupants can readily access them for dwelling units</li>
        </ul>
    </li>
</ul>

<h3>Enclosures (Part III)</h3>
<ul>
    <li><strong>240.30 General:</strong> Overcurrent devices shall be enclosed in cabinets, cutout boxes, or equipment assemblies, with specific provisions for specific types of installations.</li>
    
    <li><strong>240.33 Vertical Position:</strong> Enclosures shall be mounted in a vertical position unless this is impracticable.</li>
</ul>

<h3>Disconnecting and Guarding (Part IV)</h3>
<ul>
    <li><strong>240.40 Disconnecting Means for Fuses:</strong> Disconnecting means shall be provided on the supply side of all fuses in circuits over 150 volts to ground and cartridge fuses in circuits of any voltage where accessible to other than qualified persons.</li>
    
    <li><strong>240.41 Arcing or Suddenly Moving Parts:</strong> Arcing or suddenly moving parts shall be guarded to prevent injury to persons.</li>
</ul>

<h3>Plug Fuses, Fuseholders, and Adapters (Part V)</h3>
<ul>
    <li><strong>240.50 General:</strong> Requirements for plug fuses, fuseholders, and adapters, including Type S fuses which are designed to prevent installation of fuses with ampere ratings higher than intended for the circuit.</li>
    
    <li><strong>240.53 Type S Fuses, Adapters, and Fuseholders:</strong> Only Type S fuses shall be installed in fuseholders for replacements in existing installations where the overcurrent device is rated 15 amperes or less and 125 volts or less.</li>
</ul>

<h3>Cartridge Fuses and Fuseholders (Part VI)</h3>
<ul>
    <li><strong>240.60 General:</strong> Requirements for cartridge fuses and fuseholders, including classifications by voltage (300V or less, 301-1000V) and interrupting rating (standard or high-interrupting current).</li>
    
    <li><strong>240.61 Classification:</strong> Cartridge fuses and fuseholders shall be classified according to voltage and amperage ranges.</li>
</ul>

<h3>Circuit Breakers (Part VII)</h3>
<ul>
    <li><strong>240.80 Method of Operation:</strong> Circuit breakers shall be trip free (capable of tripping even if the handle is held in the ON position) and capable of being closed and opened by manual operation.</li>
    
    <li><strong>240.81 Indicating:</strong> Circuit breakers shall clearly indicate whether they are in the open (off) or closed (on) position.</li>
    
    <li><strong>240.82 Nontamperable:</strong> A circuit breaker shall be of such design that any alteration of its trip point or time required for operation requires dismantling or destroying the breaker.</li>
    
    <li><strong>240.83 Marking:</strong> Circuit breakers shall be durably marked with their ampere rating, and if adjustable, must indicate each adjustment position.</li>
    
    <li><strong>240.85 Applications:</strong> Circuit breakers shall have a voltage rating not less than the nominal system voltage. Circuit breakers with interrupting ratings higher than 5000 amperes shall have their interrupting rating displayed.</li>
    
    <li><strong>240.86 Series Ratings:</strong> Specific provisions for series-rated combinations where circuit breakers are used in a series combination with other circuit breakers or fuses to achieve higher interrupting ratings.</li>
</ul>

<h3>Supervised Industrial Installations (Part VIII)</h3>
<p>This part provides modified overcurrent protection requirements for specific industrial installations that are under qualified electrical engineering supervision, allowing more flexible approaches to overcurrent protection in controlled environments.</p>

<h3>Critical Applications and Common Issues</h3>
<ul>
    <li><strong>Conductor Protection:</strong> Ensuring conductors are properly protected based on their ampacities is foundational to preventing fires.</li>
    
    <li><strong>Selectivity:</strong> Designing systems so that only the OCPD closest to a fault opens, maintaining power to unaffected circuits (known as selective coordination).</li>
    
    <li><strong>Accessibility:</strong> OCPDs must be readily accessible for quick disconnection in emergencies, but must not be accessible to unqualified persons in certain applications.</li>
    
    <li><strong>Tap Conductor Rules:</strong> The complex rules for protecting tap conductors are frequently misapplied, leading to potential safety issues.</li>
    
    <li><strong>Series Ratings:</strong> Proper application of series-rated equipment requires careful review of manufacturers' specifications and proper labeling.</li>
    
    <li><strong>Common Violations:</strong>
        <ul>
            <li>Using overcurrent devices with ratings that exceed the ampacity of the protected conductors</li>
            <li>Installing OCPDs in inaccessible locations</li>
            <li>Improper protection of tap conductors</li>
            <li>Using standard OCPDs where high-interrupting capacity devices are required</li>
            <li>Missing required disconnecting means for fuses</li>
        </ul>
    </li>
</ul>

<h3>Recent Code Changes</h3>
<p>Recent editions of the NEC have included updates to Article 240 such as:</p>
<ul>
    <li>Clarified requirements for series ratings and documentation</li>
    <li>Expanded provisions for ground-fault protection</li>
    <li>Updated requirements for accessibility and location of overcurrent devices</li>
    <li>Refined tap conductor rules</li>
</ul>

<h3>Safety Considerations</h3>
<p>Proper overcurrent protection is critical for electrical safety. Overcurrent protective devices serve as the first line of defense against electrical fires and equipment damage due to faults or overloads. When properly applied, these devices disconnect the circuit before conductors reach temperatures that could ignite surrounding materials or damage insulation, preventing electrical fires and equipment failures.</p>
"""
    }

    # Check if the article already exists
    existing_article = NECArticle.query.filter_by(article_number=article_data["article_number"]).first()

    if existing_article:
        # Update existing article
        existing_article.title = article_data["title"]
        existing_article.summary = article_data["summary"]
        existing_article.content = article_data["content"]
        print(f"Updated Article {article_data['article_number']}: {article_data['title']}")
    else:
        # Create new article
        new_article = NECArticle(
            article_number=article_data["article_number"],
            title=article_data["title"],
            summary=article_data["summary"],
            content=article_data["content"]
        )
        db.session.add(new_article)
        print(f"Added Article {article_data['article_number']}: {article_data['title']}")

    # Commit the changes
    db.session.commit()
    
    return True

def main():
    """Create app context and run the update function."""
    try:
        app = create_app()
        with app.app_context():
            success = update_nec_article()
            if success:
                print(f"NEC article 240 update completed successfully.")
            else:
                print(f"NEC article 240 update failed.")
    except Exception as e:
        print(f"Error updating NEC article 240: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
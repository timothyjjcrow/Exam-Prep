import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 250 to the database."""
    # Article data
    article_data = {
        "article_number": "250",
        "title": "Grounding and Bonding",
        "summary": "Article 250 covers general requirements for grounding and bonding of electrical systems and equipment. It provides requirements for system grounding, equipment grounding, bonding, and grounding electrode systems, which are critical for electrical safety.",
        "content": "<h3>Purpose of Grounding and Bonding</h3><p>Article 250 is one of the most important articles in the NEC because it addresses grounding and bonding, which are fundamental to electrical safety. The primary purposes of grounding and bonding (250.4) are to:</p><ul><li>Limit voltage to ground (earth) during normal operation</li><li>Limit voltage to ground under fault conditions</li><li>Facilitate overcurrent device operation during ground faults</li><li>Limit lightning-induced voltages</li><li>Stabilize voltage during normal operation</li></ul><p>The article distinguishes between <strong>system grounding</strong> (connecting circuit conductors like the neutral to ground) and <strong>equipment grounding</strong> (connecting non-current-carrying metal parts to ground). This distinction is crucial because each serves different safety purposes.</p><h3>System Grounding Requirements</h3><p><strong>When to Ground (250.20):</strong> The NEC requires certain electrical systems to be grounded. For example, AC systems of less than 50V must be grounded if supplied by transformers whose primary supply exceeds 150V to ground. AC systems of 50-1000V must be grounded if:</p><ul><li>The system can be grounded so that the maximum voltage to ground doesn't exceed 150V</li><li>The system is 3-phase, 4-wire, wye-connected with the neutral used as a circuit conductor</li><li>The system is 3-phase, 4-wire, delta-connected with the midpoint of one phase used as a circuit conductor (high-leg delta)</li></ul><p><strong>Grounding Service-Supplied Systems (250.24):</strong> For a service, the grounded conductor (usually the neutral) must be connected to the grounding electrode system at the service equipment. This connection must be made with a grounding electrode conductor sized according to Table 250.66. The grounded conductor must also be routed with the ungrounded conductors to each service disconnecting means, where it is bonded to the enclosure.</p><p><strong>Main Bonding Jumper (250.28):</strong> At the service equipment, a main bonding jumper must connect the grounded conductor (neutral) to the equipment grounding conductor and the enclosure. This is typically a green screw, strap, or wire that connects the neutral bus to the metal enclosure of the service panel, creating an effective path for fault current.</p><h3>Equipment Grounding</h3><p><strong>Equipment Required to be Grounded (250.110):</strong> Generally, all exposed non-current-carrying metal parts of fixed equipment likely to be energized must be grounded. This includes equipment fastened in place, connected by permanent wiring methods, and in specific locations like wet areas, hazardous locations, or where in contact with grounded metal.</p><p><strong>Equipment Grounding Conductor (EGC) Types (250.118):</strong> The NEC recognizes various types of equipment grounding conductors:</p><ul><li>A copper or other corrosion-resistant conductor (insulated, covered, or bare)</li><li>Rigid metal conduit</li><li>Intermediate metal conduit</li><li>Electrical metallic tubing</li><li>Flexible metal conduit (with limitations)</li><li>Metal-clad cable (with limitations)</li></ul><p><strong>Sizing Equipment Grounding Conductors (250.122):</strong> EGCs must be sized based on the rating of the overcurrent device protecting the circuit. For example, for a 20A circuit, a minimum 12 AWG copper conductor is required. For larger circuits, Table 250.122 provides sizing requirements. If circuit conductors are increased in size for voltage drop, the EGC size must be increased proportionately.</p><h3>Grounding Electrode System</h3><p><strong>Grounding Electrode System Components (250.50):</strong> Buildings or structures must have a grounding electrode system consisting of all available electrodes:</p><ul><li>Metal underground water pipe (in contact with earth for 10 feet or more)</li><li>Metal frame of the building (effectively grounded)</li><li>Concrete-encased electrode (bare copper of at least 20 feet embedded in concrete foundation)</li><li>Ground ring (at least 20 feet of bare copper conductor, size 2 AWG or larger, encircling the building)</li><li>Rod, pipe, or plate electrodes</li></ul><p>These electrodes must be bonded together to form a single grounding electrode system.</p><p><strong>Ground Rods (250.52(A)(5) and 250.53):</strong> Ground rods must be at least 8 feet long and made of specified materials (copper-clad steel, stainless steel, or galvanized steel). They must be installed such that at least 8 feet contacts soil. If a single rod doesn't achieve 25 ohms to ground resistance, a second rod is required. Ground rods must be separated by at least 6 feet.</p><p><strong>Grounding Electrode Conductor Sizing (250.66):</strong> The grounding electrode conductor connects the grounded system conductor or equipment to the grounding electrode system. Its size depends on the size of the service-entrance conductors and is determined from Table 250.66.</p><h3>Bonding Requirements</h3><p><strong>Bonding of Services (250.92):</strong> At services, all metal enclosures containing service conductors must be bonded together and to the grounded conductor. Listed methods must be used for bonding around service equipment. Typical methods include bonding bushings, bonding jumpers, or ground wedges.</p><p><strong>Bonding of Piping Systems (250.104):</strong> Metal water piping and other metal piping systems that may become energized must be bonded to the service equipment enclosure, the grounded conductor, or the grounding electrode conductor.</p><p><strong>Bonding of Separately Derived Systems (250.30):</strong> For a separately derived system (like a transformer), the system bonding jumper must connect the grounded conductor to the equipment grounding conductor and the enclosure, and a grounding electrode conductor must connect the system to a grounding electrode.</p><h3>Special Provisions for Various Systems</h3><p><strong>Multiple Buildings or Structures (250.32):</strong> When there are multiple buildings or structures supplied by a feeder or branch circuit, an equipment grounding conductor must be run with the supply conductors to ground equipment in the separate building. The grounded conductor (neutral) must not be connected to ground at separate buildings except in specific circumstances.</p><p><strong>Grounding of Specific Systems (250.170-250.190):</strong> Article 250 includes specific provisions for grounding various systems, including instrument transformers, surge arresters, and high-impedance grounded neutral systems.</p><h3>Best Practices for Proper Grounding</h3><p><strong>Testing Ground Resistance:</strong> Although the NEC doesn't generally require testing except for certain installations, good practice is to test ground resistance to ensure it's within acceptable limits (preferably less than 25 ohms). This can be done with a ground resistance tester.</p><p><strong>Proper Connections:</strong> All ground and bond connections should be secure and use approved methods and materials. Exothermic welding (e.g., CADWELD) is often preferred for underground connections because it's permanent and resistant to corrosion.</p><p><strong>Accessibility:</strong> Grounding electrode connections should be accessible for inspection and testing. This helps ensure that the grounding system remains effective over time.</p><p>Understanding Article 250 is crucial for electricians, as improper grounding and bonding are leading causes of electrical hazards. A properly grounded and bonded electrical system provides essential protection against shock, fire, and equipment damage.</p>"
    }
    
    # Check if article exists
    existing_article = NECArticle.query.filter_by(
        article_number=article_data['article_number']
    ).first()
    
    if existing_article:
        # Update existing article
        existing_article.title = article_data['title']
        existing_article.summary = article_data['summary']
        existing_article.content = article_data['content']
        print(f"Updated Article {article_data['article_number']}: {article_data['title']}")
    else:
        # Create new article
        new_article = NECArticle(
            article_number=article_data['article_number'],
            title=article_data['title'],
            summary=article_data['summary'],
            content=article_data['content']
        )
        db.session.add(new_article)
        print(f"Added Article {article_data['article_number']}: {article_data['title']}")
    
    # Commit changes
    db.session.commit()
    
    return True

def main():
    """Create app context and run the update function."""
    try:
        app = create_app()
        with app.app_context():
            success = update_nec_article()
            if success:
                print(f"NEC article 250 update completed successfully.")
            else:
                print(f"NEC article 250 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 408 to the database."""
    # Article data
    article_data = {
        "article_number": "408",
        "title": "Switchboards, Switchgear, and Panelboards",
        "summary": "Article 408 covers the requirements for switchboards, switchgear, and panelboards, including their installation, grounding, clearances, and specific applications. It provides essential guidelines for the proper installation and protection of these critical distribution components.",
        "content": "<h3>Scope and General Requirements</h3><p>Article 408 covers switchboards, switchgear, and panelboards used for control of light, heat, or power circuits. These components are fundamental to electrical distribution systems in buildings, serving as central points for circuit routing, protection, and control. The article addresses installation requirements, clearances, grounding, overcurrent protection, and identification to ensure safe and compliant installations.</p><p><strong>Definitions and Distinctions (408.1):</strong></p><ul><li><strong>Switchboard:</strong> A large single panel, frame, or assembly of panels with switches, overcurrent protective devices, buses, and usually instruments, accessible from the front, rear, or both. Switchboards are generally not dead-front (meaning live parts may be exposed when the enclosure is open) and are floor-mounted.</li><li><strong>Switchgear:</strong> An assembly completely enclosed on all sides with sheet metal (except for ventilating openings and inspection windows) that contains primary power circuit switching or interrupting devices, buses, and control mechanisms. Modern switchgear is typically dead-front and includes features like arc resistance and compartmentalization.</li><li><strong>Panelboard:</strong> A single panel or group of panel units designed for assembly in the form of a single panel, including buses and automatic overcurrent devices, with or without switches, and typically installed in a cabinet accessible only from the front. Panelboards serve as distribution points for circuits in a building.</li></ul><h3>Installation Requirements</h3><p><strong>Location and Clearances (408.18):</strong> Switchboards and switchgear must be located away from moisture, easily ignitable materials, and areas where they might be damaged. Specific clearance requirements include:</p><ul><li>Working space in front of the equipment (typically 3 feet or more, depending on voltage)</li><li>Headroom of at least 6.5 feet</li><li>Illumination must be provided for working spaces around switchboards</li><li>Clear spaces must be kept clear and not used for storage</li></ul><p><strong>Wet Locations (408.16):</strong> In wet locations, switchboards and switchgear must be installed in weatherproof enclosures that meet the environmental conditions. Panelboards in wet locations must be installed so as to prevent moisture or water from entering and accumulating.</p><p><strong>Protection from Physical Damage (408.7):</strong> Switchboards, switchgear, and panelboards must be protected from physical damage. This often means locating them in dedicated electrical rooms, installing barriers, or other protective measures.</p><h3>Panelboard Requirements</h3><p><strong>Panelboard Overcurrent Protection (408.36):</strong> Each panelboard must be protected by an overcurrent protective device. The rating or setting of this device must not exceed that of the panelboard, with certain exceptions:</p><ul><li>For an individual panelboard with a single main device, the overcurrent device can be in the panel itself.</li><li>For a power panelboard with multiple disconnecting means, the maximum rating of the protection device is determined by the sum of the frame sizes of the disconnecting means.</li></ul><p><strong>Panelboard Circuit Identification (408.4):</strong> Every circuit and circuit modification must be legibly identified as to its clear, evident, and specific purpose or use. The identification must include sufficient detail to allow each circuit to be distinguished from all others. Circuit directories must be located on the face or inside of the panel door, and must not be made on removable or replaceable components.</p><p><strong>Clearance for Equipment Above Panelboards (110.26(F)):</strong> Where equipment requiring servicing is installed above a panelboard, there must be a minimum horizontal working space of 30 inches wide or the width of the equipment (whichever is greater). This prevents installations where equipment obstructs access to panelboards.</p><h3>Switchboard and Switchgear Requirements</h3><p><strong>Grounding Switchboards and Switchgear (408.20):</strong> Metal frames and structures supporting switching equipment must be grounded. This means connecting the metal enclosure to the equipment grounding system to prevent shock hazards in case of insulation failure.</p><p><strong>Busbars and Conductors (408.51):</strong> Busbars (the copper or aluminum bars within the equipment that distribute power) must be arranged to avoid strain on connections and must have sufficient capacity to carry the loads they serve. The arrangement should allow access for maintenance and future expansion.</p><p><strong>Switchboard Instruments (408.52):</strong> Where instruments like ammeters, voltmeters, and other measuring devices are installed on switchboards, they must be located so that the attendant is not in a position to make accidental contact with live parts while taking readings.</p><h3>Special Provisions</h3><p><strong>Unused Openings (408.7):</strong> Unused openings in cabinets, cutout boxes, and meter sockets must be effectively closed to provide protection equivalent to the wall of the equipment. This prevents accidental contact with live parts and keeps foreign objects out of the enclosure.</p><p><strong>Service Disconnecting Means (408.34):</strong> When a switchboard or panelboard serves as service equipment, the service disconnecting means must meet the requirements in Article 230.70. This includes being readily accessible, being suitable for the prevailing conditions, and having a way to determine visually when it is open (off).</p><p><strong>Workspace Lighting (110.26(D)):</strong> Illumination must be provided for all working spaces around switchboards, switchgear, and panelboards. This ensures that workers can safely perform testing, troubleshooting, and maintenance tasks, and can view equipment diagrams and directories.</p><h3>Special Applications</h3><p><strong>Emergency and Standby Power Systems (408.4(B)):</strong> For panelboards serving emergency or standby power systems, they must have permanent identification to alert people that the panelboard contains multiple power sources. Similar identification is required for normal and emergency or standby power sources.</p><p><strong>Service Entrance Equipment (408.36 Exception No. 1):</strong> When a panelboard is used as service equipment, specific rules apply regarding overcurrent protection. The main overcurrent device can be the sum of the frame sizes of the main circuit breakers if multiple devices serve as the main disconnecting means.</p><p><strong>High-Impedance Grounded Neutral Systems (408.3(F)):</strong> For high-impedance grounded neutral systems, the busbar connecting the grounded circuit conductors (often neutral) must be insulated from the equipment grounding conductors and from equipment enclosures. This is a specialized application often used in industrial settings.</p><h3>Common Code Issues and Best Practices</h3><p><strong>Common Code Violations:</strong></p><ul><li>Insufficient working clearances in front of electrical equipment</li><li>Missing or incomplete circuit directories</li><li>Improper wire bending space inside panelboards</li><li>Use of panel space as a raceway or junction box</li><li>Improperly sized panelboard protection</li></ul><p><strong>Best Practices:</strong></p><ul><li>Maintain detailed, updated circuit directories</li><li>Install panels in clean, dry, accessible locations</li><li>Provide spare capacity (typically 20% or more) for future expansion</li><li>Ensure proper labeling of emergency or standby power panels</li><li>Use separate electrical rooms for large installations with proper working space</li><li>Perform regular thermal scanning to detect overloaded circuits or loose connections</li></ul><p>Understanding Article 408 is essential for electricians, especially those involved in commercial and industrial work. Proper installation and maintenance of switchboards, switchgear, and panelboards ensures safe and reliable electrical distribution systems. These components form the backbone of a building's electrical system, making compliance with Article 408 a critical aspect of electrical work.</p>"
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
                print(f"NEC article 408 update completed successfully.")
            else:
                print(f"NEC article 408 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 312 to the database."""
    article_data = {
        "article_number": "312",
        "title": "Cabinets, Cutout Boxes, and Meter Socket Enclosures",
        "summary": "Requirements for the installation and construction of cabinets, cutout boxes, and meter socket enclosures that house electrical equipment and protect against accidental contact with live parts.",
        "content": """
<h3>Scope and Purpose</h3>
<p>Article 312 covers the installation and construction of cabinets, cutout boxes, and meter socket enclosures. These enclosures provide protection for electrical components and connections, while also protecting people from accidental contact with live parts. This article ensures that enclosures are properly installed, sized, and constructed to maintain safety and reliability.</p>

<h3>Key Definitions</h3>
<ul>
    <li><strong>Cabinet:</strong> An enclosure that is designed for either surface mounting or flush mounting and is provided with a frame, mat, or trim in which a swinging door or doors are or can be hung.</li>
    <li><strong>Cutout Box:</strong> An enclosure designed for surface mounting that has swinging doors or covers secured directly to and telescoping with the walls of the box proper.</li>
    <li><strong>Junction Box:</strong> An enclosure for joining or terminating circuit conductors, not incorporating a means of mounting utilization equipment (defined in Article 100, often referenced in Article 312).</li>
    <li><strong>Meter Socket Enclosure:</strong> An enclosure for housing a meter or meters, associated metering equipment, or a combination of both.</li>
</ul>

<h3>Installation Requirements (Part I)</h3>
<ul>
    <li><strong>312.2 Damp or Wet Locations:</strong> 
        <ul>
            <li>In damp or wet locations, enclosures must be placed or equipped to prevent moisture or water from entering and accumulating</li>
            <li>Enclosures in wet locations shall be weatherproof (marked with the designation "Type 3R" or higher)</li>
        </ul>
    </li>
    
    <li><strong>312.3 Position in Wall:</strong> 
        <ul>
            <li>Flush-mounted enclosures shall be installed so that the front edge will not be set back more than 6mm (¼ in.) from the finished surface</li>
            <li>Surface-mounted enclosures shall be installed so there is at least a 6mm (¼ in.) gap between the enclosure and the wall surface</li>
        </ul>
    </li>
    
    <li><strong>312.4 Repairing Noncombustible Surfaces:</strong> Noncombustible surfaces that are broken or incomplete around cabinets and cutout boxes shall be repaired to maintain the fire resistance rating of the surface.</li>
    
    <li><strong>312.5 Cabinets, Cutout Boxes, and Meter Socket Enclosures:</strong> 
        <ul>
            <li>Conductors entering enclosures shall be protected from abrasion</li>
            <li>Openings through which conductors enter shall be effectively closed</li>
            <li>Metal cabinets and cutout boxes must have approved metal bushings or fittings with shoulders</li>
            <li>Where nonmetallic sheathed cables enter, cable clamps or cable connectors must be used</li>
        </ul>
    </li>
    
    <li><strong>312.6 Deflection of Conductors:</strong> 
        <ul>
            <li>Conductors at terminals or conductors entering or leaving cabinets shall not be deflected more than 90 degrees</li>
            <li>Cabinets and cutout boxes shall have sufficient space to accommodate all conductors installed in them without crowding</li>
        </ul>
    </li>
    
    <li><strong>312.7 Space in Enclosures:</strong> Cabinets and cutout boxes shall have adequate space for all conductors installed in them without crowding. The space should accommodate splices and taps where made.</li>
    
    <li><strong>312.8 Enclosures for Switches or Overcurrent Devices:</strong> 
        <ul>
            <li>These enclosures shall not be used as junction boxes, auxiliary gutters, or raceways for conductors feeding through or tapping off to other switches or overcurrent devices, unless the enclosure provides adequate space</li>
            <li>The total cross-sectional area of all contained conductors shall not exceed 40 percent of the cross-sectional area of the space</li>
        </ul>
    </li>
    
    <li><strong>312.9 Side or Back Wiring Spaces or Gutters:</strong> Cabinets and cutout boxes shall have back-wiring spaces, gutters, or wiring compartments as required by 312.11(C) and (D).</li>
</ul>

<h3>Construction Requirements (Part II)</h3>
<ul>
    <li><strong>312.10 Material:</strong> 
        <ul>
            <li>Cabinets, cutout boxes, and meter socket enclosures shall comply with specific material requirements</li>
            <li>Metal must have specific thicknesses based on the largest dimension of the enclosure</li>
            <li>Nonmetallic enclosures shall be listed for the purpose</li>
            <li>Nonmetallic enclosures shall be suitable for the atmospheric conditions including sunlight, moisture, temperature, etc.</li>
        </ul>
    </li>
    
    <li><strong>312.11 Spacing:</strong> 
        <ul>
            <li>Distance between bare metal parts of different potential mounted on the same surface shall not be less than 12.7 mm (½ in.)</li>
            <li>Distance between bare metal parts and the enclosure walls shall not be less than 6.35 mm (¼ in.)</li>
            <li>Exception for listed components specifically designed for closer spacings</li>
        </ul>
    </li>
</ul>

<h3>Critical Applications and Common Issues</h3>
<ul>
    <li><strong>Bending Space for Conductors:</strong> One of the most common violations of Article 312 is insufficient bending space for conductors, especially with larger wire sizes. Adequate space must be provided to prevent damage to conductor insulation and maintain the minimum bending radius.</li>
    
    <li><strong>Overcrowded Enclosures:</strong> Placing too many conductors in an enclosure can lead to heat buildup, difficulty in maintenance, and potential damage to insulation. The 40 percent fill rule helps prevent this issue.</li>
    
    <li><strong>Improper Sealing:</strong> In wet or damp locations, improperly sealed enclosures can allow water ingress, which can cause corrosion, ground faults, or shock hazards.</li>
    
    <li><strong>Missing Bushings or Connectors:</strong> Failing to install proper bushings or connectors where conductors enter enclosures can result in insulation damage due to abrasion against sharp metal edges.</li>
    
    <li><strong>Using Improper Materials:</strong> Using enclosures made of materials not rated for the environment (such as indoor-rated enclosures in outdoor applications) can lead to premature failure and safety hazards.</li>
</ul>

<h3>Best Practices for Installation</h3>
<ul>
    <li><strong>Size Selection:</strong> Always select enclosures with adequate dimensions for the number and size of conductors to be installed, including any allowance for future expansion.</li>
    
    <li><strong>Environmental Consideration:</strong> Choose enclosures with appropriate NEMA or IP ratings for the installation environment (wet, damp, dusty, etc.).</li>
    
    <li><strong>Mounting Height:</strong> Install enclosures at heights that provide convenient access for operation and maintenance, while also meeting accessibility requirements for specific applications.</li>
    
    <li><strong>Proper Support:</strong> Ensure enclosures are securely mounted to structural elements, especially for heavier enclosures containing numerous devices or large conductors.</li>
    
    <li><strong>Wire Management:</strong> Organize conductors within the enclosure to facilitate easy identification, minimize crossover, and prevent unnecessary strain on connections.</li>
</ul>

<h3>Notable Code Updates in Recent Editions</h3>
<p>Recent editions of the NEC have included updates to Article 312, such as:</p>
<ul>
    <li>Clarification of requirements for wire bending space</li>
    <li>Refinement of rules regarding enclosure fill calculations</li>
    <li>Updated requirements for enclosures housing power monitoring equipment</li>
    <li>Enhanced specifications for enclosures in specific environments</li>
</ul>

<h3>Safety Considerations</h3>
<p>Properly installed and maintained enclosures play a critical role in electrical safety by:</p>
<ul>
    <li>Preventing accidental contact with live parts</li>
    <li>Containing potential arc flashes and electrical fires</li>
    <li>Protecting electrical components from environmental damage</li>
    <li>Facilitating safe access for maintenance and modification</li>
    <li>Maintaining the integrity of circuit protection schemes</li>
</ul>

<p>Article 312 requirements should be carefully followed to ensure that electrical enclosures provide the intended level of protection and safety while allowing for proper installation, maintenance, and operation of the enclosed electrical equipment.</p>
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
                print(f"NEC article 312 update completed successfully.")
            else:
                print(f"NEC article 312 update failed.")
    except Exception as e:
        print(f"Error updating NEC article 312: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
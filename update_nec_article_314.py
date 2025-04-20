import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 314 to the database."""
    # Article data
    article_data = {
        "article_number": "314",
        "title": "Outlet, Device, Pull, and Junction Boxes",
        "summary": "Article 314 covers the installation and use of all boxes and conduit bodies used as outlet, device, junction, or pull boxes. It provides requirements for box fill calculations, supports, covers, and sizing of boxes for various applications.",
        "content": "<h3>Scope and General Requirements</h3><p>Article 314 covers the installation and use of all boxes and conduit bodies that are used as outlet, device, junction, or pull boxes, depending on their application. These enclosures are fundamental components of electrical systems, providing protection, support, and access to wiring connections. The article addresses box selection, sizing, installation requirements, and fill calculations to ensure safe and accessible wiring connections.</p><p><strong>Types of Boxes (314.1):</strong> The article covers various types of boxes including:</p><ul><li>Outlet boxes: Used where devices, luminaires, or splices are installed</li><li>Device boxes: Where wiring devices such as switches and receptacles are installed</li><li>Junction boxes: Where conductors are joined or spliced</li><li>Pull boxes: Where conductors are pulled through with no splices</li><li>Conduit bodies: Providing access to conductors for pulling or splicing</li></ul><p><strong>Box Materials (314.3):</strong> Boxes must be constructed of materials appropriate for their environment and application. Common materials include:</p><ul><li>Metal boxes: Often steel or aluminum</li><li>Nonmetallic boxes: Usually PVC or fiberglass</li></ul><p>Metal boxes generally provide better structural support and heat dissipation, while nonmetallic boxes offer corrosion resistance and electrical isolation. The choice depends on the application and environment.</p><h3>Box Sizing and Fill Calculations</h3><p><strong>Minimum Box Size (314.16):</strong> Boxes must be large enough to provide adequate space for conductors, devices, and splice connectors. The NEC provides specific requirements for calculating minimum box volumes.</p><p><strong>Box Fill Calculations (314.16(B)):</strong> Each conductor entering a box must be counted according to its size (AWG) to determine the total required volume. The basic rules include:</p><ul><li>Each conductor that originates outside the box and terminates or is spliced within the box counts as one conductor.</li><li>Each conductor passing through the box without splice or termination counts as one conductor.</li><li>A conductor that both enters and exits the box, and is looped or coiled within the box, counts as two conductors.</li><li>Equipment grounding conductors as a group count as one conductor (the size of the largest EGC).</li><li>Each device (switch, receptacle) counts as two conductors.</li><li>Support fittings (e.g., cable clamps) within boxes count as one conductor.</li></ul><p><strong>Volume Requirements (Table 314.16(B)):</strong> The NEC provides a table that shows the required cubic inch volume per conductor based on conductor size. For example:</p><ul><li>14 AWG: 2.0 cubic inches per conductor</li><li>12 AWG: 2.25 cubic inches per conductor</li><li>10 AWG: 2.5 cubic inches per conductor</li><li>8 AWG: 3.0 cubic inches per conductor</li></ul><p><strong>Example Box Fill Calculation:</strong> For a box containing four 12 AWG circuit conductors, one 12 AWG equipment grounding conductor, one device, and internal cable clamps:</p><ul><li>Four 12 AWG conductors: 4 × 2.25 = 9.0 cubic inches</li><li>One equipment grounding conductor (12 AWG): 1 × 2.25 = 2.25 cubic inches</li><li>One device: 2 × 2.25 = 4.5 cubic inches</li><li>Internal cable clamps: 1 × 2.25 = 2.25 cubic inches</li><li>Total: 18.0 cubic inches</li></ul><p>Therefore, a box with a volume of at least 18.0 cubic inches would be required. From Table 314.16(A), a 4-inch square box with a depth of 1½ inches provides 21.0 cubic inches and would be adequate.</p><h3>Box Installation Requirements</h3><p><strong>Support of Boxes (314.23):</strong> Boxes must be securely fastened in place. Methods include:</p><ul><li>Direct mounting to structure (e.g., studs, joists) using screws or nails.</li><li>Support by rigid conduit or electrical metallic tubing (EMT), if the conduit is properly supported.</li><li>Special mounting brackets for suspended ceilings.</li></ul><p><strong>Box Depth (314.24):</strong> Boxes must be deep enough to allow for proper installation of devices and conductors without damaging the conductors or devices. For example, outlets installed in walls must not be set back more than ¼ inch from the finished surface, and in combustible walls, they must be flush with the finished surface.</p><p><strong>Conduit Entries (314.17):</strong> Where conduits or cables enter boxes, appropriate fittings must be used to protect conductors from abrasion. Metal boxes must be effectively grounded, and nonmetallic boxes must use fittings appropriate for the wiring method.</p><p><strong>Boxes in Wet Locations (314.15):</strong> In damp or wet locations, boxes and conduit bodies must be placed or equipped to prevent moisture from entering. Boxes in wet locations must be listed for use in wet locations.</p><h3>Covers and Access</h3><p><strong>Box Covers (314.25):</strong> All boxes must have covers appropriate for the application. Surface-mounted outlets must have covers that seat against the finished surface. Unused openings in boxes or fittings must be effectively closed to provide protection equivalent to that of the wall of the box or fitting.</p><p><strong>Access to Boxes (314.29):</strong> Junction, pull, and outlet boxes must be installed so that the wiring inside is accessible without removing part of the building or structure. This ensures that splices and connections can be inspected and maintained as needed.</p><p><strong>Junction or Pull Boxes and Conduit Bodies (314.28):</strong> For straight pulls, the length of the box must not be less than 8 times the trade diameter of the largest raceway. For angle or U-pulls, specific dimensional requirements apply to ensure adequate space for conductor bending and manipulation.</p><h3>Special Applications and Requirements</h3><p><strong>Floor Boxes (314.27(B)):</strong> Boxes used in floors must be specifically approved for that purpose and must maintain the fire rating of the floor assembly.</p><p><strong>Ceiling Outlet Boxes (314.27(A)):</strong> Boxes used to support lighting fixtures must be designed for that purpose and securely supported. For fixtures weighing more than 50 pounds, the box must be supported independently of the building structure.</p><p><strong>Boxes in Fire-Rated Assemblies (314.20 and 300.21):</strong> When boxes are installed in fire-rated walls or ceilings, they must be installed in a way that maintains the fire rating of the assembly. This may involve special fire-rated boxes or the use of fire-stop materials.</p><p><strong>Nonmetallic Boxes for Nonmetallic-Sheathed Cable (314.17(C)):</strong> When nonmetallic-sheathed cable is used with nonmetallic boxes, the cable must be secured to the box, and the box must be secured to the structure. Appropriate fittings or cable clamps must be used.</p><h3>Common Code Violations and Best Practices</h3><p><strong>Common Violations:</strong></p><ul><li>Overfilling boxes beyond their cubic inch capacity</li><li>Improper support of boxes, especially in suspended ceilings</li><li>Missing cable clamps or improper cable entry protection</li><li>Failure to use proper covers for the environment</li><li>Inadequate access to junction boxes</li></ul><p><strong>Best Practices:</strong></p><ul><li>Always perform a box fill calculation when there are many conductors</li><li>Use boxes that are larger than minimally required when possible</li><li>Maintain at least 6 inches of free conductor length at each box for connections</li><li>Ensure box edges are flush with the finished wall surface</li><li>Label junction boxes to identify circuit numbers (required in some jurisdictions)</li></ul><p>Article 314 is crucial for electricians because proper box selection, sizing, and installation are fundamental to a safe and code-compliant electrical installation. Violations related to boxes and enclosures are among the most common cited in electrical inspections, making a thorough understanding of this article essential for both novice and experienced electricians.</p>"
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
                print(f"NEC article 314 update completed successfully.")
            else:
                print(f"NEC article 314 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
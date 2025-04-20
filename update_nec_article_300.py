import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 300 to the database."""
    # Article data
    article_data = {
        "article_number": "300",
        "title": "Wiring Methods",
        "summary": "Article 300 contains general requirements for all wiring installations, including requirements for conductors, raceways, cables, and enclosures. It provides foundational rules that apply regardless of the specific wiring method used.",
        "content": "<h3>Overview of Wiring Methods</h3><p>Article 300 sets forth the general requirements for all wiring installations. It establishes the foundational rules for how electrical wiring is to be installed, regardless of the specific wiring method chosen. This article addresses conductors, cables, raceways, boxes, and enclosures – the basic building blocks of all electrical installations.</p><p>The article is organized to address:</p><ul><li>General requirements applicable to all installations</li><li>Requirements for conductors and their installation</li><li>Bending, securing, and supporting of conductors</li><li>Protection against physical damage</li><li>Installation requirements for enclosures and boxes</li></ul><p>Article 300 is essential to understand because its requirements apply regardless of whether you're using nonmetallic-sheathed cable (NM-B), armored cable (AC), metal conduit, or any other wiring method.</p><h3>Planning and Installation of Wiring</h3><p><strong>Wiring Planning (300.11):</strong> Wiring systems must be installed in a neat and workmanlike manner. Electrical equipment and wiring must not be supported by or attached to any other building element that is intended to be removed. For example, wiring cannot be supported by ceiling grids designed for removable ceiling panels.</p><p><strong>Mechanical Execution of Work (300.11(A) and 300.18):</strong> Electrical equipment, cables, and raceways must be securely fastened in place. Raceways must be installed as complete systems before the conductors are installed. This ensures the raceway provides proper support and protection for conductors.</p><p><strong>Circuits (300.3(B)):</strong> All conductors of the same circuit, including the neutral and equipment grounding conductor, must be contained in the same raceway, cable, or trench. This requirement helps minimize electromagnetic induction, which could lead to heating or reduction in equipment performance. For multiconductor cables, the same rule applies – a complete circuit must be contained within the same cable.</p><h3>Protection of Conductors and Cables</h3><p><strong>Protection Against Physical Damage (300.4):</strong> Where conductors or cables are subject to physical damage, they must be protected. For instance:</p><ul><li>When cables are run through bored holes in wood framing, the edge of the hole must be at least 1¼ inches from the nearest edge of the wood member. If this distance can't be maintained, a steel plate at least 1/16 inch thick must be installed to protect the cable.</li><li>In metal framing members, bushings, grommets, or other approved means must protect cables from abrasion.</li><li>Where cables emerge from the floor, they must be protected by rigid metal conduit, IMC, Schedule 80 PVC, or equivalent to a height of at least 6 feet.</li></ul><p><strong>Protection in Concealed Locations (300.4(D)):</strong> Cables run parallel to framing members or furring strips must be protected where they would be subject to penetration by screws or nails. This typically means keeping the cable at least 1¼ inches from the edge of the framing member, or protecting it with a 1/16 inch steel plate.</p><p><strong>Installation in Shallow Grooves (300.4(E)):</strong> Cables installed in shallow grooves in masonry, concrete, or adobe must be protected by a channel at least 1¼ inches deep and covered with wallboard or equivalent.</p><h3>Conductor Installation and Routing</h3><p><strong>Conductor Identification (300.5(D)(3)):</strong> Direct-buried cables or conductors must have their location identified by a warning ribbon placed in the trench at least 12 inches above the underground installation.</p><p><strong>Underground Installations (300.5):</strong> Direct-buried cables or conductors must be installed at specific depths depending on location and voltage. For example, residential branch circuits rated 120V or less with GFCI protection require only 12 inches of cover, while the same circuits without GFCI protection require 18 inches. Commercial parking lots typically require 24 inches of cover.</p><p><strong>Raceway Seals (300.5(G) and 300.7):</strong> Conduits or raceways entering from the exterior must be sealed to prevent moisture from entering the building. Similarly, raceways between warm and cold areas must be sealed to prevent condensation due to temperature differences, which could accumulate and damage equipment or wiring.</p><h3>Boxes and Enclosures</h3><p><strong>Boxes Required (300.15):</strong> An approved box or conduit body must be installed at each conductor splice, outlet, switch, junction, or termination point. This ensures connections are accessible and contained in a fire-resistant enclosure designed to prevent accidental contact with live parts.</p><p><strong>Installation and Support of Boxes (300.11):</strong> Boxes must be securely fastened in place unless otherwise permitted by specific exceptions. They cannot be supported by the cables entering them (except for certain listed cables and boxes specifically designed for this purpose). In suspended ceiling spaces, boxes must be supported independently of the ceiling grid.</p><p><strong>Openings in Boxes and Enclosures (300.14):</strong> Sufficient length of free conductor – at least 6 inches – must be left at each outlet, junction, and switch point for splices or connections to fixtures or devices. This ensures that connections can be made safely and provides for future replacement or service.</p><h3>Special Installations</h3><p><strong>Raceway Installations Through Framing Members (300.4(B)):</strong> If a raceway is installed through a framing member and will be subject to physical damage during or after construction, it must be protected by a steel plate, tube, or equivalent at least 1/16 inch thick.</p><p><strong>Expansion Joints (300.7(B)):</strong> When raceways cross structural expansion joints, or where movement is expected, a fitting or other approved means must be installed to compensate for the movement. This prevents stress on the raceway and potential damage to conductors.</p><p><strong>Spread of Fire or Products of Combustion (300.21):</strong> Electrical installations in hollow spaces, vertical shafts, and ventilation ducts must be made so that the fire-resistive rating of the structure is not reduced. This may require approved firestop systems where wiring penetrates fire-rated walls, floors, or ceilings.</p><h3>Conductor Bending and Ampacity</h3><p><strong>Bending Radius (300.34):</strong> Conductors must not be bent to a radius less than the minimum allowed by their construction. For most conductors, this is 5 times the diameter for conductors without metallic shielding, and 12 times the diameter for lead-covered conductors.</p><p><strong>Conductor Ampacity Adjustment (B.310.15(B)(3)):</strong> When multiple current-carrying conductors are installed in the same raceway or cable, their ampacity must be adjusted (reduced) based on the total number. This adjustment accounts for the reduced heat dissipation when conductors are bundled together.</p><p>By providing these general requirements, Article 300 ensures that regardless of the specific wiring method chosen for an installation, the basic principles of safety, accessibility, and longevity are maintained. These requirements serve as the foundation upon which the specific rules for individual wiring methods are built.</p>"
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
                print(f"NEC article 300 update completed successfully.")
            else:
                print(f"NEC article 300 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
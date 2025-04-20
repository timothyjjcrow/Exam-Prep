import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 210 to the database."""
    # Article data
    article_data = {
        "article_number": "210",
        "title": "Branch Circuits",
        "summary": "Article 210 provides the requirements for branch circuits, including provisions for conductor sizing, overcurrent protection, required outlets, and receptacle configurations for various occupancies and locations.",
        "content": """<h3>Scope and Purpose</h3><p>Article 210 covers branch circuits, which are the circuits that extend beyond the final overcurrent protective device (typically a circuit breaker or fuse) and supply outlets for utilization equipment. This article establishes requirements for:</p><ul><li>Branch circuit ratings and minimum loads</li><li>Required outlets for specific areas and occupancies</li><li>Locations where specific types of receptacles are required</li><li>Ground-fault circuit-interrupter (GFCI) and arc-fault circuit-interrupter (AFCI) protection</li><li>Branch circuit extensions and modifications</li></ul><p>The provisions in Article 210 help ensure that branch circuits can safely supply the intended loads and that outlets are provided where needed for convenience and safety.</p><h3>Branch Circuit Classifications</h3><p><strong>Individual Branch Circuit (210.8):</strong> A branch circuit that supplies only one utilization equipment.</p><p><strong>Multioutlet Branch Circuit (210.23):</strong> A branch circuit that supplies two or more outlets or receptacles.</p><p><strong>General Purpose Branch Circuit (210.23(A)):</strong> A branch circuit that supplies two or more receptacles or outlets for lighting and appliances.</p><p><strong>Appliance Branch Circuit (210.23(B)):</strong> A branch circuit that supplies a specific appliance, or appliances in a single room.</p><p><strong>Branch Circuit Ratings (210.3):</strong> Branch circuits are rated according to the rating of the overcurrent device protecting the circuit. Common ratings include 15, 20, 30, 40, and 50 amperes.</p><h3>Required Branch Circuits</h3><p><strong>Small Appliance Branch Circuits (210.11(C)(1)):</strong> In dwelling units, at least two 20-ampere small-appliance branch circuits must be provided for receptacles in kitchen, pantry, breakfast room, dining room, or similar areas. These circuits cannot supply other outlets, such as lighting.</p><p><strong>Laundry Branch Circuit (210.11(C)(2)):</strong> In dwelling units, at least one 20-ampere branch circuit must be provided for receptacles in the laundry area.</p><p><strong>Bathroom Branch Circuit (210.11(C)(3)):</strong> In dwelling units, at least one 20-ampere branch circuit must be provided for receptacles in bathrooms. This circuit can only supply bathroom receptacles, or it can supply a single bathroom entirely (both receptacles and lighting).</p><p><strong>Garage Branch Circuit (210.52(G)(1)):</strong> In dwelling units with attached garages or detached garages with electric power, at least one receptacle outlet must be installed for each car space.</p><h3>Required Receptacle Outlets</h3><p><strong>Dwelling Units (210.52):</strong> Receptacle outlets in dwelling units must be installed so that no point along the floor line in any wall space is more than 6 feet from a receptacle outlet. Additional specific requirements include:</p><ul><li><strong>Kitchen Countertop (210.52(C)):</strong> Receptacle outlets must be installed so that no point along the wall line is more than 24 inches from a receptacle, and at each countertop space wider than 12 inches.</li><li><strong>Bathrooms (210.52(D)):</strong> At least one receptacle outlet must be installed within 3 feet of the outside edge of each bathroom sink.</li><li><strong>Outdoor Outlets (210.52(E)):</strong> At least one receptacle outlet must be installed at the front and back of the dwelling, not more than 6½ feet above grade.</li><li><strong>Hallways (210.52(H)):</strong> In hallways 10 feet or longer, at least one receptacle outlet must be installed.</li></ul><p><strong>Non-Dwelling Occupancies (210.62-210.63):</strong> Various receptacle requirements exist for other occupancies, including:</p><ul><li>Show windows</li><li>Meeting rooms</li><li>Corridors</li><li>HVAC equipment (requires a receptacle within 25 feet)</li></ul><h3>Ground-Fault Circuit-Interrupter (GFCI) Protection</h3><p><strong>Dwelling Units (210.8(A)):</strong> GFCI protection is required for all 125-volt, single-phase, 15- and 20-ampere receptacles installed in the following locations:</p><ul><li>Bathrooms</li><li>Kitchens (receptacles that serve countertop surfaces)</li><li>Garages and accessory buildings</li><li>Outdoor areas</li><li>Basements (unfinished portions)</li><li>Laundry areas</li><li>Boathouses</li><li>Kitchen dishwasher branch circuit</li><li>Crawl spaces</li><li>Unfinished portions or areas of the basement</li></ul><p><strong>Other Than Dwelling Units (210.8(B)):</strong> GFCI protection is required for all 125-volt, single-phase, 15- and 20-ampere receptacles installed in the following locations:</p><ul><li>Bathrooms</li><li>Kitchens</li><li>Rooftops</li><li>Outdoor areas</li><li>Indoor wet locations</li><li>Locker rooms with associated showering facilities</li><li>Garages, service bays, and similar areas</li><li>Crawl spaces</li><li>Unfinished portions or areas of basements</li></ul><p>GFCI protection is designed to prevent serious shock hazards by quickly interrupting the circuit when a ground fault is detected.</p><h3>Arc-Fault Circuit-Interrupter (AFCI) Protection</h3><p><strong>Dwelling Units (210.12(A)):</strong> AFCI protection is required for 120-volt, single-phase, 15- and 20-ampere branch circuits supplying outlets or devices in the following locations:</p><ul><li>Kitchens</li><li>Family rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas, or similar rooms or areas</li><li>Dormitory units</li></ul><p>AFCI protection is designed to detect and interrupt dangerous arc faults that could lead to electrical fires.</p><h3>Permissible Loads and Branch Circuit Extensions</h3><p><strong>Continuous and Noncontinuous Loads (210.19(A)):</strong> Branch circuit conductors must have an ampacity not less than the noncontinuous load plus 125 percent of the continuous load.</p><p><strong>Multioutlet Branch Circuits (210.23):</strong> The total cord-and-plug-connected load on a general-purpose branch circuit must not exceed 80 percent of the branch-circuit rating where the load operates continuously for 3 hours or more.</p><p><strong>Branch Circuit Extensions (210.7):</strong> When extending existing branch circuits, the extension must comply with current requirements for new installations, including GFCI and AFCI protection where required.</p><h3>Outlet Device Ratings</h3><p><strong>Receptacle Ratings (210.21(B)):</strong> A single receptacle installed on an individual branch circuit must have an ampere rating not less than that of the branch circuit. Where connected to a branch circuit supplying two or more receptacles or outlets, a receptacle's amperage rating should align with specific requirements in Table 210.21(B)(3), which typically specifies:</p><ul><li>15-ampere receptacles may be used on 15-ampere or 20-ampere circuits</li><li>20-ampere receptacles may be used on 20-ampere circuits</li></ul><p><strong>Lampholders (210.21(A)):</strong> Lampholders connected to circuits with an ampere rating over 20 amperes shall be of the heavy-duty type, with a minimum rating of 660 watts.</p><h3>Voltage Limitations</h3><p><strong>General (210.6(A)):</strong> Branch circuits shall not exceed 120 volts between conductors serving:</p><ul><li>Lampholders with a screw-type shell</li><li>Receptacles rated 15 or 20 amperes in dwelling units</li><li>Luminaires with mogul-base screw-shell lampholders (except certain supervised installations)</li></ul><p><strong>Higher Voltages (210.6(B-E)):</strong> Permits branch circuits up to 277 volts to ground for specific applications like listed electric-discharge lighting or infrared heating, and up to 600 volts for specific utilization equipment in industrial or commercial settings.</p><h3>Common Code Issues and Violations</h3><p><strong>Inadequate Circuit Capacity:</strong> Branch circuits sometimes lack sufficient capacity for the connected load, leading to breaker trips or overheating.</p><p><strong>Missing GFCI Protection:</strong> Failure to provide GFCI protection in required locations is a common violation, particularly in older buildings being renovated.</p><p><strong>Improper Small Appliance Circuit Use:</strong> Using the required kitchen small appliance circuits for non-kitchen receptacles or for lighting fixtures.</p><p><strong>Inadequate Receptacle Spacing:</strong> In dwelling units, failing to provide receptacles at the required spacing along walls (no point more than 6 feet from a receptacle).</p><p><strong>Missing AFCI Protection:</strong> Older homes being renovated often lack AFCI protection for circuits where it is now required.</p><h3>Recent Code Changes</h3><p>Recent editions of the NEC have expanded requirements for both GFCI and AFCI protection, recognizing the safety benefits of these technologies. For example:</p><ul><li>GFCI protection has been expanded to more locations in recent code editions</li><li>AFCI protection has been expanded beyond bedrooms to most habitable rooms in dwelling units</li><li>Requirements for receptacle spacing and placement have become more specific</li></ul><p>Article 210 is one of the most frequently applied articles in the NEC, as it governs the branch circuits that supply power to utilization equipment throughout buildings. Understanding these requirements is essential for electrical safety, convenience of use, and code compliance in both residential and commercial installations.</p>"""
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
                print(f"NEC article 210 update completed successfully.")
            else:
                print(f"NEC article 210 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
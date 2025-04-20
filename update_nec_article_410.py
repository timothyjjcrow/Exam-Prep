import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 410 to the database."""
    article_data = {
        "article_number": "410",
        "title": "Luminaires, Lampholders, and Lamps",
        "summary": "Requirements for the installation, support, and wiring of luminaires (fixtures), lampholders, lamps, decorative lighting, and accessories for lighting installations in all occupancies.",
        "content": """
<h3>Scope and Purpose</h3>
<p>Article 410 covers the installation, support, and wiring of luminaires (lighting fixtures), lampholders, lamps, decorative lighting, and similar equipment for interior and exterior lighting applications. This article provides requirements to ensure safe and proper installation of lighting equipment to prevent electrical hazards, overheating, and fire risks.</p>

<h3>General Requirements</h3>
<p><strong>410.10 Luminaires in Specific Locations:</strong> Special installation requirements are provided for luminaires in combustible material, closets, bathrooms, and other locations with specific hazards:</p>
<ul>
    <li><strong>Bathtub and Shower Areas:</strong> Luminaires located within the actual outside dimension of bathtubs and shower stalls (zone measured 3 ft horizontally and 8 ft vertically from the top of the bathtub rim or shower threshold) must be marked suitable for damp or wet locations, and where subject to shower spray, must be marked suitable for wet locations.</li>
    <li><strong>Closet Storage Space:</strong> Specific clearances are required between luminaires and storage areas in clothes closets. Incandescent or LED luminaires with exposed lamps shall have minimum 12-inch clearance from storage, while totally enclosed incandescent, LED, or fluorescent luminaires require minimum 6-inch clearance.</li>
    <li><strong>Luminaires Near Combustible Material:</strong> Luminaires must be installed so that combustible materials are not subjected to temperatures in excess of 90°C (194°F).</li>
</ul>

<p><strong>410.16 Luminaires in Clothes Closets:</strong> Detailed requirements for the types of luminaires permitted in clothes closets and their required placement:</p>
<ul>
    <li>Only surface-mounted or recessed incandescent or LED luminaires with completely enclosed light sources, surface-mounted or recessed fluorescent luminaires, and surface-mounted fluorescent or LED luminaires identified as suitable for installation within the closet storage space are permitted.</li>
    <li>Pendant luminaires or lamp-holders are not permitted in clothes closets.</li>
    <li>Incandescent luminaires with open or partially enclosed lamps and pendant luminaires or lampholders are not permitted.</li>
</ul>

<p><strong>410.30 Support of Luminaires:</strong> Requirements for how luminaires must be supported:</p>
<ul>
    <li>Luminaires must be securely supported, with the dead weight of fixtures exceeding 50 lbs supported independently of the outlet box unless the box is listed for that weight.</li>
    <li>Framing members of suspended ceiling systems used to support luminaires must be securely fastened to each other and to the building structure.</li>
    <li>Luminaires must be supported by structural supports such as ceiling framing members or must be equipped with strain relief connections where mounted on outlet boxes.</li>
</ul>

<h3>Wiring and Construction of Luminaires</h3>
<p><strong>410.48 Wiring Methods:</strong> Conductors that operate at over 30 volts must be installed using approved wiring methods from Chapter 3. Flexible cord use is limited to specific applications:</p>
<ul>
    <li>Connection of pendants, portable luminaires, electric-discharge luminaires, or other fixtures that require flexibility during use or servicing.</li>
    <li>Cords must be visible for their entire length, not subject to strain, and protected from physical damage.</li>
</ul>

<p><strong>410.115 Temperature Limits:</strong> Luminaires must be constructed so that adjacent combustible material is not subjected to temperatures above 90°C (194°F). Recessed luminaires must be marked with maximum lamp wattage ratings to prevent overheating.</p>

<p><strong>410.65 through 410.72 Feeder and Branch Circuits for Lighting:</strong> Requirements for how circuits must be arranged and protected:</p>
<ul>
    <li>Branch circuits for luminaires must not exceed the rating for which the luminaire is designed.</li>
    <li>Multi-outlet branch circuits supplying luminaires must operate at not more than 20 amperes where supplying luminaires with lampholders of other than the screw-shell type.</li>
    <li>Electric-discharge luminaires with ballasts may be supplied by branch circuits of up to 40 amperes.</li>
</ul>

<h3>Special Provisions for Specific Luminaire Types</h3>
<p><strong>410.130 through 410.136 Electric-Discharge Lighting:</strong> Requirements for fluorescent, HID, and other discharge lighting:</p>
<ul>
    <li>Luminaires using double-ended lamps (such as fluorescent tubes) and containing ballasts must have automatic disconnecting means for servicing purposes.</li>
    <li>High-intensity discharge fixtures must have thermal protection to prevent overheating.</li>
    <li>Direct-current equipment used with electric-discharge lighting must be equipped with suitable protection against overcurrent.</li>
</ul>

<p><strong>410.140 through 410.144 LED Lighting:</strong> Requirements specific to LED luminaires:</p>
<ul>
    <li>LED luminaires must be listed unless they are assembled from listed parts, such as LED light engines.</li>
    <li>Retrofit kits used to convert existing luminaires to LED must be listed and installed according to manufacturer's instructions.</li>
    <li>LED drivers must be compatible with the luminaires they supply and must meet the requirements for Class 2 power sources when operating in that mode.</li>
</ul>

<p><strong>410.151 through 410.160 Track Lighting:</strong> Requirements for track lighting systems:</p>
<ul>
    <li>Track lighting must be permanently installed and operate at not more than 120 volts between conductors unless using listed track of higher voltage rating.</li>
    <li>Track must be securely mounted and rated for its physical loading, with maximum weight limits for fixtures.</li>
    <li>Fittings must be designed to prevent their insertion into energized track sections not intended for them.</li>
    <li>Branch circuit load calculations for track lighting must account for the maximum ampere rating of the track rather than just the currently installed fixtures.</li>
</ul>

<h3>Common Installation Issues</h3>
<ul>
    <li><strong>Improper Support:</strong> Not adequately supporting heavy fixtures independent of outlet boxes, or not securing suspended ceiling grid systems properly to building structure.</li>
    <li><strong>Closet Installations:</strong> Failing to maintain required clearances from storage areas in closets, or installing prohibited fixture types in closets.</li>
    <li><strong>Recessed Fixtures:</strong> Using higher wattage lamps than the fixture is rated for, or failing to maintain proper clearance from insulation (IC vs. non-IC rated fixtures).</li>
    <li><strong>Wet Locations:</strong> Installing fixtures not rated for wet locations in areas subject to water or moisture.</li>
    <li><strong>Circuit Loading:</strong> Overloading branch circuits by installing too many fixtures on a single circuit.</li>
    <li><strong>Thermal Insulation Contact:</strong> Installing recessed fixtures without proper clearance from insulation when not rated for such contact.</li>
</ul>

<h3>Recent Code Changes</h3>
<p>Recent updates to Article 410 have included:</p>
<ul>
    <li>Expanded requirements for LED luminaires and retrofit kits</li>
    <li>Updated requirements for luminaire installation in closets</li>
    <li>Enhanced provisions for disconnecting means for fluorescent and other double-ended lamp fixtures</li>
    <li>Revised requirements for luminaires in bathtub and shower areas</li>
    <li>Updated load calculation methods for track lighting</li>
</ul>

<p>Article 410 continues to evolve as lighting technology changes, with particular attention to LED technology, energy efficiency, and safety features that prevent overheating and electrical hazards. Proper application of these requirements ensures that lighting installations provide safe, reliable illumination for all types of occupancies.</p>
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
                print(f"NEC article 410 update completed successfully.")
            else:
                print(f"NEC article 410 update failed.")
    except Exception as e:
        print(f"Error updating NEC article 410: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
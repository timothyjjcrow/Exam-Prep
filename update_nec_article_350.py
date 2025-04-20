import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 350 to the database."""
    article_data = {
        "article_number": "350",
        "title": "Liquidtight Flexible Metal Conduit: Type LFMC",
        "summary": "Requirements for the installation and use of Liquidtight Flexible Metal Conduit (LFMC), which provides flexible, liquid-tight protection for electrical conductors in wet or damp locations and where flexibility is needed.",
        "content": """
<h3>Scope and Purpose</h3>
<p>Article 350 covers the use, installation, and construction specifications for Liquidtight Flexible Metal Conduit (LFMC). This wiring method consists of a flexible metal core with a liquidtight, nonmetallic, sunlight-resistant outer jacket. LFMC combines the flexibility of flexible metal conduit with the added protection against liquids, making it suitable for wet locations and applications requiring protection from oils, coolants, and other liquids.</p>

<h3>Conduit Characteristics</h3>
<p><strong>350.100 Construction:</strong> LFMC consists of a flexible metal core (similar to FMC) with a liquidtight, nonmetallic, sunlight-resistant outer jacket. The smooth or corrugated metallic core is made of a metal such as steel or aluminum, and the outer jacket is typically made of PVC or another suitable polymer. LFMC is available in trade sizes from metric designator 16 (trade size 1/2) through metric designator 103 (trade size 4).</p>

<p><strong>350.120 Marking:</strong> LFMC shall be marked according to 110.21. The marking shall include:</p>
<ul>
    <li>Manufacturer's name or trademark</li>
    <li>The trade size</li>
    <li>The designation "LFMC" or other marking to indicate liquid-tight properties</li>
</ul>

<h3>Uses Permitted</h3>
<p><strong>350.10 Uses Permitted:</strong> LFMC can be used in both exposed and concealed locations in the following cases:</p>
<ul>
    <li>Where flexibility is required for installation, operation, or maintenance</li>
    <li>In wet locations</li>
    <li>In direct burial where listed and marked for the purpose</li>
    <li>For direct exposure to sunlight where listed and marked for the purpose</li>
    <li>Where exposed to mineral oils, gasoline, or other materials having a deteriorating effect on some thermoplastics (if the conduit is listed for the specific conditions)</li>
    <li>For outdoor locations when listed and marked for the purpose</li>
    <li>For connection of motors and equipment where flexibility is needed</li>
    <li>In hazardous (classified) locations where specifically permitted by Chapter 5</li>
</ul>

<h3>Uses Not Permitted</h3>
<p><strong>350.12 Uses Not Permitted:</strong> LFMC shall not be used in the following:</p>
<ul>
    <li>Where subject to physical damage</li>
    <li>Where operating conditions are such that the overall temperature will exceed that for which the LFMC is approved</li>
    <li>In lengths longer than 6 feet (1.8 m), except where specifically permitted elsewhere in the Code</li>
    <li>Where voltage exceeds 600 volts, nominal, unless permitted elsewhere in the Code</li>
    <li>In any hazardous (classified) location except as permitted by other articles in the Code</li>
</ul>

<h3>Installation Requirements</h3>
<p><strong>350.20 Size:</strong> LFMC shall not be used in trade sizes less than metric designator 16 (trade size 1/2). The minimum size allowed depends on the number and size of conductors to be installed.</p>

<p><strong>350.22 Number of Conductors:</strong> The number of conductors permitted in LFMC must not exceed the percentage fill specified in Table 1, Chapter 9. Calculations must be based on the dimensions provided in the tables or supplied by the manufacturer.</p>

<p><strong>350.24 Bends - How Made:</strong> Bends in LFMC shall be made so that the conduit is not damaged and the internal diameter of the conduit is not effectively reduced. The radius of the curve of the inner edge of any bend shall not be less than shown in Table 2, Chapter 9.</p>

<p><strong>350.26 Bends - Number in One Run:</strong> There shall not be more than the equivalent of four quarter bends (360 degrees total) between pull points, for example, conduit bodies and boxes.</p>

<p><strong>350.30 Securing and Supporting:</strong> LFMC shall be securely fastened in place and supported in accordance with the following:</p>
<ul>
    <li>LFMC shall be securely fastened in place by an approved means within 12 inches (300 mm) of each box, cabinet, conduit body, or other conduit termination</li>
    <li>LFMC shall be supported at intervals not exceeding 4.5 feet (1.4 m)</li>
    <li>Horizontal runs of LFMC supported by openings through framing members at intervals not greater than 4.5 feet (1.4 m) and securely fastened within 12 inches (300 mm) of termination points shall be permitted</li>
    <li>Securing or supporting is not required where flexibility is necessary after installation</li>
    <li>Securing or supporting is not required for lengths not exceeding 3 feet (900 mm) at terminals where flexibility is necessary</li>
</ul>

<p><strong>350.42 Couplings and Connectors:</strong> Angle connectors shall not be used for concealed raceway installations. Couplings and connectors used with LFMC shall be of a type that effectively maintains the liquidtight characteristic of the raceway system.</p>

<p><strong>350.60 Grounding and Bonding:</strong> If flexibility is needed after installation, an equipment grounding conductor shall be installed. When not required for flexibility, LFMC can be used as an equipment grounding conductor when both the LFMC and fittings are listed for grounding.</p>

<h3>Common Installation Issues</h3>
<ul>
    <li><strong>Sealing:</strong> Not properly sealing LFMC connections, allowing water ingress and compromising the liquidtight integrity</li>
    <li><strong>Excessive Length:</strong> Using LFMC in runs longer than permitted (typically 6 feet, except where specifically permitted)</li>
    <li><strong>Temperature Concerns:</strong> Installing LFMC in environments that exceed its temperature rating</li>
    <li><strong>Inadequate Support:</strong> Not supporting LFMC at the required intervals</li>
    <li><strong>Improper Grounding:</strong> Failing to provide proper equipment grounding when LFMC is used for flexibility</li>
</ul>

<h3>Advantages of LFMC</h3>
<ul>
    <li><strong>Flexibility:</strong> Allows for easy installation around obstacles and in tight spaces</li>
    <li><strong>Liquidtight Protection:</strong> Provides a watertight seal against moisture and liquids</li>
    <li><strong>Vibration Isolation:</strong> Can absorb vibration from equipment, preventing transmission to the building structure</li>
    <li><strong>Chemical Resistance:</strong> Many types offer resistance to oils, chemicals, and corrosive environments</li>
    <li><strong>UV Resistance:</strong> When properly marked, can withstand direct sunlight exposure</li>
    <li><strong>Physical Protection:</strong> Provides mechanical protection for enclosed conductors</li>
</ul>

<h3>Common Applications</h3>
<p>LFMC is commonly used in:</p>
<ul>
    <li>Outdoor installations where exposure to precipitation is expected</li>
    <li>Connections to motors and other equipment in wet or damp locations</li>
    <li>Industrial environments where exposure to oils, coolants, or chemicals is possible</li>
    <li>Food processing facilities where regular washdown is required</li>
    <li>HVAC equipment installations, especially for outdoor units</li>
    <li>Manufacturing facilities with vibrating machinery</li>
    <li>Locations requiring both flexibility and protection from liquids</li>
</ul>

<h3>Recent Code Changes</h3>
<p>Recent updates to Article 350 have included:</p>
<ul>
    <li>Clarification of requirements for LFMC as an equipment grounding conductor</li>
    <li>Updates to support and securing requirements</li>
    <li>Expansion of permitted uses in specific applications</li>
    <li>Enhanced requirements for listings and markings</li>
</ul>

<p>When properly installed according to Article 350, Liquidtight Flexible Metal Conduit provides an effective wiring method that combines flexibility, mechanical protection, and resistance to liquids, making it ideal for many challenging installation environments.</p>
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
                print(f"NEC article 350 update completed successfully.")
            else:
                print(f"NEC article 350 update failed.")
    except Exception as e:
        print(f"Error updating NEC article 350: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
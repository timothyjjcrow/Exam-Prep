import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 348 to the database."""
    article_data = {
        "article_number": "348",
        "title": "Flexible Metal Conduit: Type FMC",
        "summary": "Requirements for the installation and use of Flexible Metal Conduit (FMC) and associated fittings, allowing for flexibility in routing while providing protection for enclosed conductors.",
        "content": """
<h3>Scope and Purpose</h3>
<p>Article 348 covers the use, installation, and construction specifications for Flexible Metal Conduit (FMC). This wiring method consists of a raceway of circular cross section made of helically wound, formed, interlocked metal strip. FMC provides a degree of flexibility not available with rigid conduit types, allowing for movement, vibration isolation, and easier installation in locations with bends and offsets.</p>

<h3>Conduit Characteristics</h3>
<p><strong>348.100 Construction:</strong> FMC is constructed of helically wound metal strip, typically steel or aluminum. The interlocked design creates a flexible yet durable raceway that can bend without collapsing or reducing its internal diameter significantly. Available in trade sizes from metric designator 16 (trade size 1/2) through metric designator 103 (trade size 4).</p>

<p><strong>348.120 Marking:</strong> FMC shall be marked according to 110.21. The marking shall include:</p>
<ul>
    <li>Manufacturer's name or trademark</li>
    <li>The trade size</li>
    <li>Type designation, if applicable</li>
</ul>

<h3>Uses Permitted</h3>
<p><strong>348.10 Uses Permitted:</strong> FMC can be used in both exposed and concealed locations in the following cases:</p>
<ul>
    <li>Where flexibility is required for installation, operation, or maintenance</li>
    <li>Where protection from liquids, vapors, or solids is not required</li>
    <li>For direct embedding in poured concrete or aggregate where listed for this purpose</li>
    <li>In dry locations</li>
    <li>In hoistways, where permitted by Article 620</li>
    <li>For connection of motors and other equipment where flexibility is needed</li>
    <li>In hazardous (classified) locations where specifically permitted by Chapter 5</li>
</ul>

<h3>Uses Not Permitted</h3>
<p><strong>348.12 Uses Not Permitted:</strong> FMC shall not be used in the following:</p>
<ul>
    <li>In wet locations, unless the conductors are listed for the specific conditions and the installation prevents water from entering the conduit</li>
    <li>Where subject to physical damage</li>
    <li>In lengths longer than 6 feet (1.8 m), unless specifically permitted elsewhere in the Code</li>
    <li>Where operating voltage exceeds 600 volts, nominal</li>
    <li>In any hazardous (classified) location except as permitted by other articles in the Code</li>
</ul>

<h3>Installation Requirements</h3>
<p><strong>348.20 Size:</strong> FMC shall not be used in trade sizes less than metric designator 16 (trade size 1/2). The minimum size allowed depends on the number and size of conductors to be installed.</p>

<p><strong>348.22 Number of Conductors:</strong> The number of conductors permitted in FMC must not exceed the percentage fill specified in Table 1, Chapter 9. Calculations must be based on the dimensions provided in the tables or supplied by the manufacturer.</p>

<p><strong>348.24 Bends - How Made:</strong> Bends in FMC shall be made so that the conduit is not damaged and the internal diameter of the conduit is not effectively reduced. The radius of the curve of the inner edge of any bend shall not be less than shown in Table 2, Chapter 9.</p>

<p><strong>348.26 Bends - Number in One Run:</strong> There shall not be more than the equivalent of four quarter bends (360 degrees total) between pull points, for example, conduit bodies and boxes.</p>

<p><strong>348.28 Trimming:</strong> All cut ends shall be trimmed or otherwise finished to remove rough edges. This protects conductors from damage during installation.</p>

<p><strong>348.30 Securing and Supporting:</strong> FMC shall be securely fastened in place and supported in accordance with the following:</p>
<ul>
    <li>FMC shall be secured by an approved means within 12 inches (300 mm) of each box, cabinet, conduit body, or other conduit termination</li>
    <li>FMC shall be supported at intervals not exceeding 4.5 feet (1.4 m)</li>
    <li>Horizontal runs of FMC supported by openings through framing members at intervals not greater than 4.5 feet (1.4 m) and securely fastened within 12 inches (300 mm) of termination points shall be permitted</li>
    <li>Securing or supporting is not required where flexibility is necessary after installation</li>
    <li>Securing or supporting is not required for lengths not exceeding 3 feet (900 mm) at terminals where flexibility is necessary</li>
</ul>

<p><strong>348.42 Couplings and Connectors:</strong> Angle connectors shall not be used for concealed raceway installations. Couplings and connectors shall be compatible with the FMC and shall be of a type that will securely fasten the FMC to boxes, fittings, or other enclosures.</p>

<p><strong>348.60 Grounding and Bonding:</strong> When used with a listed grounding/bonding means, FMC can serve as an equipment grounding conductor if both the FMC and fittings are listed for grounding. If not, a separate equipment grounding conductor must be installed. If used for flexibility, an additional equipment grounding bonding jumper is generally required.</p>

<h3>Common Installation Issues</h3>
<ul>
    <li><strong>Excessive Length:</strong> Using FMC in runs longer than permitted (typically 6 feet except where specifically permitted)</li>
    <li><strong>Improper Installation in Wet Locations:</strong> Using standard FMC in wet locations instead of the appropriate LFMC</li>
    <li><strong>Inadequate Support:</strong> Not supporting FMC at the required intervals</li>
    <li><strong>Missing Bushings:</strong> Not using bushings or suitable fittings where the FMC connects to boxes or enclosures, potentially damaging conductor insulation</li>
    <li><strong>Improper Grounding:</strong> Relying on FMC for grounding without verification that the specific type is listed for this use</li>
</ul>

<h3>Advantages of FMC</h3>
<ul>
    <li><strong>Flexibility:</strong> Allows for easy installation around obstacles and in tight spaces</li>
    <li><strong>Vibration Isolation:</strong> Can absorb vibration from equipment, preventing transmission to the building structure</li>
    <li><strong>Thermal Movement:</strong> Accommodates thermal expansion and contraction in long runs</li>
    <li><strong>Physical Protection:</strong> Provides mechanical protection for enclosed conductors</li>
    <li><strong>Ease of Installation:</strong> Often quicker to install than rigid conduit in complex routing situations</li>
</ul>

<h3>Common Applications</h3>
<p>FMC is commonly used in:</p>
<ul>
    <li>Connections to motors and other vibrating equipment</li>
    <li>HVAC installations where equipment movement must be accommodated</li>
    <li>Installations where future movement or repositioning may be necessary</li>
    <li>Locations where rigid conduit would be difficult to install due to bends or alignment issues</li>
    <li>Connections to recessed lighting fixtures in suspended ceilings</li>
</ul>

<h3>Recent Code Changes</h3>
<p>Recent updates to Article 348 have included:</p>
<ul>
    <li>Clarification of requirements for FMC as an equipment grounding conductor</li>
    <li>Updates to support and securing requirements</li>
    <li>Refinement of permitted uses in specific locations</li>
</ul>

<p>When properly installed according to Article 348, Flexible Metal Conduit provides a versatile and effective raceway system that combines protection for conductors with the flexibility needed in many electrical installations.</p>
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
                print(f"NEC article 348 update completed successfully.")
            else:
                print(f"NEC article 348 update failed.")
    except Exception as e:
        print(f"Error updating NEC article 348: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
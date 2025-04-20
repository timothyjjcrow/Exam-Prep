import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 344 to the database."""
    article_data = {
        "article_number": "344",
        "title": "Rigid Metal Conduit: Type RMC",
        "summary": "Requirements for the installation and use of Rigid Metal Conduit (RMC) and associated fittings, providing the strongest level of mechanical protection for electrical conductors.",
        "content": """
<h3>Scope and Purpose</h3>
<p>Article 344 covers the use, installation, and construction specifications for Rigid Metal Conduit (RMC). RMC provides maximum mechanical protection for enclosed conductors and cables. It is the most physically robust of the metal raceway systems and is designed to withstand severe physical damage while providing a continuous ground path.</p>

<h3>Conduit Characteristics</h3>
<p><strong>344.100 Construction:</strong> RMC is a listed metal raceway of circular cross section with a coupling that can be either threaded or unthreaded. RMC is generally made in 10-foot lengths and is available in trade sizes ranging from metric designator 16 (trade size 1/2) through 155 (trade size 6). RMC is made of:</p>
<ul>
    <li>Steel (ferrous) with protective coatings (galvanized or coated with an approved corrosion-resistant material)</li>
    <li>Aluminum (nonferrous)</li>
    <li>Red brass</li>
    <li>Stainless steel</li>
</ul>

<p><strong>344.120 Marking:</strong> Each length of RMC shall be clearly and durably marked at least every 3 m (10 ft) with:</p>
<ul>
    <li>The manufacturer's name or trademark</li>
    <li>Material designation if other than steel</li>
    <li>Trade size</li>
</ul>

<h3>Uses Permitted</h3>
<p><strong>344.10 Uses Permitted:</strong> RMC can be used in all atmospheric conditions and occupancies, including:</p>
<ul>
    <li>In all atmospheric conditions and occupancies</li>
    <li>In both concealed and exposed locations</li>
    <li>In concrete (embedded), in direct contact with the earth, or in areas subject to severe corrosive influences when protected by corrosion protection judged suitable for the condition</li>
    <li>In wet locations</li>
    <li>In all hazardous (classified) locations as permitted by other applicable NEC articles</li>
</ul>

<h3>Uses Not Permitted</h3>
<p><strong>344.12 Uses Not Permitted:</strong> RMC shall not be used:</p>
<ul>
    <li>Where subject to severe corrosive conditions unless protected by material suitable for the condition</li>
</ul>

<h3>Installation Requirements</h3>
<p><strong>344.20 Size:</strong> RMC is available in trade sizes from metric designator 16 (trade size 1/2) through metric designator 155 (trade size 6). The minimum size allowed depends on the number and size of conductors to be installed.</p>

<p><strong>344.22 Number of Conductors:</strong> The number of conductors shall not exceed that permitted by the percentage fill specified in Table 1, Chapter 9. Calculations must be based on the dimensions provided in the tables or supplied by the manufacturer.</p>

<p><strong>344.24 Bends - How Made:</strong> Bends of RMC shall be made so that the conduit is not damaged and the internal diameter of the conduit is not effectively reduced. For field bends, the minimum radius shall not be less than shown in Table 2, Chapter 9. Factory bends are permitted.</p>

<p><strong>344.26 Bends - Number in One Run:</strong> There shall not be more than the equivalent of four quarter bends (360 degrees total) between pull points, for example, conduit bodies and boxes.</p>

<p><strong>344.28 Reaming and Threading:</strong> All cut ends shall be reamed or otherwise finished to remove rough edges. Where conduit is threaded in the field, a standard cutting die with a taper of 1 in 16 (3/4 inch per foot) shall be used.</p>

<p><strong>344.30 Securing and Supporting:</strong> RMC shall be installed as a complete system as provided in Article 300 and shall be secured in place and supported in accordance with the following:</p>
<ul>
    <li>RMC shall be securely fastened within 900 mm (3 ft) of each outlet box, junction box, device box, cabinet, conduit body, or other conduit termination</li>
    <li>RMC shall be supported at least every 3 m (10 ft)</li>
    <li>Straight runs of RMC supported by openings through framing members at intervals not greater than 3 m (10 ft) and securely fastened within 900 mm (3 ft) of termination points shall be permitted</li>
</ul>

<p><strong>344.42 Couplings and Connectors:</strong> Couplings and connectors used with RMC shall be made up tight. Where buried in masonry or concrete, they shall be of the concrete-tight type. Where installed in wet locations, they shall be listed for wet locations.</p>

<p><strong>344.46 Bushings:</strong> Where a conduit enters a box, fitting, or other enclosure, a bushing shall be provided to protect the wire from abrasion unless the design of the box, fitting, or enclosure affords equivalent protection.</p>

<p><strong>344.60 Grounding:</strong> RMC shall be permitted as an equipment grounding conductor when installed in accordance with 250.118.</p>

<h3>Advantages of RMC</h3>
<ul>
    <li><strong>Maximum Mechanical Protection:</strong> RMC provides the highest level of physical protection for enclosed conductors</li>
    <li><strong>Durability:</strong> Resists crushing, impact, and physical damage</li>
    <li><strong>Fire Resistance:</strong> Metal construction helps maintain circuit integrity during fires</li>
    <li><strong>Equipment Grounding:</strong> Serves as an effective equipment grounding conductor</li>
    <li><strong>Longevity:</strong> When properly installed and protected against corrosion, has an extremely long service life</li>
</ul>

<h3>Common Installation Issues</h3>
<ul>
    <li><strong>Improper Threading:</strong> Not using the proper die or not cutting threads to the proper length</li>
    <li><strong>Corrosion:</strong> Failing to provide proper corrosion protection in harsh environments</li>
    <li><strong>Inadequate Support:</strong> Not securing RMC at the required intervals</li>
    <li><strong>Sharp Edges:</strong> Not properly reaming cut ends, which can damage conductor insulation</li>
    <li><strong>Excessive Bending:</strong> Exceeding four quarter bends between pull points, making conductor pulling difficult or impossible</li>
</ul>

<h3>Material Selection Considerations</h3>
<ul>
    <li><strong>Steel RMC:</strong> Most common, suitable for most environments when properly protected</li>
    <li><strong>Aluminum RMC:</strong> Lighter weight, excellent corrosion resistance in certain environments, not suitable where exposed to certain materials (concrete, masonry)</li>
    <li><strong>Stainless Steel RMC:</strong> Superior corrosion resistance for harsh chemical environments</li>
    <li><strong>Red Brass:</strong> Specialty applications with specific corrosion resistance requirements</li>
</ul>

<h3>Common Applications</h3>
<p>RMC is commonly used in:</p>
<ul>
    <li>Industrial facilities where physical protection is paramount</li>
    <li>Hazardous (classified) locations where explosion-proof installations are required</li>
    <li>Exposed outdoor locations that may be subject to physical damage</li>
    <li>Service entrances where maximum protection is desired</li>
    <li>Vehicle service bays, loading docks, and other areas with high potential for physical impact</li>
</ul>

<h3>Recent Code Changes</h3>
<p>Recent updates to Article 344 have included:</p>
<ul>
    <li>Clarification of support requirements</li>
    <li>Updates to corrosion protection requirements</li>
    <li>Enhanced guidance on proper installation in various environments</li>
    <li>Refinement of listing requirements for fittings</li>
</ul>

<p>Rigid Metal Conduit remains one of the most reliable and durable wiring methods available. When properly installed according to the requirements of Article 344, RMC provides maximum protection for conductors and a high level of safety for electrical systems, especially in demanding environments or where physical damage is likely.</p>
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
                print(f"NEC article 344 update completed successfully.")
            else:
                print(f"NEC article 344 update failed.")
    except Exception as e:
        print(f"Error updating NEC article 344: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
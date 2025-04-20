import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 342 to the database."""
    article_data = {
        "article_number": "342",
        "title": "Intermediate Metal Conduit: Type IMC",
        "summary": "Requirements for the installation and use of Intermediate Metal Conduit (IMC) and associated fittings for electrical systems.",
        "content": """
<h3>Scope and Purpose</h3>
<p>Article 342 covers the use, installation, and construction specifications for Intermediate Metal Conduit (IMC). IMC provides a protected pathway for electrical conductors with mechanical strength intermediate between rigid metal conduit and electrical metallic tubing. It is designed to provide physical protection and a continuous ground path while being lighter and more economical than rigid metal conduit.</p>

<h3>Conduit Characteristics</h3>
<p><strong>Construction:</strong> IMC is made of steel with protective coatings (typically galvanized) or aluminum, providing strong mechanical protection for enclosed conductors. It is lighter than rigid metal conduit but heavier and stronger than electrical metallic tubing (EMT).</p>

<p><strong>342.100 Construction:</strong> IMC shall be made of steel with protective coatings or of listed aluminum, and shall comply with the following applicable standard:</p>
<ul>
    <li>UL 1242, Intermediate Metal Conduit - Steel</li>
</ul>

<p><strong>342.120 Marking:</strong> Each length of IMC shall be clearly and durably marked at least every 1.5 m (5 ft) with:</p>
<ul>
    <li>The manufacturer's name or trademark</li>
    <li>The material designation</li>
    <li>The trade size</li>
</ul>

<h3>Uses Permitted</h3>
<p><strong>342.10 Uses Permitted:</strong> IMC can be used in nearly all electrical installations, including:</p>
<ul>
    <li>In all atmospheric conditions and occupancies</li>
    <li>In both concealed and exposed locations</li>
    <li>In concrete (embedded), in direct contact with the earth, or in areas subject to severe corrosive influences when protected by corrosion protection judged suitable for the condition</li>
    <li>In wet locations</li>
    <li>In hazardous (classified) locations as permitted by other applicable NEC articles</li>
</ul>

<h3>Uses Not Permitted</h3>
<p><strong>342.12 Uses Not Permitted:</strong> IMC shall not be used:</p>
<ul>
    <li>Where subject to severe corrosive conditions, unless protected by materials suitable for the condition</li>
</ul>

<h3>Installation Requirements</h3>
<p><strong>342.20 Size:</strong> IMC is available in trade sizes from metric designator 16 (trade size 1/2) through metric designator 103 (trade size 4). The minimum size allowed depends on the number and size of conductors to be installed.</p>

<p><strong>342.22 Number of Conductors:</strong> The number of conductors permitted in IMC must not exceed the percentage fill specified in Table 1, Chapter 9. Calculations must be based on the dimensions provided in the tables or supplied by the manufacturer.</p>

<p><strong>342.24 Bends - How Made:</strong> Bends of IMC shall be made so that the conduit is not damaged and the internal diameter of the conduit is not effectively reduced. For field bends, the minimum radius shall not be less than shown in Table 2, Chapter 9. Factory bends shall be permitted.</p>

<p><strong>342.26 Bends - Number in One Run:</strong> There shall not be more than the equivalent of four quarter bends (360 degrees total) between pull points, for example, conduit bodies and boxes.</p>

<p><strong>342.28 Reaming and Threading:</strong> All cut ends shall be reamed to remove rough edges. Where IMC is threaded in the field, a standard cutting die with a taper of 1 in 16 (3/4 inch per foot) shall be used.</p>

<p><strong>342.30 Securing and Supporting:</strong> IMC shall be installed as a complete system as provided in Article 300 and shall be secured in place and supported in accordance with the following:</p>
<ul>
    <li>IMC shall be securely fastened within 900 mm (3 ft) of each outlet box, junction box, device box, cabinet, conduit body, or other conduit termination</li>
    <li>IMC shall be supported at least every 3 m (10 ft)</li>
    <li>Straight runs of IMC supported by openings through framing members at intervals not greater than 3 m (10 ft) and securely fastened within 900 mm (3 ft) of termination points shall be permitted</li>
</ul>

<p><strong>342.42 Couplings and Connectors:</strong> Couplings and connectors used with IMC shall be made up tight. Where buried in masonry or concrete, they shall be of the concrete-tight type. Where installed in wet locations, they shall be listed for wet locations.</p>

<p><strong>342.46 Bushings:</strong> Where a conduit enters a box, fitting, or other enclosure, a bushing shall be provided to protect the wire from abrasion unless the design of the box, fitting, or enclosure affords equivalent protection.</p>

<p><strong>342.60 Grounding:</strong> IMC shall be permitted as an equipment grounding conductor when installed in accordance with 250.118.</p>

<h3>Common Installation Issues</h3>
<ul>
    <li><strong>Improper Support:</strong> Not securing IMC within the required distance from boxes or at proper intervals</li>
    <li><strong>Excessive Bends:</strong> Exceeding the allowed four quarter bends between pull points</li>
    <li><strong>Improper Cutting:</strong> Failure to ream cut ends, leaving rough edges that can damage conductor insulation</li>
    <li><strong>Corrosion Concerns:</strong> Installing unprotected IMC in highly corrosive environments</li>
    <li><strong>Inadequate Fittings:</strong> Using fittings not rated for the environment (wet locations, etc.)</li>
</ul>

<h3>Advantages of IMC</h3>
<ul>
    <li><strong>Mechanical Strength:</strong> More durable than EMT but lighter than rigid metal conduit</li>
    <li><strong>Corrosion Resistance:</strong> Galvanized coating provides good protection in many environments</li>
    <li><strong>Equipment Grounding:</strong> Serves as an effective equipment grounding conductor</li>
    <li><strong>Fire Resistance:</strong> Non-combustible material helps maintain circuit integrity during fires</li>
    <li><strong>Versatility:</strong> Suitable for nearly all locations and conditions when properly installed</li>
</ul>

<h3>Common Applications</h3>
<p>IMC is commonly used in:</p>
<ul>
    <li>Commercial construction where physical protection is important but the weight of rigid metal conduit is a concern</li>
    <li>Industrial facilities that require moderate mechanical protection</li>
    <li>Outdoor installations where galvanized IMC provides adequate corrosion protection</li>
    <li>Installations where a more economical alternative to rigid metal conduit is desired</li>
</ul>

<h3>Recent Code Changes</h3>
<p>Recent updates to Article 342 have included:</p>
<ul>
    <li>Clarification of support requirements</li>
    <li>Updates to corrosion protection requirements</li>
    <li>Refinement of listing requirements for fittings</li>
</ul>

<p>Proper adherence to the requirements in Article 342 ensures that IMC installations provide safe, reliable pathways for conductors with appropriate mechanical protection and grounding capabilities.</p>
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
                print(f"NEC article 342 update completed successfully.")
            else:
                print(f"NEC article 342 update failed.")
    except Exception as e:
        print(f"Error updating NEC article 342: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
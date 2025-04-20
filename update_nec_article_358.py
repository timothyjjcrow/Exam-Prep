import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 358 to the database."""
    article_data = {
        "article_number": "358",
        "title": "Electrical Metallic Tubing: Type EMT",
        "summary": "Requirements for the installation and use of Electrical Metallic Tubing (EMT), a lightweight, thin-walled raceway that provides moderate mechanical protection for enclosed conductors.",
        "content": """
<h3>Scope and Purpose</h3>
<p>Article 358 covers the use, installation, and construction specifications for Electrical Metallic Tubing (EMT), also known as thin-wall conduit. EMT is a lightweight metal raceway with walls thinner than those of Intermediate Metal Conduit (IMC) or Rigid Metal Conduit (RMC). EMT provides moderate mechanical protection for enclosed conductors while being more economical and easier to install than heavier conduit types.</p>

<h3>Conduit Characteristics</h3>
<p><strong>358.100 Construction:</strong> EMT is a listed metal raceway of circular cross section that is unthreaded, with thinner walls than rigid metal conduit. EMT is made of steel (with or without protective coatings) or aluminum. It is available in trade sizes from metric designator 16 (trade size 1/2) through metric designator 103 (trade size 4).</p>

<p><strong>358.120 Marking:</strong> EMT shall be clearly and durably marked at least every 3 m (10 ft) with:</p>
<ul>
    <li>Manufacturer's name or trademark</li>
    <li>The material designation if other than steel</li>
    <li>The trade size</li>
</ul>

<h3>Uses Permitted</h3>
<p><strong>358.10 Uses Permitted:</strong> EMT is permitted for both exposed and concealed work in the following locations:</p>
<ul>
    <li>In concrete, in direct contact with the earth, or in areas subject to severe corrosive influences where protected by corrosion protection judged suitable for the condition</li>
    <li>For the support of luminaires or other equipment</li>
    <li>In wet locations where the entire EMT system including all fittings is installed to prevent water from entering the tubing</li>
    <li>In hazardous (classified) locations as permitted by other Articles in the Code</li>
</ul>

<h3>Uses Not Permitted</h3>
<p><strong>358.12 Uses Not Permitted:</strong> EMT shall not be used in the following:</p>
<ul>
    <li>Where subject to severe physical damage</li>
    <li>For the support of luminaires or other equipment except conduit bodies no larger than the largest trade size of the tubing</li>
    <li>Where practicably subject to severe corrosive influences, unless protected by corrosion protection judged suitable for the condition</li>
</ul>

<h3>Installation Requirements</h3>
<p><strong>358.20 Size:</strong> EMT shall not be used in trade sizes less than metric designator 16 (trade size 1/2).</p>

<p><strong>358.22 Number of Conductors:</strong> The number of conductors permitted in EMT must not exceed the percentage fill specified in Table 1, Chapter 9. Calculations must be based on the dimensions provided in the tables or supplied by the manufacturer.</p>

<p><strong>358.24 Bends - How Made:</strong> Bends in EMT shall be made so that the tubing is not damaged and the internal diameter of the tubing is not effectively reduced. For field bends, the minimum radius shall not be less than shown in Table 2, Chapter 9.</p>

<p><strong>358.26 Bends - Number in One Run:</strong> There shall not be more than the equivalent of four quarter bends (360 degrees total) between pull points, for example, conduit bodies and boxes.</p>

<p><strong>358.28 Reaming and Threading:</strong> All cut ends of EMT shall be reamed or otherwise finished to remove rough edges. EMT shall not be threaded. Couplings and connectors used with EMT shall be of the set-screw or compression type.</p>

<p><strong>358.30 Securing and Supporting:</strong> EMT shall be installed as a complete system as provided in Article 300 and shall be securely fastened in place and supported in accordance with the following:</p>
<ul>
    <li>EMT shall be securely fastened in place at least every 3 m (10 ft)</li>
    <li>Each EMT run shall be secured within 900 mm (3 ft) of each outlet box, junction box, device box, cabinet, conduit body, or other tubing termination</li>
    <li>Fastened in place is not required for concealed work in finished buildings or prefinished wall panels where such securing is impracticable</li>
    <li>Horizontal runs of EMT supported by openings through framing members at intervals not greater than 3 m (10 ft) and securely fastened within 900 mm (3 ft) of termination points shall be permitted</li>
</ul>

<p><strong>358.42 Couplings and Connectors:</strong> Couplings and connectors used with EMT shall be made up tight. Where buried in masonry or concrete, they shall be of the concrete-tight type. Where installed in wet locations, they shall be listed for wet locations.</p>

<p><strong>358.60 Grounding and Bonding:</strong> EMT shall be permitted as an equipment grounding conductor when both the EMT and fittings are listed for grounding and when installed in accordance with 250.118.</p>

<h3>Common Installation Issues</h3>
<ul>
    <li><strong>Physical Damage:</strong> Installing EMT in locations subject to severe physical damage, where rigid or intermediate conduit would be more appropriate</li>
    <li><strong>Improper Connections:</strong> Not fully tightening set-screw or compression fittings, compromising the mechanical and electrical continuity of the system</li>
    <li><strong>Over-bending:</strong> Creating bends with radii smaller than permitted, potentially damaging the conduit or making conductor pulling difficult</li>
    <li><strong>Inadequate Support:</strong> Not securing EMT at required intervals or distances from termination points</li>
    <li><strong>Improper Fittings:</strong> Using fittings not suitable for the installation environment (e.g., non-weatherproof fittings in wet locations)</li>
    <li><strong>Missing Bushings:</strong> Not properly reaming cut ends or installing bushings where required, potentially damaging conductor insulation</li>
</ul>

<h3>Advantages of EMT</h3>
<ul>
    <li><strong>Cost-effective:</strong> Less expensive than rigid or intermediate metal conduit</li>
    <li><strong>Lightweight:</strong> Easier to handle and install than heavier conduit types</li>
    <li><strong>Moderate Protection:</strong> Provides good mechanical protection in many environments</li>
    <li><strong>Equipment Grounding:</strong> Can serve as an equipment grounding conductor when properly installed with listed fittings</li>
    <li><strong>Bendability:</strong> Can be bent with hand benders, making field installations more efficient</li>
    <li><strong>Fire Resistance:</strong> Non-combustible material helps maintain circuit integrity during fires</li>
</ul>

<h3>Common Applications</h3>
<p>EMT is commonly used in:</p>
<ul>
    <li>Commercial construction for branch circuits and feeders</li>
    <li>Light industrial applications where extreme physical protection is not required</li>
    <li>Exposed installations in finished spaces where appearance is important</li>
    <li>Institutional buildings such as schools and hospitals</li>
    <li>Retail spaces and office buildings</li>
    <li>Residential garages and basements</li>
</ul>

<h3>Selection Considerations</h3>
<p>When selecting EMT for an installation, consider:</p>
<ul>
    <li><strong>Physical Protection:</strong> EMT provides less physical protection than rigid or intermediate conduit. Assess the risk of physical damage in the installation location.</li>
    <li><strong>Corrosion:</strong> Standard steel EMT is subject to corrosion in wet or corrosive environments unless properly coated or aluminum EMT is used.</li>
    <li><strong>Fittings:</strong> Set-screw fittings are generally used in dry, indoor locations, while compression fittings are required in wet or damp locations.</li>
    <li><strong>Support Requirements:</strong> Ensure the structure can accommodate the required support intervals for EMT.</li>
</ul>

<h3>Recent Code Changes</h3>
<p>Recent updates to Article 358 have included:</p>
<ul>
    <li>Clarification of support and securing requirements</li>
    <li>Updates to permitted uses in specific applications</li>
    <li>Enhanced guidance on corrosion protection requirements</li>
    <li>Refinement of requirements for EMT as an equipment grounding conductor</li>
</ul>

<p>Electrical Metallic Tubing remains one of the most widely used raceway systems due to its balance of cost, physical protection, and ease of installation. When properly installed according to Article 358, EMT provides a reliable and safe pathway for electrical conductors in a wide variety of applications.</p>
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
                print(f"NEC article 358 update completed successfully.")
            else:
                print(f"NEC article 358 update failed.")
    except Exception as e:
        print(f"Error updating NEC article 358: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
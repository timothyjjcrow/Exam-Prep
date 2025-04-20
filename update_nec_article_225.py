import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 225 to the database."""
    article_data = {
        "article_number": "225",
        "title": "Outside Branch Circuits and Feeders",
        "summary": "Requirements for outside branch circuits and feeders run on or between buildings, structures, or poles on the premises; and electrical equipment and wiring for the supply of utilization equipment located on or attached to the outside of buildings, structures, or poles.",
        "content": """
<h3>Scope and Coverage</h3>
<p>Article 225 provides requirements for outside branch circuits and feeders that are installed outdoors, between buildings, or on poles. These requirements are in addition to the general wiring methods covered elsewhere in the Code.</p>

<h3>Key Provisions</h3>
<ul>
    <li><strong>225.4 Conductor Covering:</strong> Where conductors are within reach from ground, roof, or window, they require additional insulation or covering for protection.</li>
    
    <li><strong>225.6 Conductor Size and Support:</strong> 
        <ul>
            <li>Overhead spans require minimum size of 10 AWG copper or 8 AWG aluminum for spans up to 50 feet</li>
            <li>Larger conductors required for longer spans</li>
            <li>Support must be provided to prevent excessive sag</li>
        </ul>
    </li>
    
    <li><strong>225.10 Wiring on Buildings:</strong> Conductors on exterior surfaces of buildings must be installed in raceways, cable trays, cables, or as open wiring on insulators as specified in the code.</li>
    
    <li><strong>225.15 Supports Over Buildings:</strong> Conductors passing over buildings must be securely supported and meet clearance requirements.</li>
    
    <li><strong>225.18 Clearance from Ground:</strong> Specific minimum clearances are required:
        <ul>
            <li>10 feet above finished grade, sidewalks, or platforms for circuits up to 150V</li>
            <li>12 feet above residential property and driveways</li>
            <li>18 feet above public streets, alleys, roads, and parking areas subject to truck traffic</li>
        </ul>
    </li>
    
    <li><strong>225.19 Clearances from Buildings:</strong> Conductors must maintain specific clearances from building openings:
        <ul>
            <li>3 feet from windows, doors, porches, or similar locations</li>
            <li>Vertical clearance of 8 feet above roofs (with exceptions)</li>
        </ul>
    </li>
    
    <li><strong>225.20 Mechanical Protection of Conductors:</strong> Requirements for protection against physical damage where exposed to physical damage.</li>
    
    <li><strong>225.22 Raceways on Exterior Surfaces:</strong> Raceways on exterior surfaces must be arranged to drain and be suitable for wet locations.</li>
    
    <li><strong>225.30 Number of Supplies:</strong> Limits the number of feeders or branch circuits supplying a building to one, with six specific exceptions.</li>
    
    <li><strong>225.31 Disconnecting Means:</strong> Requires a means to disconnect all ungrounded conductors that supply or pass through a building/structure.</li>
    
    <li><strong>225.32 Location:</strong> The disconnecting means must be installed at a readily accessible location either outside or inside nearest the point of entrance.</li>
    
    <li><strong>225.33 Maximum Number of Disconnects:</strong> The disconnecting means shall consist of not more than six switches or sets of circuit breakers.</li>
    
    <li><strong>225.36 Suitable for Service Equipment:</strong> The disconnecting means specified in 225.31 shall be suitable for use as service equipment.</li>
    
    <li><strong>225.39 Rating of Disconnect:</strong> The feeder or branch circuit disconnecting means shall have a rating of not less than 30 amperes.</li>
    
    <li><strong>225.51-225.56 Identification and Marking:</strong> Requirements for labeling and identification of outdoor disconnects and equipment.</li>
</ul>

<h3>Common Applications</h3>
<p>Article 225 is frequently applied in these scenarios:</p>
<ul>
    <li>Installation of feeders to detached garages or accessory buildings</li>
    <li>Supply to outbuildings on commercial and industrial properties</li>
    <li>Overhead distribution on private property</li>
    <li>Outdoor lighting installations</li>
    <li>Connections between multiple buildings on the same property</li>
</ul>

<h3>Critical Safety Considerations</h3>
<p>The requirements in Article 225 are particularly important for safety because outside installations are exposed to weather, physical damage, and often involve longer runs with different clearance requirements than indoor wiring. Following these requirements helps prevent hazards such as shock, electrocution, and fire due to deteriorated insulation or physical damage to conductors and equipment.</p>
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

def main():
    """Create app context and run the update function."""
    try:
        app = create_app()
        with app.app_context():
            update_nec_article()
        print(f"NEC article 225 update completed successfully.")
    except Exception as e:
        print(f"Error updating NEC article 225: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 230 to the database."""
    article_data = {
        "article_number": "230",
        "title": "Services",
        "summary": "Requirements for service conductors and equipment for control and protection of services, and their installation requirements.",
        "content": """
<h3>Scope and Coverage</h3>
<p>Article 230 covers service conductors and equipment for control and protection of services, and their installation requirements. It includes provisions for service drops, laterals, conductors, equipment, disconnecting means, overcurrent protection, and grounding.</p>

<h3>Key Provisions</h3>
<ul>
    <li><strong>230.6 Conductors Considered Outside the Building:</strong> Defines conditions under which conductors are considered outside a building for application of requirements in this article.</li>
    
    <li><strong>230.9 Clearances on Buildings:</strong> Service conductors and final spans must maintain specified clearances:
        <ul>
            <li>3 feet from windows, doors, porches, balconies, ladders, stairs, fire escapes, etc.</li>
            <li>Exceptions for conductors run above the top level of a window</li>
        </ul>
    </li>
    
    <li><strong>230.24 Clearances:</strong> Overhead service conductors must maintain:
        <ul>
            <li>8 feet clearance above roofs with minimum slope of 4/12</li>
            <li>10 feet above finished grade or sidewalks</li>
            <li>12 feet over residential driveways</li>
            <li>18 feet over public streets and roads</li>
        </ul>
    </li>
    
    <li><strong>230.42 Minimum Size and Rating:</strong> Service-entrance conductors must have sufficient ampacity to carry the load as calculated in Article 220, and not be smaller than 8 AWG copper or 6 AWG aluminum.</li>
    
    <li><strong>230.43 Wiring Methods for 1000 Volts or Less:</strong> Lists permitted wiring methods for service-entrance conductors, including:
        <ul>
            <li>Open wiring on insulators</li>
            <li>Type IGS cable</li>
            <li>Rigid metal conduit</li>
            <li>Intermediate metal conduit</li>
            <li>Electrical metallic tubing</li>
            <li>Electrical nonmetallic tubing</li>
            <li>Service-entrance cables</li>
            <li>Wireways</li>
            <li>Busways</li>
            <li>And other specified raceways and cables</li>
        </ul>
    </li>
    
    <li><strong>230.70 General Service Disconnecting Means:</strong> 
        <ul>
            <li>Each service must have means to disconnect all conductors from the service-entrance conductors</li>
            <li>Disconnect must be installed at a readily accessible location either outside or inside nearest the point of entrance</li>
            <li>Permanently marked to identify it as a service disconnect</li>
        </ul>
    </li>
    
    <li><strong>230.71 Maximum Number of Disconnects:</strong> Service disconnecting means shall consist of not more than six switches or six circuit breakers mounted in a single enclosure or grouped in separate enclosures.</li>
    
    <li><strong>230.75 Disconnection of Grounded Conductor:</strong> Where the service disconnecting means disconnects the ungrounded service conductors, it shall also disconnect the grounded conductor from the premises wiring system.</li>
    
    <li><strong>230.82 Equipment Connected to the Supply Side:</strong> Lists equipment permitted to be connected to the supply side of the service disconnecting means, including:
        <ul>
            <li>Cable limiters or other current-limiting devices</li>
            <li>Meters and meter sockets</li>
            <li>Meter disconnect switches</li>
            <li>Instrument transformers</li>
            <li>Surge protective devices</li>
            <li>And other specified equipment</li>
        </ul>
    </li>
    
    <li><strong>230.90 Where Required:</strong> Each ungrounded service conductor shall have overload protection.</li>
    
    <li><strong>230.91 Location:</strong> The service overcurrent device shall be an integral part of the service disconnecting means or located immediately adjacent thereto.</li>
    
    <li><strong>230.95 Ground-Fault Protection of Equipment:</strong> Ground-fault protection shall be provided for solidly grounded wye electrical services of more than 150 volts to ground but not exceeding 1000 volts phase-to-phase for each service disconnect rated 1000 amperes or more.</li>
</ul>

<h3>Significant Considerations</h3>
<p>The service is the point of connection between the utility supply and the premises wiring system. Article 230 provisions are critical because:</p>
<ul>
    <li>They constitute primary safety provisions that protect the entire electrical installation</li>
    <li>They establish the capacity of the service, affecting the entire electrical system</li>
    <li>They define disconnecting requirements that impact emergency access and safety</li>
    <li>Requirements must coordinate with both the NEC and the serving utility's requirements</li>
</ul>

<h3>Common Applications</h3>
<p>Article 230 requirements apply to:</p>
<ul>
    <li>Residential service installations</li>
    <li>Commercial building services</li>
    <li>Industrial services</li>
    <li>Service upgrades and modifications</li>
    <li>Temporary services for construction</li>
</ul>

<h3>Coordination with Utilities</h3>
<p>While Article 230 establishes minimum safety requirements for services, it's important to note that utility companies often have additional requirements that must be followed. Always coordinate with the local utility when installing or modifying services.</p>
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
        print(f"NEC article 230 update completed successfully.")
    except Exception as e:
        print(f"Error updating NEC article 230: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
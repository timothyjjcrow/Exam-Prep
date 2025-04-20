import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from circuit_breaker_app import create_app, db
from circuit_breaker_app.models import NECArticle

def update_nec_articles():
    """Add or update NEC articles in the database."""
    
    # Articles data
    articles = [
        {
            "article_number": "100",
            "title": "Definitions",
            "summary": "Provides definitions of terms used throughout the NEC that are essential for proper application and understanding of the Code requirements.",
            "content": """<h2>Article 100: Definitions</h2>
            <p>This article contains definitions essential to the proper application of the NEC. It includes terms that are used in two or more articles of the Code.</p>
            
            <h3>Key Definitions</h3>
            <ul>
                <li><strong>Accessible (as applied to equipment):</strong> Admitting close approach; not guarded by locked doors, elevation, or other effective means.</li>
                <li><strong>Ampacity:</strong> The maximum current, in amperes, that a conductor can carry continuously under the conditions of use without exceeding its temperature rating.</li>
                <li><strong>Branch Circuit:</strong> The circuit conductors between the final overcurrent device protecting the circuit and the outlet(s).</li>
                <li><strong>Circuit Breaker:</strong> A device designed to open and close a circuit by nonautomatic means and to open the circuit automatically on a predetermined overcurrent without damage to itself when properly applied within its rating.</li>
                <li><strong>Feeder:</strong> All circuit conductors between the service equipment, the source of a separately derived system, or other power supply source and the final branch-circuit overcurrent device.</li>
                <li><strong>Ground:</strong> The earth.</li>
                <li><strong>Grounded (Grounding):</strong> Connected to ground or to a conductive body that extends the ground connection.</li>
                <li><strong>Ground Fault:</strong> An unintentional, electrically conductive connection between an ungrounded conductor of an electrical circuit and the normally non-current-carrying conductors, metallic enclosures, metallic raceways, metallic equipment, or earth.</li>
                <li><strong>Qualified Person:</strong> One who has skills and knowledge related to the construction and operation of the electrical equipment and installations and has received safety training to recognize and avoid the hazards involved.</li>
                <li><strong>Service:</strong> The conductors and equipment for delivering electric energy from the serving utility to the wiring system of the premises served.</li>
                <li><strong>Voltage (of a circuit):</strong> The greatest root-mean-square (rms) (effective) difference of potential between any two conductors of the circuit concerned.</li>
            </ul>
            
            <p>These definitions are crucial for understanding electrical code requirements and ensuring safe, compliant installations.</p>"""
        },
        {
            "article_number": "110",
            "title": "Requirements for Electrical Installations",
            "summary": "Covers general requirements for electrical installations, including examination and approval of equipment, installations, conductors, and working spaces.",
            "content": """<h2>Article 110: Requirements for Electrical Installations</h2>
            <p>This article covers general requirements for the examination and approval of electrical equipment and installations, working spaces, and guarding of live parts.</p>
            
            <h3>110.3 Examination, Identification, Installation, and Use of Equipment</h3>
            <p>Equipment must be:</p>
            <ul>
                <li>Listed or labeled by a nationally recognized testing laboratory (NRTL)</li>
                <li>Installed and used according to any instructions included in the listing or labeling</li>
                <li>Suitable for the environment where it will be used</li>
            </ul>
            
            <h3>110.9 Interrupting Rating</h3>
            <p>Equipment intended to interrupt current at fault levels must have an interrupting rating not less than the nominal circuit voltage and the current that is available at the line terminals of the equipment.</p>
            
            <h3>110.12 Mechanical Execution of Work</h3>
            <p>Electrical equipment shall be installed in a neat and workmanlike manner.</p>
            
            <h3>110.13 Mounting and Cooling of Equipment</h3>
            <p>Electrical equipment must be firmly secured to the surface on which it is mounted and must be installed in a manner that allows for proper cooling.</p>
            
            <h3>110.14 Electrical Connections</h3>
            <p>Connections must ensure a good connection without damaging the conductors. Terminals for more than one conductor must be identified for this use.</p>
            
            <h3>110.26 Spaces About Electrical Equipment</h3>
            <p>Sufficient access and working space must be provided and maintained around all electrical equipment to permit ready and safe operation and maintenance.</p>
            <ul>
                <li>Working space depth: 3 feet (for 0-150V to ground), 3½ feet (for 151-600V to ground), or 4 feet (for over 600V)</li>
                <li>Headroom must be at least 6½ feet</li>
                <li>For equipment likely to require examination, adjustment, servicing, or maintenance while energized, the width of the working space must be at least 30 inches</li>
            </ul>"""
        },
        {
            "article_number": "200",
            "title": "Use and Identification of Grounded Conductors",
            "summary": "Covers the identification and use of grounded conductors, including color coding requirements.",
            "content": """<h2>Article 200: Use and Identification of Grounded Conductors</h2>
            <p>This article provides requirements for the identification and use of grounded conductors (typically the neutral conductor in residential and commercial wiring).</p>
            
            <h3>200.1 Scope</h3>
            <p>This article provides requirements for:</p>
            <ul>
                <li>Identification of grounded conductors</li>
                <li>The use and identification of grounded conductors</li>
            </ul>
            
            <h3>200.6 Means of Identifying Grounded Conductors</h3>
            <p>Grounded conductors must be identified as follows:</p>
            <ul>
                <li>For sizes 6 AWG or smaller: continuous white or gray outer finish, or three continuous white or gray stripes along the conductor's entire length on other than green insulation</li>
                <li>For sizes larger than 6 AWG: either a continuous white or gray outer finish or with three continuous white or gray stripes, or at the time of installation, by distinctive white or gray marking at terminations</li>
            </ul>
            
            <h3>200.7 Use of Insulation that is White or Gray</h3>
            <p>A white or gray insulated conductor can only be used as an ungrounded conductor where:</p>
            <ul>
                <li>It is part of a cable assembly and the insulation is permanently re-identified to indicate its use (e.g., with paint, tape, or other effective means)</li>
                <li>It is a flexible cord with the re-identified conductor at the time of installation</li>
            </ul>
            
            <h3>200.10 Identification of Terminals</h3>
            <p>Terminals for connection of grounded conductors must be:</p>
            <ul>
                <li>Identified by a white marking or other equally effective means</li>
                <li>Substantially white in color for devices and equipment</li>
                <li>Identified by the letters "W" or "WH" where terminal markings are required</li>
            </ul>"""
        },
        {
            "article_number": "210",
            "title": "Branch Circuits",
            "summary": "Covers branch circuit requirements, including ratings, permitted loads, and required outlets for specific locations.",
            "content": """<h2>Article 210: Branch Circuits</h2>
            <p>This article covers branch circuit requirements including provisions for branch-circuit ratings, permitted loads, required outlets, and location of outlets.</p>
            
            <h3>210.3 Rating</h3>
            <p>Branch circuits shall be rated according to the maximum permitted ampere rating of the overcurrent device. Typical branch circuit ratings are 15, 20, 30, 40, and 50 amperes.</p>
            
            <h3>210.4 Multiwire Branch Circuits</h3>
            <p>Multiwire branch circuits (having a shared neutral) must have all ungrounded conductors disconnected simultaneously if serving line-to-neutral loads. They must also be grouped together with a tie or similar means at the point of origination where the branch circuit receives its supply.</p>
            
            <h3>210.8 Ground-Fault Circuit-Interrupter Protection for Personnel</h3>
            <p>GFCI protection is required for receptacles installed in the following locations:</p>
            <p><strong>Dwelling Units:</strong></p>
            <ul>
                <li>Bathrooms</li>
                <li>Kitchens (serving countertops)</li>
                <li>Outdoors</li>
                <li>Basements (finished or unfinished)</li>
                <li>Garages and accessory buildings</li>
                <li>Crawl spaces</li>
                <li>Unfinished portions or areas of the basement</li>
                <li>Boathouses</li>
                <li>Bathtubs or shower stalls (within 6 feet)</li>
                <li>Laundry areas</li>
            </ul>
            
            <h3>210.11 Branch Circuits Required</h3>
            <p>Branch circuits for lighting and appliances must be provided as follows:</p>
            <ul>
                <li>Two or more 20-amp small-appliance branch circuits for receptacles in kitchen, pantry, dining room</li>
                <li>At least one 20-amp branch circuit for bathroom receptacle outlets</li>
                <li>At least one 20-amp branch circuit for laundry receptacles</li>
            </ul>
            
            <h3>210.52 Dwelling Unit Receptacle Outlets</h3>
            <p>Receptacle outlets must be installed as follows:</p>
            <ul>
                <li><strong>General areas:</strong> Receptacles shall be installed so that no point measured horizontally along the floor line in any wall space is more than 6 feet from a receptacle outlet</li>
                <li><strong>Kitchen Countertops:</strong> Receptacles shall be installed so that no point along the wall line is more than 24 inches from a receptacle outlet. Countertops wider than 12 inches require at least one receptacle</li>
                <li><strong>Bathrooms:</strong> At least one receptacle outlet must be installed within 3 feet of the outside edge of each basin</li>
                <li><strong>Outdoor:</strong> At least one receptacle outlet accessible at grade level must be installed at the front and back of the dwelling</li>
                <li><strong>Laundry:</strong> At least one receptacle outlet shall be installed in laundry areas</li>
                <li><strong>Garages:</strong> At least one receptacle outlet in each attached garage and in each detached garage with electric power</li>
            </ul>"""
        }
    ]
    
    added_count = 0
    updated_count = 0
    
    for article_data in articles:
        # Check if the article exists
        article = NECArticle.query.filter_by(article_number=article_data['article_number']).first()
        
        if article:
            # Update existing article
            article.title = article_data['title']
            article.summary = article_data['summary']
            article.content = article_data['content']
            updated_count += 1
            print(f"Updated Article {article_data['article_number']}: {article_data['title']}")
        else:
            # Add new article
            new_article = NECArticle(
                article_number=article_data['article_number'],
                title=article_data['title'],
                summary=article_data['summary'],
                content=article_data['content']
            )
            db.session.add(new_article)
            added_count += 1
            print(f"Added Article {article_data['article_number']}: {article_data['title']}")
    
    # Commit changes
    db.session.commit()
    
    print(f"\nSummary: Added {added_count} articles, Updated {updated_count} articles")
    return added_count, updated_count

def main():
    """Main function to create app context and run the update."""
    try:
        app = create_app()
        with app.app_context():
            update_nec_articles()
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main()) 
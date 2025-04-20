import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 110 to the database."""
    # Article data
    article_data = {
        "article_number": "110",
        "title": "Requirements for Electrical Installations",
        "summary": "Article 110 covers general requirements for electrical installations, including examination and approval of equipment, installations in damp or wet locations, mechanical execution of work, mounting and cooling of equipment, and electrical connections.",
        "content": """<h3>Scope and Purpose</h3><p>Article 110 provides the general requirements for the examination and installation of electrical equipment covered by the NEC. This article lays the groundwork for proper installation practices that apply regardless of the specific type of electrical installation. The requirements in this article help ensure that electrical installations are safe, properly executed, and can be maintained effectively throughout their service life.</p><p>Article 110 is divided into several parts:</p><ul><li>Part I: General requirements applicable to all installations</li><li>Part II: Requirements for installations operating at 1000 volts or less, nominal</li><li>Part III: Requirements for installations operating over 1000 volts, nominal</li><li>Part IV: Tunnel installations over 1000 volts, nominal</li><li>Part V: Manholes and other electric enclosures intended for personnel entry</li></ul><h3>Approval of Equipment and Materials</h3><p><strong>Examination, Identification, and Use of Equipment (110.3):</strong> This section establishes fundamental requirements for evaluating electrical equipment and materials:</p><ul><li>Equipment must be evaluated for suitability before installation</li><li>Examination should consider safety factors such as mechanical strength, electrical insulation, heating effects, and arcing effects</li><li>Equipment must be used or installed according to any instructions included in the listing or labeling</li></ul><p><strong>Listed or Labeled Equipment (110.3(B)):</strong> Equipment that is listed or labeled by a qualified testing laboratory must be installed and used in accordance with instructions included in the listing or labeling. This requirement helps ensure that equipment is properly applied within its design limitations.</p><h3>Workspace and Access Requirements</h3><p><strong>Working Space (110.26):</strong> Clear access and sufficient working space must be provided and maintained around all electrical equipment to permit:</p><ul><li>Ready and safe operation and maintenance of equipment</li><li>Minimum depth of working space ranging from 3 feet to 4 feet, depending on voltage and opposing conditions</li><li>Minimum width of working space of 30 inches or width of equipment, whichever is greater</li><li>Minimum headroom of 6½ feet or the height of equipment, whichever is greater</li></ul><p><strong>Access and Entrance to Working Space (110.26(C)):</strong> For equipment rated 1200 amperes or more and over 6 feet wide, at least one entrance not less than 24 inches wide and 6½ feet high is required. For large equipment, two entrances are often required to provide safe egress.</p><p><strong>Dedicated Equipment Space (110.26(E)):</strong> Electrical equipment such as panelboards and motor control centers requires dedicated space extending from the floor to 6 feet above the equipment or to the structural ceiling, whichever is lower. This space must be kept clear of pipes, ducts, and other equipment foreign to the electrical installation.</p><h3>Installation Requirements</h3><p><strong>Mechanical Execution of Work (110.12):</strong> Electrical equipment must be installed in a neat and workmanlike manner. This includes:</p><ul><li>Proper support and securing of equipment</li><li>Careful routing and bending of conductors</li><li>Proper termination of conductors and cables</li><li>Protection of exposed conductors from physical damage</li></ul><p><strong>Mounting and Cooling of Equipment (110.13):</strong> Electrical equipment must be firmly secured to the surface on which it is mounted. Wooden plugs driven into masonry, concrete, plaster, or similar materials are not considered secure mounting. Equipment that depends on natural cooling must have sufficient airflow and clearance from adjacent equipment to allow heat to dissipate.</p><p><strong>Electrical Connections (110.14):</strong> Proper electrical connections are crucial for safety and reliability:</p><ul><li>Terminals for more than one conductor must be identified for such use</li><li>Conductors must be within the temperature rating of the equipment terminals</li><li>Connections must provide a secure and low-resistance junction</li><li>Connection methods include soldering, welding, pressure connectors, and terminal blocks</li></ul><p><strong>Temperature Limitations (110.14(C)):</strong> The temperature rating associated with a conductor's ampacity must be selected so that it does not exceed the lowest temperature rating of any connected termination, conductor, or device. This is a critical consideration when using conductors with high temperature insulation, such as THHN or XHHW-2.</p><h3>Identification of Circuit Components</h3><p><strong>Identification of Conductors (110.15):</strong> Grounded conductors must be identifiable by white or gray insulation or by three continuous white or gray stripes on other colors. Ungrounded conductors must not use these colors for identification.</p><p><strong>Labeling and Warning Signs (110.16, 110.21):</strong> Various labeling requirements apply to electrical equipment:</p><ul><li>Arc flash warning labels on equipment where examination, adjustment, or maintenance might expose individuals to arc flash hazards</li><li>Field-marked equipment must be marked with the manufacturer's name, trademark, or other descriptive marking</li><li>Warning signs identifying the presence of multiple sources of power</li></ul><p><strong>Identification of Disconnecting Means (110.22):</strong> Each disconnecting means must be legibly marked to indicate its purpose, except where the purpose is evident. Where a circuit's source of power is not immediately evident, placards or directories must be installed at each feeder and branch circuit originated location.</p><h3>Requirements for High-Voltage Installations</h3><p><strong>High-Voltage Installations (110.30-110.41):</strong> For equipment operating over 1000 volts, nominal, additional requirements apply:</p><ul><li>Enhanced working space requirements to accommodate the increased danger</li><li>Specialized enclosures to prevent unauthorized access</li><li>Warning signs indicating high voltage</li><li>Additional guarding of live parts</li><li>Provisions for isolating high-voltage equipment for maintenance</li></ul><p>The high-voltage requirements recognize the increased hazards associated with higher voltage systems and provide additional safeguards for personnel working on or near such systems.</p><h3>Manholes and Underground Installations</h3><p><strong>Manholes and Other Electric Enclosures for Personnel (110.70-110.79):</strong> Special requirements apply to manholes and underground equipment enclosures:</p><ul><li>Sufficient size for safe installation and maintenance of equipment</li><li>Adequate means of entrance and exit</li><li>Provisions for drainage</li><li>Proper ventilation to dissipate heat and harmful gases</li><li>Proper support of cables and conductors</li></ul><p>These requirements help ensure the safety of personnel who must enter underground electrical spaces for installation or maintenance work.</p><h3>Common Code Violations</h3><p><strong>Workspace Violations:</strong> Common violations include:</p><ul><li>Inadequate clearance in front of electrical equipment</li><li>Storage of materials in the dedicated electrical space</li><li>Installation of equipment that blocks required workspace</li><li>Failure to maintain the required headroom</li></ul><p><strong>Connection Issues:</strong> Problems with electrical connections often include:</p><ul><li>Using terminals for multiple conductors when not designed for such use</li><li>Failing to properly torque connections to manufacturer's specifications</li><li>Using conductors with temperature ratings that exceed the terminal rating</li><li>Poor workmanship in making connections</li></ul><p><strong>Identification Problems:</strong> Common violations in this area include:</p><ul><li>Failure to properly identify the purpose of disconnecting means</li><li>Lack of required warning signs or labels</li><li>Improper color-coding of conductors</li></ul><h3>Recent Code Changes</h3><p>Recent editions of the NEC have added or modified requirements in Article 110 related to:</p><ul><li>Enhanced arc flash labeling requirements to better protect workers</li><li>Clarification of workspace requirements for large equipment</li><li>Specific provisions for the assessment of existing equipment when adding, modifying, or renovating installations</li><li>Expanded requirements for reconditioned equipment</li></ul><p>These changes reflect the ongoing effort to improve electrical safety as technology and installation practices evolve.</p><p>Article 110 serves as the foundation for proper electrical installations under the NEC. Its requirements apply to virtually all electrical work and establish the baseline for safety and reliability. Electricians, inspectors, and engineers must thoroughly understand these requirements to ensure that electrical installations meet both the letter and the intent of the code.</p>"""
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
                print(f"NEC article 110 update completed successfully.")
            else:
                print(f"NEC article 110 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
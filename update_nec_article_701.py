import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 701 to the database."""
    # Article data
    article_data = {
        "article_number": "701",
        "title": "Legally Required Standby Systems",
        "summary": "Article 701 covers the electrical safety of the legally required standby power systems, their circuits, and their installation requirements. These systems are intended to automatically supply power to selected loads within specific time limits when the normal electrical supply is interrupted.",
        "content": """<h3>Scope and Purpose</h3><p>Article 701 covers the installation, operation, and maintenance of legally required standby systems. These systems are mandated by municipal, state, federal, or other codes or by governmental agencies having jurisdiction. The primary purpose of legally required standby systems is to provide electric power to aid in firefighting, rescue operations, control of health hazards, and similar emergency operations, though they are not classified as emergency systems covered under Article 700.</p><p>Common applications for legally required standby systems include:</p><ul><li>Smoke control systems and stair pressurization</li><li>Industrial processes where current interruption would produce serious hazards</li><li>Public safety communication systems</li><li>Selected lighting and power circuits in industrial and commercial buildings</li><li>Heating and refrigeration systems in critical facilities</li></ul><p>While Article 700 (Emergency Systems) covers systems that are essential for life safety, Article 701 covers systems that are important but not directly critical to life safety. The distinction is often subtle and depends on the authority having jurisdiction.</p><h3>Equipment Classification</h3><p><strong>Classification (701.2):</strong> The legally required standby systems are classified as:</p><ul><li>Type 10: Systems that can accept the standby load within 10 seconds of normal power loss</li><li>Type 60: Systems that can accept the standby load within 60 seconds of normal power loss</li><li>Type 120: Systems that can accept the standby load within 120 seconds of normal power loss</li></ul><p>The specific classification required depends on the application and the governing codes or regulations.</p><h3>Transfer Equipment</h3><p><strong>Transfer Switch Requirements (701.5):</strong> Transfer equipment must be automatic, identified for standby use, and designed to prevent inadvertent interconnection of normal and standby sources of supply. Transfer switches must be electrically operated and mechanically held, and must be listed for emergency service as a completely factory-assembled and factory-tested apparatus.</p><p><strong>Supply Side Connections (701.5(A)):</strong> The alternate source for legally required standby systems is permitted to supply other equipment, such as optional standby loads, but only after transfer equipment for the legally required loads has operated.</p><p><strong>Operation (701.6):</strong> The operation of transfer equipment must be automatic, ensuring the continuity of legally required systems without manual intervention.</p><h3>Capacity and Rating</h3><p><strong>Capacity and Rating (701.4):</strong> The legally required standby system must have adequate capacity and rating to supply all intended loads simultaneously. The system must be permitted to supply legally required standby and optional standby systems where automatic selective load pickup and load shedding is provided to ensure adequate power to the legally required standby circuits.</p><p><strong>Selective Load Pickup (701.4):</strong> When automatic load control is provided, the system must be designed so that if a failure occurs within the system, the legally required loads are given priority over optional standby loads.</p><p><strong>Signs (701.7):</strong> A sign must be placed at the service entrance equipment indicating the type and location of on-site legally required standby power sources, or a sign at the grounding location shall indicate the type and location of any standby power sources.</p><h3>Circuit Wiring</h3><p><strong>Wiring (701.10):</strong> Wiring from the alternate source to legally required standby equipment must be kept entirely independent of all other wiring and equipment, except:</p><ul><li>In transfer equipment enclosures</li><li>In exit or emergency lighting fixtures supplied from two sources</li><li>In a common junction box attached to exit or emergency lighting fixtures supplied from two sources</li><li>When two or more legally required circuits supply the same equipment</li></ul><p><strong>Protection Against Physical Damage (701.10(B)):</strong> Legally required standby circuits must be designed and located to minimize the risk of damage from material handling, flooding, or other environmental conditions.</p><p><strong>Fire Protection (701.10(C)):</strong> Circuits for legally required standby systems must meet specific criteria for increased fire resistance when they must continue to operate in a fire. This typically involves routing through areas with low fire risk or using fire-rated assemblies.</p><h3>Power Sources</h3><p><strong>Legally Required Standby Power Sources (701.12):</strong> The power source for legally required standby systems can be any of the following:</p><ul><li>Storage batteries (subject to specific capacity requirements and charging means)</li><li>Generator set (internal combustion engine, microturbine, or fuel cell powered)</li><li>Uninterruptible power supply (UPS)</li><li>Separate service (when approved by the authority having jurisdiction)</li></ul><p><strong>Generator Requirements (701.12(B)):</strong> When an engine-driven generator is used as the power source, it must be:</p><ul><li>Of sufficient capacity to carry the load</li><li>Equipped with appropriate means for automatically starting the prime mover upon failure of the normal service</li><li>Capable of providing power within the specified timeframe (10, 60, or 120 seconds)</li><li>Provided with a permanent weatherproof housing or suitable protection if installed outdoors</li></ul><p><strong>Fuel Supply (701.12(B)(2)):</strong> When internal combustion engines are used as the prime mover, an on-site fuel supply must be provided, with sufficient capacity to operate the system at full demand for a minimum of 2 hours.</p><h3>Control and Protection</h3><p><strong>Ground-Fault Protection of Equipment (701.26):</strong> The alternate source for legally required standby systems is not required to have ground-fault protection of equipment with automatic disconnecting means. Ground-fault indication of the legally required standby source is required.</p><p><strong>Selective Coordination (701.27):</strong> Overcurrent protective devices serving legally required standby systems must be selectively coordinated with all supply-side overcurrent protective devices. This means that a fault at any point in the system should be cleared by the nearest upstream protective device, limiting the extent of the outage.</p><h3>Testing and Maintenance</h3><p><strong>Testing and Maintenance (701.3):</strong> Legally required standby systems must be tested periodically to ensure operational readiness. This includes:</p><ul><li>Initial acceptance testing of the complete system</li><li>Periodic testing (often monthly) under load conditions</li><li>Annual testing for a minimum of 4 hours under load</li><li>Written records of testing and maintenance</li></ul><p>The legally required standby system equipment must be maintained in accordance with manufacturer instructions and industry standards.</p><h3>Application and Compliance Considerations</h3><p><strong>Identification (701.9):</strong> All boxes and enclosures for legally required standby circuits must be permanently marked to identify them as components of the legally required standby system. Junction boxes, pull boxes, and similar enclosures are typically identified with distinctive coloring, labeling, or both.</p><p><strong>Coordination with Other Codes (701.3(A)):</strong> Legally required standby systems must comply with relevant requirements from other applicable codes, such as:</p><ul><li>NFPA 110: Standard for Emergency and Standby Power Systems</li><li>NFPA 111: Standard on Stored Electrical Energy Emergency and Standby Power Systems</li><li>Local building codes</li><li>Specific requirements from the authority having jurisdiction</li></ul><p><strong>Common Compliance Issues:</strong></p><ul><li>Inadequate separation of legally required standby circuits from normal power circuits</li><li>Insufficient fuel supply for generator-driven systems</li><li>Lack of proper testing and maintenance documentation</li><li>Failure to properly identify components of the legally required standby system</li><li>Insufficient selective coordination of overcurrent devices</li></ul><p>Legally required standby systems represent a critical component of building safety systems, serving as a middle tier between the critical emergency systems of Article 700 and the optional standby systems of Article 702. Proper design, installation, and maintenance of these systems is essential to ensure they perform as required during power outages.</p>"""
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
                print(f"NEC article 701 update completed successfully.")
            else:
                print(f"NEC article 701 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
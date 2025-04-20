import sys
import os
from flask import Flask

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import app factory and db
from circuit_breaker_app import create_app, db
from circuit_breaker_app.models import NECArticle

def update_nec_articles():
    """Update or add NEC articles to the database."""
    # List of updated NEC articles
    updated_articles = [
        {
            "article_number": "90",
            "title": "Introduction",
            "summary": "Purpose and scope of the NEC",
            "content": "<h3>Article 90: Introduction</h3><p>This article establishes the purpose and scope of the National Electrical Code (NEC), setting forth the fundamental principles that govern its application.</p><h4>Key Provisions:</h4><ul><li><strong>90.1 Purpose:</strong> The NEC is designed to provide practical safeguarding of persons and property from hazards arising from the use of electricity.</li><li><strong>90.2 Scope:</strong> Specifies what installations are covered by the NEC and which ones are not.</li><li><strong>90.3 Code Arrangement:</strong> Explains how the code is structured, with general rules and specific requirements.</li><li><strong>90.4 Enforcement:</strong> Addresses the authority having jurisdiction (AHJ) and their role in enforcing the code.</li><li><strong>90.5 Mandatory Rules and Explanatory Material:</strong> Distinguishes between mandatory requirements and advisory information.</li><li><strong>90.6 Formal Interpretations:</strong> Outlines the process for obtaining official interpretations of code requirements.</li><li><strong>90.7 Examination of Equipment for Safety:</strong> Discusses product testing, listing, and approval.</li><li><strong>90.8 Wiring Planning:</strong> Encourages planning for future expansion and changes in electrical systems.</li><li><strong>90.9 Units of Measurement:</strong> Specifies the use of metric and inch-pound units in the code.</li></ul>"
        },
        {
            "article_number": "100",
            "title": "Definitions",
            "summary": "Essential definitions used throughout the code",
            "content": "<h3>Article 100: Definitions</h3><p>This article contains definitions essential to the proper application of the NEC. These definitions establish the precise meaning of terms used throughout the code.</p><h4>Key Definitions:</h4><ul><li><strong>Accessible:</strong> Capable of being reached for operation, renewal, or inspection without requiring actions such as removing obstacles or using ladders.</li><li><strong>Ampacity:</strong> The maximum current, in amperes, that a conductor can carry continuously under specified conditions.</li><li><strong>Branch Circuit:</strong> The circuit conductors between the final overcurrent device protecting the circuit and the outlet(s).</li><li><strong>Circuit Breaker:</strong> A device designed to open and close a circuit by nonautomatic means and to open the circuit automatically on a predetermined overcurrent.</li><li><strong>Dwelling Unit:</strong> A single unit providing complete and independent living facilities for one or more persons, including permanent provisions for living, sleeping, cooking, and sanitation.</li><li><strong>Feeder:</strong> All circuit conductors between the service equipment, the source of a separate derived system, or other power supply source and the final branch-circuit overcurrent device.</li><li><strong>Ground:</strong> A conducting connection, whether intentional or accidental, between an electrical circuit or equipment and the earth.</li><li><strong>Grounded Conductor:</strong> A system or circuit conductor that is intentionally grounded.</li><li><strong>Grounding Conductor:</strong> A conductor used to connect equipment or the grounded circuit of a wiring system to a grounding electrode or electrodes.</li><li><strong>Listed:</strong> Equipment, materials, or services included in a list published by an organization that is acceptable to the authority having jurisdiction.</li><li><strong>Raceway:</strong> An enclosed channel of metallic or nonmetallic materials designed expressly for holding wires, cables, or busbars.</li><li><strong>Service:</strong> The conductors and equipment for delivering electric energy from the serving utility to the wiring system of the premises served.</li><li><strong>Voltage:</strong> The greatest root-mean-square (rms) difference of potential between any two conductors of the circuit concerned.</li></ul>"
        },
        {
            "article_number": "110",
            "title": "Requirements for Electrical Installations",
            "summary": "General requirements for electrical installations",
            "content": "<h3>Article 110: Requirements for Electrical Installations</h3><p>This article covers general requirements for electrical installations, setting the foundation for specific requirements in other articles.</p><h4>Key Provisions:</h4><ul><li><strong>110.2 Approval:</strong> Conductors and equipment must be acceptable only if approved by the authority having jurisdiction.</li><li><strong>110.3 Examination, Identification, and Use of Equipment:</strong> Guidelines for examining and evaluating electrical equipment for safety.</li><li><strong>110.7 Wiring Integrity:</strong> Completed wiring installations must be free from short circuits, ground faults, or any connections other than those intended.</li><li><strong>110.11 Deteriorating Agents:</strong> Equipment must be suitable for installation in environments where exposed to destructive agents.</li><li><strong>110.12 Mechanical Execution of Work:</strong> Electrical equipment must be installed in a neat and workmanlike manner.</li><li><strong>110.13 Mounting and Cooling of Equipment:</strong> Requirements for securing equipment and ensuring proper cooling.</li><li><strong>110.14 Electrical Connections:</strong> Specific requirements for making electrical connections to ensure conductivity and mechanical security.</li><li><strong>110.16 Arc-Flash Hazard Warning:</strong> Requirements for labeling equipment that may be worked on while energized.</li><li><strong>110.21 Marking:</strong> Equipment must be marked with the manufacturer's name, trademark, or other descriptive marking.</li><li><strong>110.22 Identification of Disconnecting Means:</strong> Each disconnecting means must be legibly marked to indicate its purpose.</li><li><strong>110.26 Spaces About Electrical Equipment:</strong> Specific clearance requirements for access and working space around electrical equipment.</li><li><strong>110.27 Guarding of Live Parts:</strong> Live parts operating at 50 volts or more must be guarded against accidental contact.</li></ul>"
        },
        {
            "article_number": "200",
            "title": "Use and Identification of Grounded Conductors",
            "summary": "Requirements for identifying and using grounded conductors",
            "content": "<h3>Article 200: Use and Identification of Grounded Conductors</h3><p>This article covers the identification and use of grounded conductors in electrical systems.</p><h4>Key Provisions:</h4><ul><li><strong>200.1 Scope:</strong> This article provides requirements for identification of terminals and use of grounded conductors.</li><li><strong>200.2 General:</strong> Grounded conductors must be identified according to the requirements of this article.</li><li><strong>200.3 Connection to Grounded System:</strong> Premises wiring shall not be electrically connected to a supply system unless the latter contains a grounded conductor.</li><li><strong>200.6 Means of Identifying Grounded Conductors:</strong> Specifies how grounded conductors must be identified by color (white or gray) or by other approved means.</li><li><strong>200.7 Use of Insulation of a White or Gray Color or with Three Continuous White or Gray Stripes:</strong> Restricts the use of white or gray insulated conductors to grounded conductors only, with specific exceptions.</li><li><strong>200.9 Means of Identification of Terminals:</strong> Describes how terminals for grounded conductors must be identified in devices and equipment.</li><li><strong>200.10 Identification of Terminals:</strong> Provides specific requirements for identification of terminals in devices such as receptacles, plugs, and connectors.</li><li><strong>200.11 Polarity of Connections:</strong> Requires that polarized connections for current-carrying conductors be made in a uniform manner.</li></ul>"
        },
        {
            "article_number": "210",
            "title": "Branch Circuits",
            "summary": "Requirements for branch circuits including rating and overcurrent protection",
            "content": "<h3>Article 210: Branch Circuits</h3><p>This article covers branch circuits, including their rating, required outlets, and specific load requirements for various occupancies.</p><h4>Key Provisions:</h4><ul><li><strong>210.3 Rating:</strong> Branch circuits are rated according to the rating of the overcurrent device protecting the circuit.</li><li><strong>210.4 Multiwire Branch Circuits:</strong> Specific requirements for circuits that consist of two or more ungrounded conductors with a common neutral.</li><li><strong>210.5 Identification for Branch Circuits:</strong> Requirements for identifying conductors for branch circuits.</li><li><strong>210.8 Ground-Fault Circuit-Interrupter Protection for Personnel:</strong> Locations where GFCI protection is required, such as bathrooms, kitchens, and outdoor receptacles.</li><li><strong>210.11 Branch Circuits Required:</strong> General provisions for the minimum number of branch circuits required.</li><li><strong>210.12 Arc-Fault Circuit-Interrupter Protection:</strong> Locations where AFCI protection is required, primarily in dwelling units.</li><li><strong>210.19 Conductors — Minimum Ampacity and Size:</strong> Requirements for sizing branch circuit conductors.</li><li><strong>210.20 Overcurrent Protection:</strong> Requirements for protecting branch circuits against overcurrent.</li><li><strong>210.21 Outlet Devices:</strong> Requirements for the rating of outlet devices on branch circuits.</li><li><strong>210.23 Permissible Loads, Individual Branch Circuits:</strong> Limitations on the types of loads that can be connected to various branch circuits.</li><li><strong>210.25 Branch Circuits in Buildings with More Than One Occupancy:</strong> Requirements for separating branch circuits serving different occupancies.</li><li><strong>210.52 Dwelling Unit Receptacle Outlets:</strong> Specific requirements for the placement and spacing of receptacles in dwelling units.</li><li><strong>210.63 Heating, Air-Conditioning, and Refrigeration Equipment Outlet:</strong> Requirements for receptacles near such equipment to facilitate servicing.</li><li><strong>210.70 Lighting Outlets Required:</strong> Requirements for the placement of lighting outlets in various spaces.</li></ul>"
        },
        {
            "article_number": "215",
            "title": "Feeders",
            "summary": "Requirements for feeders, including sizing and overcurrent protection",
            "content": "<h3>Article 215: Feeders</h3><p>This article covers the installation requirements, minimum size, and ampacity of conductors for feeders supplying branch-circuit loads.</p><h4>Key Provisions:</h4><ul><li><strong>215.1 Scope:</strong> This article covers the installation requirements, minimum size, and ampacity of conductors for feeders.</li><li><strong>215.2 Minimum Rating and Size:</strong> Feeder conductors shall have an ampacity not less than required to supply the load as calculated in Parts III, IV, and V of Article 220.</li><li><strong>215.3 Overcurrent Protection:</strong> Feeders shall be protected against overcurrent in accordance with Part I of Article 240.</li><li><strong>215.4 Feeders with Common Neutral Conductor:</strong> Specific requirements for feeders that consist of multiple ungrounded conductors sharing a common neutral.</li><li><strong>215.5 Diagrams of Feeders:</strong> If required by the authority having jurisdiction, a diagram showing feeder details shall be provided prior to installation.</li><li><strong>215.6 Feeder Conductor Grounding Means:</strong> Requirements for grounding means for feeder circuits.</li><li><strong>215.7 Ungrounded Conductors Tapped from Grounded Systems:</strong> Requirements for ungrounded conductors tapped from the grounded conductor of a system where the system has a grounded neutral.</li><li><strong>215.9 Ground-Fault Circuit-Interrupter Protection for Personnel:</strong> Requirements for GFCI protection on feeders.</li><li><strong>215.10 Ground-Fault Protection of Equipment:</strong> Requirements for ground-fault protection of equipment on solidly grounded wye electrical services of more than 150 volts to ground but not exceeding 1000 volts phase-to-phase for each service disconnect rated 1000 amperes or more.</li><li><strong>215.11 Circuits Derived from Autotransformers:</strong> Requirements for feeders supplied from autotransformers.</li><li><strong>215.12 Identification for Feeders:</strong> Requirements for identifying conductors for feeders.</li></ul>"
        },
        {
            "article_number": "240",
            "title": "Overcurrent Protection",
            "summary": "Requirements for overcurrent protection for conductors and equipment",
            "content": "<h3>Article 240: Overcurrent Protection</h3><p>This article provides the requirements for overcurrent protection and overcurrent protective devices for conductors and equipment.</p><h4>Key Provisions:</h4><ul><li><strong>240.1 Scope:</strong> This article provides the requirements for overcurrent protection and overcurrent protective devices.</li><li><strong>240.4 Protection of Conductors:</strong> Conductors, other than flexible cords, flexible cables, and fixture wires, shall be protected against overcurrent in accordance with their ampacities specified in 310.15.</li><li><strong>240.6 Standard Ampere Ratings:</strong> The standard ampere ratings for fuses and inverse time circuit breakers.</li><li><strong>240.8 Fuses or Circuit Breakers in Parallel:</strong> Fuses and circuit breakers shall be permitted to be connected in parallel where they are factory assembled in parallel and listed as a unit.</li><li><strong>240.12 Electrical System Coordination:</strong> Where an orderly shutdown is required to minimize the hazard(s) to personnel and equipment, a system of coordination based on the following two conditions shall be permitted.</li><li><strong>240.15 Ungrounded Conductors:</strong> Each ungrounded conductor shall be protected by an overcurrent device in series with the conductor.</li><li><strong>240.21 Location in Circuit:</strong> Overcurrent protection shall be provided in each ungrounded circuit conductor and shall be located at the point where the conductors receive their supply.</li><li><strong>240.24 Location in or on Premises:</strong> Overcurrent devices shall be readily accessible and installed so that the center of the grip of the operating handle of the switch or circuit breaker, when in its highest position, is not more than 2.0 m (6 ft 7 in.) above the floor or working platform.</li><li><strong>240.50 Plug Fuses:</strong> Requirements for plug fuses and fuseholders.</li><li><strong>240.60 Cartridge Fuses and Fuseholders:</strong> Requirements for cartridge fuses and fuseholders.</li><li><strong>240.80 Method of Operation:</strong> Circuit breakers shall be trip free and capable of being closed and opened by manual operation.</li><li><strong>240.83 Marking:</strong> Circuit breakers shall be durably marked with specific information.</li><li><strong>240.85 Applications:</strong> A circuit breaker with a straight voltage rating shall be permitted to be applied in a circuit in which the nominal voltage between any two conductors does not exceed the circuit breaker's voltage rating.</li></ul>"
        }
    ]
    
    # Track statistics
    added_count = 0
    updated_count = 0
    skipped_count = 0
    
    try:
        # Process each article
        for article_data in updated_articles:
            # Check if article exists
            existing_article = NECArticle.query.filter_by(
                article_number=article_data['article_number']
            ).first()
            
            if existing_article:
                # Update existing article
                existing_article.title = article_data['title']
                existing_article.summary = article_data['summary']
                existing_article.content = article_data['content']
                updated_count += 1
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
                added_count += 1
                print(f"Added Article {article_data['article_number']}: {article_data['title']}")
        
        # Commit changes
        db.session.commit()
        
        print(f"\nNEC Article Update Summary:")
        print(f"Articles added: {added_count}")
        print(f"Articles updated: {updated_count}")
        print(f"Articles skipped: {skipped_count}")
        print(f"Total processed: {added_count + updated_count + skipped_count}")
        
        return True
        
    except Exception as e:
        db.session.rollback()
        print(f"Error updating NEC articles: {str(e)}")
        return False

def main():
    """Create app context and run the update function."""
    try:
        app = create_app()
        with app.app_context():
            success = update_nec_articles()
            if success:
                print("NEC article update completed successfully.")
            else:
                print("NEC article update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
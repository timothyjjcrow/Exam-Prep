import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 625 to the database."""
    article_data = {
        "article_number": "625",
        "title": "Electric Vehicle Charging Systems",
        "summary": "Requirements for the installation of electric vehicle supply equipment (EVSE), including safety provisions, wiring methods, marking, and specific requirements for various charging levels and locations.",
        "content": """
<h3>Scope and Overview</h3>
<p>Article 625 covers the electrical conductors and equipment external to an electric vehicle (EV) that connect it to a supply of electricity for charging, power export, or bidirectional current flow, as well as the installation of equipment and devices related to EV charging. This article has grown in importance with the rapid adoption of electric vehicles and continues to evolve with charging technology advancements.</p>

<h3>Key Definitions (625.2)</h3>
<ul>
    <li><strong>Electric Vehicle (EV):</strong> An automotive-type vehicle for highway use that includes an electric motor and is powered by an external source of electricity or by a battery.</li>
    <li><strong>Electric Vehicle Supply Equipment (EVSE):</strong> The conductors, including the ungrounded, grounded, and equipment grounding conductors, the electric vehicle connectors, attachment plugs, and all other fittings, devices, power outlets, or apparatus installed specifically for the purpose of transferring energy between the premises wiring and the electric vehicle.</li>
    <li><strong>Wireless Power Transfer Equipment (WPTE):</strong> Equipment that transfers electrical energy from a power transmitter to a power receiver without physical electrical connection.</li>
    <li><strong>Bidirectional Electric Vehicle (BEV):</strong> An EV capable of both receiving energy from and supplying energy to the premises wiring system.</li>
    <li><strong>Charging Levels:</strong> Various levels of EV charging based on voltage and current ratings:
        <ul>
            <li><strong>Level 1:</strong> 120VAC, up to 16A (typically 1.4-1.9 kW)</li>
            <li><strong>Level 2:</strong> 208-240VAC, up to 80A (typically 3.3-19.2 kW)</li>
            <li><strong>Level 3/DC Fast Charging:</strong> High-voltage DC power (typically 50-350+ kW)</li>
        </ul>
    </li>
</ul>

<h3>General Requirements</h3>

<p><strong>625.4 Voltages:</strong> Equipment covered by this article shall be rated at nominal system voltages in accordance with 110.4.</p>

<p><strong>625.5 Listed or Labeled:</strong> All electrical materials, devices, fittings, and associated equipment shall be listed or labeled for the intended use.</p>

<p><strong>625.10 Electric Vehicle Coupler:</strong> The EV coupler shall comply with specific requirements:</p>
<ul>
    <li>It must be polarized unless part of a listed EV supply equipment.</li>
    <li>It must be non-interchangeable with other electrical connectors in the installation.</li>
    <li>It must be constructed to minimize the possibility of a shock hazard.</li>
    <li>No connector part that may be touched during charging can be energized when exposed.</li>
    <li>It must be designed to prevent unintentional disconnection during charging.</li>
</ul>

<h3>Equipment Construction</h3>

<p><strong>625.15 Markings:</strong> EVSE shall clearly indicate:</p>
<ul>
    <li>Maximum current ratings, voltage, and frequency</li>
    <li>Whether it's for indoor or outdoor use (or both)</li>
    <li>Ventilation requirements if battery charging requires ventilation</li>
    <li>Instructions or diagrams for proper connection of the electric vehicle</li>
</ul>

<p><strong>625.17 Cable Management System:</strong> EVSE shall be provided with a means to manage the output cable, such as retractors or cable hangers, to protect the cable from damage and prevent strain at the connection points.</p>

<p><strong>625.18 Interlock:</strong> EVSE shall be provided with an interlock that de-energizes the EV connector when it's uncoupled from the vehicle.</p>

<p><strong>625.19 Automatic De-energization of Cable:</strong> The EVSE or the cable-connector combination shall be designed such that the cable conductors are de-energized if there's a strain that could rupture the cable or separate the cable from the connector.</p>

<p><strong>625.22 Personnel Protection System:</strong> The EVSE shall have a system of protection against electric shock that includes:
<ul>
    <li>A listed personnel protection system (such as GFCI)</li>
    <li>A listed system that verifies the connection of the equipment grounding conductor</li>
</ul>

<h3>Installation Requirements</h3>

<p><strong>625.40 Electric Vehicle Branch Circuit:</strong> Each outlet installed for charging EVs shall be supplied by an individual branch circuit that supplies no other loads, except for ventilation equipment as specified.</p>

<p><strong>625.41 Overcurrent Protection:</strong> Overcurrent protection for circuits supplying EVSE shall be sized for continuous duty and shall have a rating of not less than 125% of the maximum load of the EVSE.</p>

<p><strong>625.42 Rating:</strong> EVSE shall have sufficient rating to supply the load. The EVSE load shall be considered continuous (3 hours or more of operation).</p>

<p><strong>625.43 Disconnecting Means:</strong> For EVSE rated more than 60 amperes or more than 150 volts to ground, a disconnecting means shall be provided and installed in a readily accessible location and shall be lockable in the open position.</p>

<p><strong>625.44 EVSE Connection to Other Systems:</strong> Requirements for how EVSE can connect to electrical systems:</p>
<ul>
    <li><strong>Interactive Systems:</strong> EVSE that incorporate bidirectional current flow shall comply with Article 705 (Interconnected Electric Power Production Sources).</li>
    <li><strong>Energy Management Systems:</strong> If used, must comply with Article 750.</li>
</ul>

<p><strong>625.48 Interactive Systems:</strong> EVs capable of bidirectional current flow shall comply with the requirements of 625.48 through 625.54.</p>

<p><strong>625.50 Supply Equipment:</strong> Interactive EVs shall only operate through equipment with the specific function of supplying or taking power from the vehicle.</p>

<p><strong>625.52 Loss of Primary Source:</strong> Means shall be provided to prevent power from being exported to the premises wiring system when the primary source is de-energized (anti-islanding protection).</p>

<p><strong>625.54 Power Export Equipment:</strong> Hardware and software utilized for power export shall be compatible with the connected EV.</p>

<h3>Wiring Methods</h3>

<p><strong>625.30 Wiring Systems:</strong> All wiring methods for circuits supplying EVSE shall comply with the relevant articles of Chapter 3 of the NEC, with additional requirements:
<ul>
    <li>The wiring method must be suitable for the environment (indoor/outdoor)</li>
    <li>EVSE wiring must have adequate physical protection against damage</li>
    <li>If installed where subject to physical damage, adequate protection must be provided</li>
</ul>

<p><strong>625.44 Methods of Connection:</strong> EVSE can be connected to the premises wiring via:</p>
<ul>
    <li>Permanent wiring methods covered in Chapter 3</li>
    <li>Cord-and-plug connection (with specific requirements based on rating)</li>
    <li>Power supply cords for portable equipment (with length limitations)</li>
</ul>

<h3>Specific Requirements for Different Charging Types</h3>

<p><strong>625.60 AC Receptacle Outlets Used for EVSE:</strong> Requirements for using standard receptacles for EV charging:</p>
<ul>
    <li>A receptacle must be located to allow a cord of 25 ft or less</li>
    <li>Specific requirements for various ampacity levels</li>
    <li>GFCI protection requirements for certain installations</li>
</ul>

<p><strong>625.62 through 625.65 Wireless Power Transfer:</strong> Requirements for wireless charging systems:</p>
<ul>
    <li>Installation requirements to minimize hazards</li>
    <li>Specific provisions for mounting and alignment</li>
    <li>Protection against physical damage</li>
    <li>Requirements for installation in specific locations (garages, repair facilities, etc.)</li>
</ul>

<h3>Location and Installation Requirements</h3>

<p><strong>625.46 Loss of Primary Source:</strong> Means shall be provided to prevent current flow from the EVSE to the premises wiring when the primary source is de-energized.</p>

<p><strong>625.47 Multiple Feeders:</strong> Where EVSE is supplied by more than one source (for redundancy or power-level selection), interconnection requirements must be observed.</p>

<p><strong>625.50 Location:</strong> EVSE shall be installed in accordance with its listing and:
<ul>
    <li>Indoor locations shall have ventilation when required for the type of battery being charged</li>
    <li>Outdoor installations must be suitable for outdoor use</li>
    <li>EVSE shall not be installed in hazardous (classified) locations unless specifically designed and listed for such use</li>
</ul>

<p><strong>625.52 Ventilation:</strong> Where ventilation is required (for certain battery types):
<ul>
    <li>The ventilation system shall be interlocked with the EVSE</li>
    <li>Specific ventilation rates based on the size and number of vehicles</li>
    <li>Mechanical ventilation requirements and controls</li>
</ul>

<h3>Common Installation Issues and Practical Applications</h3>

<p><strong>Common Issues:</strong></p>
<ul>
    <li><strong>Inadequate Circuit Sizing:</strong> Not accounting for the continuous duty rating (125% factor) for branch circuits feeding EVSE.</li>
    <li><strong>Improper Mounting:</strong> EVSE not securely mounted or positioned where subject to physical damage.</li>
    <li><strong>Missing Disconnects:</strong> Not providing required disconnecting means for higher-rated equipment.</li>
    <li><strong>Ventilation Issues:</strong> Not providing or interlocking required ventilation for certain battery types.</li>
    <li><strong>Cable Management:</strong> Inadequate protection of charging cables against physical damage or strain.</li>
    <li><strong>Receptacle Distance:</strong> Installing receptacles too far from parking spaces, requiring extension cords.</li>
    <li><strong>Lack of GFCI Protection:</strong> Missing required personnel protection systems.</li>
    <li><strong>Clearance Issues:</strong> Not providing adequate working clearances for EVSE as required by 110.26.</li>
</ul>

<p><strong>Practical Application:</strong></p>
<ul>
    <li><strong>Load Calculations:</strong> When adding EVSE to existing properties, perform load calculations to ensure service capacity.</li>
    <li><strong>Future Planning:</strong> Consider installing conduit and service capacity for future EVSE installations.</li>
    <li><strong>Commercial Installations:</strong> Commercial EVSE often requires specialized design considerations for power management, billing systems, and accessibility.</li>
    <li><strong>Residential Considerations:</strong> For residences, consider the most appropriate connection method based on usage patterns and electrical service capacity.</li>
    <li><strong>Energy Management:</strong> Modern installations often include load management systems to prevent service overloads when multiple EVs are charging simultaneously.</li>
    <li><strong>Bidirectional Considerations:</strong> Vehicle-to-grid (V2G) or vehicle-to-home (V2H) systems require careful design to meet Article 705 requirements.</li>
</ul>

<h3>Recent Code Changes</h3>
<p>Recent updates to Article 625 have included:</p>
<ul>
    <li>Expanded provisions for bidirectional power flow from EVs (vehicle-to-grid/home)</li>
    <li>Enhanced requirements for wireless power transfer equipment</li>
    <li>Updated load calculation methods for multiple charging stations</li>
    <li>New provisions for energy management systems to enable smart charging</li>
    <li>Clarified requirements for EVSE in various locations (parking garages, dwellings, etc.)</li>
    <li>Additional safety requirements for DC fast charging equipment</li>
</ul>

<p>As electric vehicle adoption continues to accelerate, Article 625 remains one of the most rapidly evolving sections of the NEC, with each code cycle bringing significant updates to address new technologies and installation practices.</p>
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
                print(f"NEC article 625 update completed successfully.")
            else:
                print(f"NEC article 625 update failed.")
    except Exception as e:
        print(f"Error updating NEC article 625: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
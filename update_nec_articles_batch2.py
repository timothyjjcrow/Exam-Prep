import sys
import os
from flask import Flask

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import app factory and db
from circuit_breaker_app import create_app, db
from circuit_breaker_app.models import NECArticle

def update_nec_articles_batch2():
    """Update or add NEC articles to the database (second batch)."""
    # List of updated NEC articles
    updated_articles = [
        {
            "article_number": "220",
            "title": "Branch-Circuit, Feeder, and Service Load Calculations",
            "summary": "Provides requirements for calculating branch-circuit, feeder, and service loads.",
            "content": """<h2>Article 220: Branch-Circuit, Feeder, and Service Load Calculations</h2>
            <p>This article provides requirements for calculating branch-circuit, feeder, and service loads. It includes methods for calculating minimum load requirements for various installation types.</p>
            
            <h3>220.3 Application of Other Articles</h3>
            <p>Load calculations must comply with other applicable articles in the Code for specific occupancies or equipment.</p>
            
            <h3>220.5 Calculations</h3>
            <p>Calculations shall be permitted to be rounded to the nearest ampere, volt, or volt-ampere. Voltage drop must be in accordance with 210.19(A) for branch circuits and 215.2(A) for feeders.</p>
            
            <h3>220.12 Lighting Load for Specified Occupancies</h3>
            <p>General lighting loads must be calculated at a minimum of the unit load per area specified in Table 220.12, multiplied by the area involved. These unit loads account for general lighting plus receptacle loads.</p>
            <p>For example:</p>
            <ul>
                <li>Dwelling units: 3 VA per square foot</li>
                <li>Hospitals: 2 VA per square foot</li>
                <li>Hotels and motels: 2 VA per square foot</li>
                <li>Warehouses: 0.25 VA per square foot</li>
            </ul>
            
            <h3>220.14 Other Loads — All Occupancies</h3>
            <p>The minimum load for each receptacle outlet in occupancies other than dwelling units shall be calculated based on their intended use.</p>
            <ul>
                <li>For receptacles of general use, calculate a minimum of 180 VA per receptacle outlet</li>
                <li>For fixed multi-outlet assemblies, calculate a minimum of 180 VA for each 5 feet or fraction thereof</li>
            </ul>
            
            <h3>220.18 Maximum Loads</h3>
            <p>The total load shall not exceed the rating of the branch circuit, and it shall not exceed the maximum loads specified in 220.18(A) through (C) under the conditions specified.</p>
            
            <h3>220.40 General (Feeder and Service Calculations)</h3>
            <p>The calculated load of a feeder or service shall not be less than the sum of the loads on the branch circuits supplied, after any applicable demand factors have been applied.</p>
            
            <h3>220.42 General Lighting</h3>
            <p>The demand factors specified in Table 220.42 shall apply to the portion of the total branch-circuit load calculated for general illumination.</p>
            
            <h3>220.50 Motors</h3>
            <p>Motor loads shall be calculated in accordance with 430.24, 430.25, and 430.26, and with 440.6 for hermetic refrigerant motor-compressors.</p>
            
            <h3>220.51 Fixed Electric Space Heating</h3>
            <p>Fixed electric space heating loads shall be calculated at 100 percent of the total connected load. However, in no case shall a feeder or service load current rating be less than the rating of the largest branch circuit supplied.</p>
            
            <h3>Part III: Optional Calculations for Computing Feeder and Service Loads</h3>
            <p>This part provides optional methods for calculating residential feeder and service loads, which may result in lower load calculations than the standard method in Part II.</p>
            
            <h3>Part IV: Method for Computing Farm Loads</h3>
            <p>This part provides a method for calculating farm loads, recognizing the diversity of loads in agricultural settings.</p>"""
        },
        {
            "article_number": "225",
            "title": "Outside Branch Circuits and Feeders",
            "summary": "Covers requirements for outside branch circuits and feeders run on or between buildings, structures, or poles.",
            "content": """<h2>Article 225: Outside Branch Circuits and Feeders</h2>
            <p>This article covers requirements for outside branch circuits and feeders run on or between buildings, structures, or poles on the premises.</p>
            
            <h3>225.4 Conductor Covering</h3>
            <p>Where within 3.0 m (10 ft) of grade level, conductors shall be protected by conduit, cable trays, or other approved means.</p>
            
            <h3>225.6 Conductor Size and Support</h3>
            <p>Overhead conductors for outside branch circuits and feeders must be sized as follows:</p>
            <ul>
                <li>For 600 volts or less, not less than 10 AWG copper or 8 AWG aluminum for spans up to 50 feet</li>
                <li>For spans exceeding 50 feet, conductor sizes must be increased</li>
            </ul>
            
            <h3>225.10 Wiring on Buildings</h3>
            <p>Conductors must be securely attached to the building surface and protected against physical damage where necessary.</p>
            
            <h3>225.18 Clearance from Ground</h3>
            <p>Overhead conductors must maintain minimum clearances from ground:</p>
            <ul>
                <li>10 feet above finished grade, sidewalks, or platforms from which they might be accessible to pedestrians</li>
                <li>12 feet over residential property and driveways</li>
                <li>18 feet over public streets, alleys, roads, parking areas subject to truck traffic</li>
            </ul>
            
            <h3>225.19 Clearances from Buildings</h3>
            <p>Conductors must maintain specific clearances from buildings for fire safety and to prevent accidental contact:</p>
            <ul>
                <li>3 feet from windows, doors, porches, fire escapes, or similar locations</li>
                <li>Conductors run above the top level of a window shall be at least 3 feet from the window</li>
            </ul>
            
            <h3>225.30 Number of Supplies</h3>
            <p>A building or structure shall be supplied by only one feeder or branch circuit except as permitted in 225.30(A) through (F), which include provisions for special conditions, capacity requirements, and different characteristics.</p>
            
            <h3>225.31 Disconnecting Means</h3>
            <p>Means shall be provided for disconnecting all ungrounded conductors that supply or pass through the building or structure from the source of supply.</p>
            
            <h3>225.32 Location</h3>
            <p>The disconnecting means shall be installed either inside or outside the building or structure served, at a readily accessible location nearest the point of entrance of the supply conductors.</p>
            
            <h3>225.33 Maximum Number of Disconnects</h3>
            <p>The disconnecting means shall consist of not more than six switches or six circuit breakers mounted in a single enclosure, in a group of separate enclosures, or in or on a switchboard or switchgear.</p>
            
            <h3>225.36 Suitable for Service Equipment</h3>
            <p>The disconnecting means specified in 225.31 shall be suitable for use as service equipment.</p>
            
            <h3>225.39 Rating of Disconnect</h3>
            <p>The disconnecting means shall have a rating not less than the calculated load to be supplied, determined in accordance with Parts I and II of Article 220 for branch circuits, Part III or IV of Article 220 for feeders, or Part V of Article 220 for farm loads.</p>"""
        },
        {
            "article_number": "230",
            "title": "Services",
            "summary": "Covers service conductors and equipment for control and protection of services and their installation requirements.",
            "content": """<h2>Article 230: Services</h2>
            <p>This article covers service conductors and equipment for control and protection of services and their installation requirements.</p>
            
            <h3>230.2 Number of Services</h3>
            <p>A building or structure shall be supplied by only one service except as permitted in 230.2(A) through (D), which include special conditions such as:</p>
            <ul>
                <li>Fire pumps</li>
                <li>Emergency systems</li>
                <li>Multiple-occupancy buildings</li>
                <li>Capacity requirements</li>
                <li>Different characteristics (voltages, frequencies, etc.)</li>
            </ul>
            
            <h3>230.6 Conductors Considered Outside the Building</h3>
            <p>Service conductors are considered outside the building under certain conditions, including:</p>
            <ul>
                <li>When installed under at least 2 inches of concrete beneath a building</li>
                <li>Within a building in a raceway enclosed by concrete or brick not less than 2 inches thick</li>
            </ul>
            
            <h3>230.24 Clearances</h3>
            <p>Service-drop conductors must maintain minimum clearances:</p>
            <ul>
                <li>10 feet above finished grade, sidewalks, or platforms from which they might be accessible to pedestrians</li>
                <li>12 feet over residential property and driveways</li>
                <li>18 feet over public streets, alleys, roads, parking areas subject to truck traffic</li>
            </ul>
            
            <h3>230.42 Minimum Size and Rating</h3>
            <p>The service-entrance conductors shall have an ampacity of not less than the maximum load to be served, and not smaller than 8 AWG copper or 6 AWG aluminum or copper-clad aluminum.</p>
            
            <h3>230.43 Wiring Methods for 1000 Volts, Nominal, or Less</h3>
            <p>Service-entrance conductors shall be installed in accordance with the applicable requirements of the Code covering the type of wiring method used. Several approved wiring methods are listed, including:</p>
            <ul>
                <li>Rigid metal conduit (RMC)</li>
                <li>Intermediate metal conduit (IMC)</li>
                <li>Electrical metallic tubing (EMT)</li>
                <li>Service-entrance cables</li>
                <li>Wireways</li>
                <li>Busways</li>
                <li>Auxiliary gutters</li>
            </ul>
            
            <h3>230.70 General (Service Disconnecting Means)</h3>
            <p>Means shall be provided to disconnect all conductors in a building or structure from the service-entrance conductors.</p>
            <p>The service disconnecting means shall:</p>
            <ul>
                <li>Be installed at a readily accessible location either outside a building or structure or inside nearest the point of entrance of the service conductors</li>
                <li>Consist of not more than six switches or six circuit breakers mounted in a single enclosure, a group of separate enclosures, or in a switchboard or switchgear</li>
                <li>Be clearly marked as suitable for use as service equipment</li>
            </ul>
            
            <h3>230.82 Equipment Connected to the Supply Side</h3>
            <p>Only the following equipment shall be permitted to be connected to the supply side of the service disconnecting means:</p>
            <ul>
                <li>Cable limiters or other current-limiting devices</li>
                <li>Meters and meter sockets nominally rated not in excess of 1000 volts</li>
                <li>Meter disconnect switches</li>
                <li>Surge protective devices (SPDs)</li>
                <li>Ground-fault protection systems</li>
                <li>Solar photovoltaic systems, fuel cell systems, or interconnected electric power production sources</li>
                <li>Control circuits for power-operable service disconnecting means</li>
                <li>Ground-fault circuit interrupters</li>
            </ul>
            
            <h3>230.95 Ground-Fault Protection of Equipment</h3>
            <p>Ground-fault protection of equipment shall be provided for solidly grounded wye electrical services of more than 150 volts to ground but not exceeding 1000 volts phase-to-phase for each service disconnect rated 1000 amperes or more.</p>"""
        },
        {
            "article_number": "240",
            "title": "Overcurrent Protection",
            "summary": "Covers overcurrent protection requirements for conductors and equipment, including fuses and circuit breakers.",
            "content": """<h2>Article 240: Overcurrent Protection</h2>
            <p>This article establishes requirements for overcurrent protection and overcurrent protective devices for conductors and equipment.</p>
            
            <h3>240.1 Scope</h3>
            <p>Parts I through VII of this article provide the general requirements for overcurrent protection and overcurrent protective devices. Part VIII covers overcurrent protection for supervised industrial installations, and Part IX covers overcurrent protection for over 1000 volts, nominal.</p>
            
            <h3>240.4 Protection of Conductors</h3>
            <p>Conductors shall be protected against overcurrent in accordance with their ampacities specified in 310.15, unless otherwise permitted or required in 240.4(A) through (G).</p>
            <p>Small conductors have specific limitations:</p>
            <ul>
                <li>14 AWG copper: 15 amperes</li>
                <li>12 AWG copper: 20 amperes</li>
                <li>10 AWG copper: 30 amperes</li>
            </ul>
            
            <h3>240.6 Standard Ampere Ratings</h3>
            <p>Standard ampere ratings for fuses and inverse time circuit breakers are: 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, and 6000 amperes.</p>
            
            <h3>240.8 Fuses or Circuit Breakers in Parallel</h3>
            <p>Fuses and circuit breakers shall be permitted to be connected in parallel where they are factory assembled in parallel and listed as a unit. Individual fuses, circuit breakers, or combinations thereof shall not otherwise be connected in parallel.</p>
            
            <h3>240.15 Ungrounded Conductors</h3>
            <p>Overcurrent protection shall be provided in each ungrounded circuit conductor and shall be located at the point where the conductors receive their supply except as specified in 240.21. Overcurrent devices shall not be connected in series with any conductor that is intentionally grounded.</p>
            
            <h3>240.21 Location in Circuit</h3>
            <p>Overcurrent protection shall be provided at the point where the conductor to be protected receives its supply. Specific exceptions permit taps under certain conditions:</p>
            <ul>
                <li>Taps not exceeding 10 feet</li>
                <li>Taps not exceeding 25 feet</li>
                <li>Taps supplying a transformer</li>
                <li>Outside feeder taps</li>
            </ul>
            
            <h3>240.24 Location in or on Premises</h3>
            <p>Overcurrent devices shall:</p>
            <ul>
                <li>Be readily accessible and installed so that the center of the grip of the operating handle, when in its highest position, is not more than 6 feet 7 inches above the floor or working platform</li>
                <li>Not be located in the vicinity of easily ignitable material, such as in clothes closets</li>
                <li>Not be located in bathrooms of dwelling units, dormitories, guest rooms, or guest suites</li>
            </ul>
            
            <h3>240.50 General (Plug Fuses)</h3>
            <p>Plug fuses shall be classified at not over 125 volts and 30 amperes and below. They shall be permitted only for use in circuits where overcurrent protection is not required to handle the starting current of motors.</p>
            
            <h3>240.60 General (Cartridge Fuses and Fuseholders)</h3>
            <p>Cartridge fuses and fuseholders shall conform to 240.60(A) through (D).</p>
            
            <h3>240.80 Method of Operation (Circuit Breakers)</h3>
            <p>Circuit breakers shall be trip free and capable of being closed and opened by manual operation. Their normal method of operation by other than manual means, such as electrical or pneumatic, shall be permitted if means for manual operation are also provided.</p>
            
            <h3>240.83 Marking</h3>
            <p>Circuit breakers shall be durably and legibly marked with their ampere rating in a manner that will be visible after installation without removing any covers or barriers. They must also be marked with "SWD" or "HID" if they are suitable for switching duty or high-intensity discharge lighting.</p>"""
        },
        {
            "article_number": "250",
            "title": "Grounding and Bonding",
            "summary": "Covers general requirements for grounding and bonding of electrical installations, and specific requirements for system and equipment grounding.",
            "content": """<h2>Article 250: Grounding and Bonding</h2>
            <p>This article covers general requirements for grounding and bonding of electrical installations, and specific requirements for various systems, circuits, and equipment.</p>
            
            <h3>250.4 General Requirements for Grounding and Bonding</h3>
            <p>The following general requirements identify what grounding and bonding of electrical systems are required to accomplish.</p>
            
            <p><strong>(A) Grounded Systems:</strong></p>
            <ol>
                <li><strong>Electrical System Grounding:</strong> Electrical systems that are grounded shall be connected to earth to limit the voltage imposed by lightning, line surges, or unintentional contact with higher-voltage lines.</li>
                <li><strong>Grounding of Electrical Equipment:</strong> Normally non-current-carrying conductive materials enclosing electrical conductors or equipment shall be connected to earth to limit the voltage to ground on these materials.</li>
                <li><strong>Bonding of Electrical Equipment:</strong> Normally non-current-carrying conductive materials enclosing electrical conductors or equipment shall be connected together and to the electrical supply source in a manner that establishes an effective ground-fault current path.</li>
                <li><strong>Bonding of Electrically Conductive Materials and Other Equipment:</strong> Electrically conductive materials that are likely to become energized shall be connected together and to the electrical supply source in a manner that establishes an effective ground-fault current path.</li>
            </ol>
            
            <p><strong>(B) Ungrounded Systems:</strong></p>
            <ol>
                <li><strong>Grounding Electrical Equipment:</strong> Non-current-carrying conductive materials enclosing electrical conductors or equipment shall be connected to earth to limit the voltage imposed by lightning or unintentional contact with higher-voltage lines.</li>
                <li><strong>Bonding of Electrical Equipment:</strong> Non-current-carrying conductive materials enclosing electrical conductors or equipment shall be connected together and to the supply system grounded equipment in a manner that creates a low-impedance path for ground-fault current.</li>
                <li><strong>Bonding of Electrically Conductive Materials and Other Equipment:</strong> Electrically conductive materials that are likely to become energized shall be connected together and to the supply system grounded equipment.</li>
            </ol>
            
            <h3>250.6 Objectionable Current</h3>
            <p>The grounding of electrical systems, circuit conductors, surge arresters, surge-protective devices, and conductive normally non-current-carrying metal parts of equipment shall be installed and arranged in a manner that will prevent objectionable current over the grounding conductors or grounding paths.</p>
            
            <h3>250.20 Alternating-Current Systems to Be Grounded</h3>
            <p>The following AC systems shall be grounded:</p>
            <ul>
                <li>Systems of less than 50 volts under specific conditions</li>
                <li>Systems of 50 volts to 1000 volts where the system can be grounded so that the maximum voltage to ground does not exceed 150 volts</li>
                <li>Systems of 1 kV and over where the system is installed as a solidly grounded neutral system</li>
            </ul>
            
            <h3>250.24 Grounding Service-Supplied Alternating-Current Systems</h3>
            <p>The grounding electrode conductor connection shall be made at any accessible point from the load end of the service drop or service lateral to and including the terminal or bus to which the grounded service conductor is connected at the service disconnecting means.</p>
            
            <h3>250.28 Main Bonding Jumper</h3>
            <p>For a grounded system, an unspliced main bonding jumper shall be used to connect the equipment grounding conductor(s) and the service-disconnect enclosure to the grounded conductor within the enclosure for each service disconnect.</p>
            
            <h3>250.50 Grounding Electrode System</h3>
            <p>All grounding electrodes described in 250.52(A)(1) through (A)(7) that are present at each building or structure served shall be bonded together to form the grounding electrode system. These include:</p>
            <ul>
                <li>Metal underground water pipe in direct contact with the earth for 10 feet or more</li>
                <li>Metal frame of the building or structure</li>
                <li>Concrete-encased electrode (rebar or conductor)</li>
                <li>Ground ring</li>
                <li>Rod and pipe electrodes</li>
                <li>Plate electrodes</li>
                <li>Other listed electrodes</li>
            </ul>
            
            <h3>250.66 Size of Alternating-Current Grounding Electrode Conductor</h3>
            <p>The size of the grounding electrode conductor shall not be less than given in Table 250.66, which relates the size of the largest ungrounded service-entrance conductor to the required size of the grounding electrode conductor.</p>
            
            <h3>250.104 Bonding of Piping Systems and Exposed Structural Metal</h3>
            <p>Metal water piping system(s) installed in or attached to a building or structure shall be bonded to the service equipment enclosure, the grounded conductor at the service, the grounding electrode conductor where of sufficient size, or to one or more grounding electrodes used.</p>
            
            <h3>250.122 Size of Equipment Grounding Conductors</h3>
            <p>The minimum size of equipment grounding conductors for grounding raceway and equipment is based on the rating of the overcurrent device ahead of the circuit, as specified in Table 250.122.</p>"""
        },
        {
            "article_number": "300",
            "title": "Wiring Methods and Materials",
            "summary": "General requirements for wiring methods and materials",
            "content": "<h3>Article 300: Wiring Methods and Materials</h3><p>This article covers general requirements for wiring methods and materials for all wiring installations.</p><h4>Key Provisions:</h4><ul><li><strong>300.1 Scope:</strong> This article covers general requirements for wiring methods and materials for all wiring installations.</li><li><strong>300.3 Conductors:</strong> Requirements for conductors, including the requirement that all conductors of the same circuit must be contained within the same raceway, cable, trench, or cord.</li><li><strong>300.4 Protection Against Physical Damage:</strong> Requirements for protecting wiring against physical damage.</li><li><strong>300.5 Underground Installations:</strong> Requirements for underground installations, including minimum cover requirements.</li><li><strong>300.6 Protection Against Corrosion and Deterioration:</strong> Requirements for protecting raceways, cable trays, cablebus, auxiliary gutters, cable armor, boxes, cable sheathing, cabinets, elbows, couplings, fittings, supports, and support hardware against corrosion and deterioration.</li><li><strong>300.7 Raceways Exposed to Different Temperatures:</strong> Requirements for sealing raceways that pass from one temperature environment to another.</li><li><strong>300.9 Raceways in Wet Locations Above Grade:</strong> Where raceways are installed in wet locations above grade, the interior of these raceways shall be considered to be a wet location.</li><li><strong>300.10 Electrical Continuity of Metal Raceways and Enclosures:</strong> Metal raceways, cable armor, and other metal enclosures for conductors shall be metallically joined together into a continuous electrical conductor and shall be connected to all boxes, fittings, and cabinets so as to provide effective electrical continuity.</li><li><strong>300.11 Securing and Supporting:</strong> Requirements for securing and supporting raceways, cable assemblies, boxes, cabinets, and fittings.</li><li><strong>300.12 Mechanical Continuity — Raceways and Cables:</strong> Requirements for mechanical continuity of raceways and cables.</li><li><strong>300.13 Mechanical and Electrical Continuity — Conductors:</strong> Requirements for mechanical and electrical continuity of conductors.</li><li><strong>300.14 Length of Free Conductors at Outlets, Junctions, and Switch Points:</strong> At least 150 mm (6 in.) of free conductor shall be left at each outlet, junction, and switch point for splices or the connection of luminaires or devices.</li><li><strong>300.15 Boxes, Conduit Bodies, or Fittings — Where Required:</strong> A box shall be installed at each outlet and switch point for concealed knob-and-tube wiring.</li><li><strong>300.16 Raceway or Cable to Open or Concealed Wiring:</strong> Requirements for transitions from raceway or cable to open or concealed wiring.</li><li><strong>300.17 Number and Size of Conductors in Raceway:</strong> The number and size of conductors in any raceway shall not be more than will permit dissipation of the heat and ready installation or withdrawal of the conductors without damage to the conductors or to their insulation.</li><li><strong>300.18 Raceway Installations:</strong> Raceways shall be installed complete between outlet, junction, or splicing points prior to the installation of conductors.</li><li><strong>300.19 Supporting Conductors in Vertical Raceways:</strong> Conductors in vertical raceways shall be supported at the intervals not exceeding those specified in this section.</li><li><strong>300.20 Induced Currents in Ferrous Metal Enclosures or Ferrous Metal Raceways:</strong> Requirements for preventing induced currents in ferrous metal enclosures or ferrous metal raceways.</li><li><strong>300.21 Spread of Fire or Products of Combustion:</strong> Electrical installations in hollow spaces, vertical shafts, and ventilation or air-handling ducts shall be made so that the possible spread of fire or products of combustion will not be substantially increased.</li><li><strong>300.22 Wiring in Ducts Not Used for Air Handling, Fabricated Ducts for Environmental Air, and Other Spaces for Environmental Air (Plenums):</strong> Requirements for wiring in ducts, plenums, and other air-handling spaces.</li></ul>"
        },
        {
            "article_number": "310",
            "title": "Conductors for General Wiring",
            "summary": "Requirements for conductors used in general wiring applications",
            "content": "<h3>Article 310: Conductors for General Wiring</h3><p>This article covers general requirements for conductors and their type designations, insulations, markings, mechanical strengths, ampacity ratings, and uses.</p><h4>Key Provisions:</h4><ul><li><strong>310.1 Scope:</strong> This article covers general requirements for conductors and their type designations, insulations, markings, mechanical strengths, ampacity ratings, and uses.</li><li><strong>310.2 Definitions:</strong> Provides definitions for terms used within this article.</li><li><strong>310.3 Conductors:</strong> Requirements for conductors, including the rule that all conductors of a circuit shall be of the same conductor material.</li><li><strong>310.4 Conductors in Parallel:</strong> Requirements for conductors connected in parallel.</li><li><strong>310.6 Conductor Identification:</strong> Requirements for conductor identification.</li><li><strong>310.10 Uses Permitted:</strong> Permitted uses for various conductor types in different applications and environments.</li><li><strong>310.15 Ampacities for Conductors Rated 0–2000 Volts:</strong> The ampacities for conductors shall be as specified in the Ampacity Tables 310.15(B)(16) through 310.15(B)(21), with associated correction factors and adjustment factors.</li><li><strong>310.15(B)(3) Adjustment Factors:</strong> Where the number of current-carrying conductors in a raceway or cable exceeds three, the allowable ampacity of each conductor shall be reduced as shown in this section.</li><li><strong>310.15(B)(7) 120/240-Volt, Single-Phase Dwelling Services and Feeders:</strong> For one-family dwellings and individual dwelling units of two-family and multifamily dwellings, service and feeder conductors supplied by a single-phase, 120/240-volt system shall be permitted to be sized per this section.</li><li><strong>310.15(B)(16) Allowable Ampacities of Insulated Conductors:</strong> The famous ampacity table for insulated conductors rated up to and including 2000 volts, 60°C through 90°C, not more than three current-carrying conductors in raceway, cable, or earth.</li><li><strong>310.60 Conductors Rated 2001 to 35,000 Volts:</strong> Ampacities for solid dielectric-insulated conductors rated 2001 to 35,000 volts shall be as specified in Tables 310.60(C)(67) through 310.60(C)(86), with associated correction factors and adjustment factors.</li><li><strong>310.104 Conductor Constructions and Applications:</strong> Insulated conductors shall comply with the applicable provisions of one or more of the tables listed in this section.</li><li><strong>310.106 Conductors:</strong> Requirements for conductor construction, including the rule that all conductors shall be of copper unless otherwise specified.</li><li><strong>310.110 Conductor Identification:</strong> Requirements for conductor identification, including the use of colored insulation or marking methods.</li></ul>"
        },
        {
            "article_number": "314",
            "title": "Outlet, Device, Pull, and Junction Boxes; Conduit Bodies; Fittings; and Handhole Enclosures",
            "summary": "Requirements for boxes, conduit bodies, and fittings",
            "content": "<h3>Article 314: Outlet, Device, Pull, and Junction Boxes; Conduit Bodies; Fittings; and Handhole Enclosures</h3><p>This article covers the installation and use of all boxes and conduit bodies used as outlet, device, junction, or pull boxes.</p><h4>Key Provisions:</h4><ul><li><strong>314.1 Scope:</strong> This article covers the installation and use of all boxes and conduit bodies used as outlet, device, junction, or pull boxes, depending on their use, and handhole enclosures.</li><li><strong>314.3 Nonmetallic Boxes:</strong> Nonmetallic boxes shall be permitted only with open wiring on insulators, concealed knob-and-tube wiring, cabled wiring methods with entirely nonmetallic sheaths, flexible cords, and nonmetallic raceways.</li><li><strong>314.4 Metal Boxes:</strong> Metal boxes shall be grounded and bonded in accordance with Parts I, IV, V, VI, VII, and X of Article 250 as applicable.</li><li><strong>314.15 Damp or Wet Locations:</strong> In damp or wet locations, boxes, conduit bodies, outlet box hoods, and fittings shall be placed or equipped so as to prevent moisture from entering or accumulating within the box, conduit body, or fitting.</li><li><strong>314.16 Number of Conductors in Outlet, Device, and Junction Boxes, and Conduit Bodies:</strong> Boxes and conduit bodies shall be of an approved size to provide free space for all enclosed conductors.</li><li><strong>314.17 Conductors Entering Boxes, Conduit Bodies, or Fittings:</strong> Conductors entering boxes, conduit bodies, or fittings shall be protected from abrasion and shall comply with other requirements in this section.</li><li><strong>314.20 In Wall or Ceiling:</strong> Boxes in walls and ceilings shall be installed so that the front edge of the box will not be set back of the finished surface more than 6 mm (1⁄4 in.).</li><li><strong>314.21 Repairing Noncombustible Surfaces:</strong> Noncombustible surfaces that are broken or incomplete around boxes employing a flush-type cover or faceplate shall be repaired so there will be no gaps or open spaces greater than 3 mm (1⁄8 in.) at the edge of the box.</li><li><strong>314.22 Surface Extensions:</strong> Surface extensions shall be made by mounting and mechanically securing an extension ring over the box.</li><li><strong>314.23 Supports:</strong> Enclosures within the scope of this article shall be supported in accordance with one or more of the provisions in this section.</li><li><strong>314.24 Depth of Outlet Boxes:</strong> Outlet boxes shall have sufficient depth to allow equipment installed within them to be mounted properly and without likelihood of damage to conductors within the box.</li><li><strong>314.27 Outlet Boxes:</strong> Requirements for outlet boxes installed for the support of luminaires and other equipment.</li><li><strong>314.28 Pull and Junction Boxes and Conduit Bodies:</strong> Pull and junction boxes and conduit bodies shall provide adequate space and dimensions for the installation of conductors, and they shall comply with the specific requirements of this section.</li><li><strong>314.29 Boxes, Conduit Bodies, and Handhole Enclosures to Be Accessible:</strong> Boxes, conduit bodies, and handhole enclosures shall be installed so that the wiring contained in them can be rendered accessible without removing any part of the building or structure or, in underground circuits, without excavating sidewalks, paving, earth, or other substance that is to be used to establish the finished grade.</li><li><strong>314.30 Handhole Enclosures:</strong> Requirements for handhole enclosures, which are used for personnel to reach through and perform wire and cable splices and maintenance.</li></ul>"
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
        
        print(f"\nNEC Article Update Summary (Batch 2):")
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
            success = update_nec_articles_batch2()
            if success:
                print("NEC article update (batch 2) completed successfully.")
            else:
                print("NEC article update (batch 2) failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
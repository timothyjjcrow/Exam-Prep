import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import app factory and db
from app import create_app, db
from models import NECArticle

def fix_incomplete_articles():
    """Fixes all incomplete articles identified in our verification."""
    
    # Define the corrected articles
    corrected_articles = [
        {
            "article_number": "220",
            "title": "Branch-Circuit, Feeder, and Service Calculations",
            "summary": "Article 220 provides requirements for calculating branch circuit, feeder, and service loads.",
            "content": "<h3>Article 220: Branch-Circuit, Feeder, and Service Calculations</h3><p>This article covers the requirements for branch-circuit, feeder, and service calculations. It includes methods for calculating general lighting loads, appliance loads, and other electrical loads for sizing conductors, overcurrent protection, and service equipment in various occupancies.</p><h4>Key Provisions:</h4><ul><li><strong>220.1 Scope:</strong> This article provides requirements for calculating branch-circuit, feeder, and service loads.</li><li><strong>220.3 Application of Other Articles:</strong> In other articles applying to the calculation of loads in specialized applications, there are requirements provided in Table 220.3 that amend or supplement the requirements of this article.</li><li><strong>220.5 Calculations:</strong> Calculations shall be permitted to be rounded to the nearest ampere, volt, or VA, or kilowatt.</li><li><strong>220.12 Lighting Load for Specified Occupancies:</strong> A unit load per area is required to constitute the minimum lighting load for specified occupancies.</li><li><strong>220.14 Other Loads — All Occupancies:</strong> The minimum load for each outlet for specific appliances or equipment shall not be less than the load for the specific appliance or equipment.</li><li><strong>220.18 Maximum Loads:</strong> The total load shall not exceed the rating of the branch circuit, and it shall not exceed the maximum loads specified in 220.18(A) through (C) under the conditions specified therein.</li><li><strong>220.40 General:</strong> The calculated load of a feeder or service shall not be less than the sum of the loads on the branch circuits supplied, as determined by Part II of this article, after any applicable demand factors permitted by Part III or IV or required by Part V have been applied.</li><li><strong>220.60 Noncoincident Loads:</strong> Where it is unlikely that two or more noncoincident loads will be in use simultaneously, it shall be permissible to use only the largest load(s) that will be used at one time, in calculating the total load of a feeder or service.</li><li><strong>220.61 Feeder or Service Neutral Load:</strong> The feeder or service neutral load shall be the maximum unbalance of the load determined by this article.</li></ul>"
        },
        {
            "article_number": "300",
            "title": "Wiring Methods and Materials",
            "summary": "Article 300 covers general requirements for wiring methods and materials for all wiring installations.",
            "content": "<h3>Article 300: Wiring Methods and Materials</h3><p>This article covers general requirements for wiring methods and materials for all wiring installations.</p><h4>Key Provisions:</h4><ul><li><strong>300.1 Scope:</strong> This article covers wiring methods for all wiring installations unless modified by other articles.</li><li><strong>300.3 Conductors:</strong> Requirements for conductors, including requirements that all conductors of the same circuit be contained in the same raceway, cable, or trench.</li><li><strong>300.4 Protection Against Physical Damage:</strong> Requirements for protecting wiring methods against physical damage, including requirements for cables and raceways passing through wood or metal framing members.</li><li><strong>300.5 Underground Installations:</strong> Requirements for underground installations, including minimum cover requirements, protection from damage, splices and taps, backfill, and raceway seals.</li><li><strong>300.6 Protection Against Corrosion and Deterioration:</strong> Requirements for protecting raceways, cable trays, cablebus, auxiliary gutters, cable armor, boxes, cable sheathing, cabinets, elbows, couplings, fittings, supports, and support hardware from corrosion and deterioration.</li><li><strong>300.7 Raceways Exposed to Different Temperatures:</strong> Where portions of a raceway or sleeve are subject to different temperatures and condensation is known to be a problem, the raceway shall be filled with an approved material to prevent the circulation of warm air to a colder section of the raceway or sleeve.</li><li><strong>300.8 Installation of Conductors with Other Systems:</strong> Raceways or cable trays containing electrical conductors shall not contain any pipe, tube, or equal for steam, water, air, gas, drainage, or any service other than electrical.</li><li><strong>300.11 Securing and Supporting:</strong> Raceways, cable assemblies, boxes, cabinets, and fittings shall be securely fastened in place.</li><li><strong>300.14 Length of Free Conductors at Outlets, Junctions, and Switch Points:</strong> At least 150 mm (6 in.) of free conductor shall be left at each outlet, junction, and switch point for splices or the connection of luminaires or devices.</li><li><strong>300.15 Boxes, Conduit Bodies, or Fittings — Where Required:</strong> A box shall be installed at each conductor splice point, outlet, switch point, junction point, or pull point for the connection of conduit, electrical metallic tubing, electrical nonmetallic tubing, Type MC cable, Type AC cable, or other cables, and at each outlet and switch point for concealed knob-and-tube wiring.</li></ul>"
        },
        {
            "article_number": "334",
            "title": "Nonmetallic-Sheathed Cable: Types NM, NMC, and NMS",
            "summary": "Requirements for nonmetallic-sheathed cable",
            "content": "<h3>Article 334: Nonmetallic-Sheathed Cable: Types NM, NMC, and NMS</h3><p>This article covers the use, installation, and construction specifications for nonmetallic-sheathed cable.</p><h4>Key Provisions:</h4><ul><li><strong>334.1 Scope:</strong> This article covers the use, installation, and construction specifications of nonmetallic-sheathed cable.</li><li><strong>334.2 Definitions:</strong> Defines Type NM, Type NMC, and Type NMS cables.</li><li><strong>334.6 Listed:</strong> Types NM, NMC, and NMS cables shall be listed.</li><li><strong>334.10 Uses Permitted:</strong> Lists where Types NM, NMC, and NMS cables are permitted to be used.</li><li><strong>334.12 Uses Not Permitted:</strong> Lists where Types NM, NMC, and NMS cables shall not be used.</li><li><strong>334.15 Exposed Work:</strong> In exposed work, except as provided in 300.11(A), the cable shall be installed as specified in certain subsections.</li><li><strong>334.17 Through or Parallel to Framing Members:</strong> Types NM, NMC, or NMS cable shall comply with 300.4 where installed through or parallel to framing members.</li><li><strong>334.23 In Accessible Attics:</strong> Types NM, NMC, and NMS cables in accessible attics or roof spaces shall be installed as specified in 320.23.</li><li><strong>334.24 Bending Radius:</strong> Bends in Types NM, NMC, and NMS cable shall be made so that the cable is not damaged, with the radius of the curve of the inner edge of any bend not less than five times the diameter of the cable.</li><li><strong>334.30 Securing and Supporting:</strong> Nonmetallic-sheathed cable shall be secured by staples, cable ties, straps, or similar fittings so designed and installed as not to damage the cable at intervals not exceeding 1.4 m (4 1⁄2 ft) and within 300 mm (12 in.) of every outlet box, junction box, cabinet, or fitting.</li><li><strong>334.40 Boxes and Fittings:</strong> Requirements for boxes and fittings used with nonmetallic-sheathed cable.</li><li><strong>334.80 Ampacity:</strong> The ampacity of Types NM, NMC, and NMS cable shall be determined in accordance with 310.15.</li></ul>"
        },
        {
            "article_number": "352",
            "title": "Rigid Polyvinyl Chloride Conduit: Type PVC",
            "summary": "Requirements for rigid PVC conduit",
            "content": "<h3>Article 352: Rigid Polyvinyl Chloride Conduit: Type PVC</h3><p>This article covers the use, installation, and construction specifications for rigid polyvinyl chloride conduit (PVC) and associated fittings.</p><h4>Key Provisions:</h4><ul><li><strong>352.1 Scope:</strong> This article covers the use, installation, and construction specifications for rigid polyvinyl chloride conduit (PVC) and associated fittings.</li><li><strong>352.2 Definition:</strong> Defines rigid polyvinyl chloride conduit (PVC).</li><li><strong>352.6 Listing Requirements:</strong> PVC conduit, factory elbows, and associated fittings shall be listed.</li><li><strong>352.10 Uses Permitted:</strong> Lists where PVC conduit is permitted to be used.</li><li><strong>352.12 Uses Not Permitted:</strong> Lists where PVC conduit shall not be used.</li><li><strong>352.20 Size:</strong> PVC conduit shall be permitted in trade sizes 1⁄2 through 6.</li><li><strong>352.22 Number of Conductors:</strong> The number of conductors shall not exceed that permitted by the percentage fill specified in Table 1, Chapter 9.</li><li><strong>352.24 Bends — How Made:</strong> Bends shall be made by methods that do not damage the conduit. Field bends shall be made only with bending equipment identified for the purpose.</li><li><strong>352.26 Bends — Number in One Run:</strong> There shall not be more than the equivalent of four quarter bends (360 degrees total) between pull points.</li><li><strong>352.28 Trimming:</strong> All cut ends shall be trimmed inside and outside to remove rough edges.</li><li><strong>352.30 Securing and Supporting:</strong> PVC conduit shall be installed as a complete system as provided in 300.18 and shall be secured and supported in accordance with this section.</li><li><strong>352.44 Expansion Fittings:</strong> Expansion fittings for PVC conduit shall be provided to compensate for thermal expansion and contraction where the length change is expected to be 6 mm (1⁄4 in.) or greater in a straight run.</li><li><strong>352.46 Bushings:</strong> Where a conduit enters a box, fitting, or other enclosure, a bushing or adapter shall be provided to protect the wire from abrasion unless the box, fitting, or enclosure design provides equivalent protection.</li><li><strong>352.48 Joints:</strong> All joints between lengths of conduit, and between conduit and couplings, fittings, and boxes, shall be made by an approved method.</li><li><strong>352.56 Splices and Taps:</strong> Splices and taps shall be made in accordance with 300.15.</li><li><strong>352.60 Grounding:</strong> Where equipment grounding is required, a separate equipment grounding conductor shall be installed in the conduit.</li></ul>"
        },
        {
            "article_number": "404",
            "title": "Switches",
            "summary": "Requirements for installation and use of switches",
            "content": "<h3>Article 404: Switches</h3><p>This article covers the requirements for switches, including installation, ratings, and applications for various types of switches.</p><h4>Key Provisions:</h4><ul><li><strong>404.1 Scope:</strong> This article covers requirements for switches, switching devices, and circuit breakers used as switches.</li><li><strong>404.2 Switch Connections:</strong> Requirements for switch connections, including rules for connection to the grounded (neutral) conductor.</li><li><strong>404.3 Enclosure:</strong> Switches and circuit breakers shall be of the externally operable type mounted in an enclosure listed for the intended use.</li><li><strong>404.4 Wet Locations:</strong> A switch or circuit breaker in a wet location shall be enclosed in a weatherproof enclosure or cabinet.</li><li><strong>404.6 Position and Connection of Switches:</strong> Requirements for the position and connection of switches, including multi-way switches.</li><li><strong>404.7 Indicating:</strong> General-use and motor-circuit switches, circuit breakers, and molded case switches shall clearly indicate whether they are in the open 'off' or closed 'on' position.</li><li><strong>404.8 Accessibility and Grouping:</strong> Requirements for the accessibility and grouping of switches, including height limitations.</li><li><strong>404.9 Provisions for General-Use Snap Switches:</strong> Requirements for faceplates, grounding, and boxes for general-use snap switches.</li><li><strong>404.10 Mounting of Snap Switches:</strong> Snap switches mounted in boxes shall have faceplates installed so as to completely cover the opening and seat against the finished surface.</li><li><strong>404.11 Circuit Breakers as Switches:</strong> Circuit breakers used as switches in 120-volt and 277-volt fluorescent lighting circuits shall be listed and shall be marked SWD or HID.</li><li><strong>404.12 Grounding of Enclosures:</strong> Metal enclosures for switches or circuit breakers shall be connected to an equipment grounding conductor.</li><li><strong>404.13 Knife Switches:</strong> Requirements for knife switches, including mounting, connection, and use.</li><li><strong>404.14 Rating and Use of Snap Switches:</strong> Requirements for the rating and use of snap switches for various applications.</li><li><strong>404.15 Marking:</strong> Switches shall be marked with the current, voltage, and, if horsepower rated, the maximum rating for which they are designed.</li><li><strong>404.16 600-Volt Knife Switches:</strong> Requirements for knife switches rated over 600 volts.</li><li><strong>404.17 Fused Switches:</strong> Requirements for fused switches, which shall have the fuses connected on the load side.</li><li><strong>404.18 Wire-Bending Space:</strong> The wire-bending space at the supply terminals of switches and at the supply and load terminals of circuit breakers shall be as required in Article 312.6.</li></ul>"
        },
        {
            "article_number": "422",
            "title": "Appliances",
            "summary": "Requirements for electric appliances",
            "content": "<h3>Article 422: Appliances</h3><p>This article covers electric appliances used in any occupancy, including installation requirements, branch circuits, and disconnecting means.</p><h4>Key Provisions:</h4><ul><li><strong>422.1 Scope:</strong> This article covers electric appliances used in any occupancy.</li><li><strong>422.5 Ground-Fault Circuit-Interrupter (GFCI) Protection:</strong> Defines when GFCI protection is required for appliances.</li><li><strong>422.6 Listing Required:</strong> All appliances shall be listed unless otherwise permitted in 422.6(A) or (B).</li><li><strong>422.10 Branch-Circuit Rating:</strong> This section specifies the branch-circuit rating for appliances.</li><li><strong>422.11 Overcurrent Protection:</strong> Appliances shall be protected against overcurrent in accordance with this section.</li><li><strong>422.12 Central Heating Equipment:</strong> Central heating equipment other than fixed electric space-heating equipment shall be supplied by an individual branch circuit.</li><li><strong>422.13 Storage-Type Water Heaters:</strong> A branch circuit supplying a fixed storage-type water heater with a capacity of 450 L (120 gal) or less shall have a rating not less than 125 percent of the nameplate rating of the water heater.</li><li><strong>422.16 Flexible Cords:</strong> Conditions under which flexible cords are permitted for connection of appliances.</li><li><strong>422.17 Protection of Combustible Material:</strong> Appliances that may present a fire hazard shall be installed to provide clearances from combustible materials.</li><li><strong>422.18 Support of Ceiling-Suspended (Paddle) Fans:</strong> Ceiling-suspended (paddle) fans shall be supported independently of an outlet box or by a listed outlet box or outlet box system identified for the use and installed in accordance with 314.27(C).</li><li><strong>422.20 Other Installation Methods:</strong> Appliances using other installation methods shall be installed in accordance with the related articles.</li><li><strong>422.30 General:</strong> A means shall be provided to disconnect each appliance from all ungrounded conductors in accordance with the following sections.</li><li><strong>422.31 Disconnection of Permanently Connected Appliances:</strong> Requirements for disconnection of permanently connected appliances rated at not over 300 volt-amperes or 1⁄8 horsepower.</li><li><strong>422.33 Disconnection of Cord-and-Plug-Connected Appliances:</strong> Requirements for disconnection of cord-and-plug-connected appliances.</li><li><strong>422.41 Cord-and-Plug-Connected Appliances Subject to Immersion:</strong> Cord-and-plug-connected portable, freestanding hydromassage units and hand-held hair dryers shall be constructed to provide protection for personnel against electrocution when immersed while in the "on" or "off" position.</li><li><strong>422.49 High-Pressure Spray Washers:</strong> All single-phase cord-and-plug-connected high-pressure spray washing machines rated at 250 volts or less shall be provided with factory-installed GFCI protection for personnel.</li><li><strong>422.50 Cord-and-Plug-Connected Pipe Heating Assemblies:</strong> Heating assemblies are permitted to be cord-and-plug connected provided certain conditions are met.</li><li><strong>422.51 Vending Machines:</strong> Cord-and-plug-connected vending machines shall have GFCI protection for personnel.</li><li><strong>422.52 Electric Drinking Fountains:</strong> Electric drinking fountains shall be protected with GFCI protection for personnel.</li></ul>"
        }
    ]
    
    print("=== FIXING INCOMPLETE NEC ARTICLES ===")
    
    fixed_count = 0
    error_count = 0
    
    try:
        for article_data in corrected_articles:
            article_number = article_data["article_number"]
            
            # Check if article exists
            existing_article = NECArticle.query.filter_by(article_number=article_number).first()
            
            if existing_article:
                # Update the article
                existing_article.title = article_data["title"]
                existing_article.summary = article_data.get("summary", existing_article.summary)
                existing_article.content = article_data["content"]
                fixed_count += 1
                print(f"✅ Updated Article {article_number}: {article_data['title']}")
            else:
                # Create new article
                new_article = NECArticle(
                    article_number=article_data["article_number"],
                    title=article_data["title"],
                    summary=article_data.get("summary", ""),
                    content=article_data["content"]
                )
                db.session.add(new_article)
                fixed_count += 1
                print(f"✅ Added Article {article_number}: {article_data['title']}")
        
        # Commit changes
        db.session.commit()
        
        print(f"\nSuccessfully fixed {fixed_count} articles.")
        print("Run 'verify_all_articles.py' again to check if all articles are now complete.")
        
    except Exception as e:
        db.session.rollback()
        error_count += 1
        print(f"❌ Error fixing articles: {str(e)}")
    
    return fixed_count, error_count

def main():
    """Create app context and run the fix function."""
    try:
        app = create_app()
        with app.app_context():
            fixed_count, error_count = fix_incomplete_articles()
            if error_count == 0:
                print("All articles fixed successfully!")
            else:
                print(f"Encountered {error_count} errors while fixing articles.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
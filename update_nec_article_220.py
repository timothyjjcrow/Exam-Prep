import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 220 to the database."""
    # Article data
    article_data = {
        "article_number": "220",
        "title": "Branch-Circuit, Feeder, and Service Load Calculations",
        "summary": "Article 220 provides requirements for calculating loads for branch circuits, feeders, and services. It includes methods for computing minimum required ampacity and load calculations for various types of occupancies.",
        "content": """<h3>Scope and Purpose</h3><p>Article 220 provides requirements for calculating electrical loads for branch circuits, feeders, and services. These calculations are essential for determining the appropriate size of conductors, overcurrent protection devices, and service equipment. The article is organized into five parts:</p><ul><li>Part I: General Requirements</li><li>Part II: Branch-Circuit Load Calculations</li><li>Part III: Feeder and Service Load Calculations</li><li>Part IV: Optional Feeder and Service Load Calculations</li><li>Part V: Farm Load Calculations</li></ul><p>Accurate load calculations are fundamental to electrical safety, preventing overloaded circuits and ensuring adequate capacity for the intended use of the electrical system.</p><h3>Branch Circuit Load Calculations</h3><p><strong>General Lighting Loads (220.12):</strong> General lighting loads are calculated based on the unit load per square foot (volt-amperes per square foot) for the occupancy involved. For example:</p><ul><li>Dwelling units: 3 VA per square foot</li><li>Hospitals: 2 VA per square foot</li><li>Hotels and motels (guest rooms): 2 VA per square foot</li><li>Warehouses (storage): 0.25 VA per square foot</li></ul><p>The general lighting load is calculated by multiplying the square footage of the area by the appropriate unit load value.</p><p><strong>Show Window and Track Lighting (220.14(G)(H)):</strong> For show windows, a minimum of 200 VA per linear foot of show window is required. For track lighting, the load is calculated at not less than 150 VA for every 2 feet of track or fraction thereof.</p><p><strong>Receptacle Loads (220.14(I)(J)):</strong> For receptacle outlets of 20-ampere or less rating in non-dwelling occupancies, a minimum of 180 VA for each single or multiple receptacle on one yoke is required. For dwelling units, general-use receptacles are covered under the general lighting load calculation.</p><h3>Feeder and Service Load Calculations</h3><p><strong>General Method (220.40):</strong> The calculated load of a feeder or service is the sum of all branch circuit loads as determined by Part II of Article 220, subject to applicable demand factors permitted by Parts III, IV, or V.</p><p><strong>General Lighting (220.42):</strong> The demand factors in Table 220.42 can be applied to the total general lighting load. For example:</p><ul><li>First 3000 VA or less: 100% demand factor</li><li>Next 117,000 VA: 35% demand factor</li><li>Remainder over 120,000 VA: 25% demand factor</li></ul><p>This recognizes that not all lighting in a building operates simultaneously, allowing for a reduction in the calculated load.</p><p><strong>Receptacle Loads (220.44):</strong> For non-dwelling receptacle loads, a demand factor of 100% for the first 10 kVA and 50% for the remainder is permitted.</p><p><strong>Electric Dryers and Cooking Appliances (220.54-220.55):</strong> Specific demand factors apply to electric dryers and cooking appliances in dwelling units, recognizing that not all appliances operate at full load simultaneously. For example:</p><ul><li>Electric dryers: Demand factors range from 100% for 1-4 dryers to as low as 28% for large numbers of dryers</li><li>Electric ranges: Demand factors are based on the number and size of the appliances, with detailed tables provided in 220.55</li></ul><h3>Dwelling Unit Calculations</h3><p><strong>Standard Method (220.80-220.82):</strong> For dwelling units, the standard method for calculating service or feeder loads includes:</p><ul><li>General lighting and general-use receptacles: 3 VA per square foot</li><li>Small appliance branch circuits: 1500 VA for each circuit</li><li>Laundry branch circuit: 1500 VA</li><li>Appliances on dedicated circuits (e.g., dishwasher, disposal): Nameplate rating</li><li>Ranges, ovens, and dryers: According to specific tables</li><li>Largest motor: 25% of motor rating</li></ul><p>The first 10,000 VA of the sum is calculated at 100%, and the remainder at 40%.</p><p><strong>Optional Method (220.84):</strong> The optional method for dwelling units (100 amperes or greater) provides an alternative calculation based on the square footage of the dwelling and the specific appliances installed. It can result in a lower calculated load than the standard method and includes:</p><ul><li>Base load: 100 VA per square foot for the first 1000 square feet, plus 40 VA per square foot for area over 1000 square feet</li><li>Air conditioning: Largest of cooling or heating equipment</li><li>Range, oven, cooktop: 8 kVA</li><li>Dryer: 5 kVA</li><li>Other appliances: 1 kVA each for four or more fixed appliances</li></ul><p>This method is particularly useful for larger dwellings where the standard method might result in an unnecessarily large service.</p><h3>Feeder Demand Factors</h3><p><strong>Multiple Dwelling Units (220.84-220.86):</strong> For multiple dwelling units, significant demand factors can be applied based on the number of units. Optional calculations are provided in 220.84 through 220.86, which recognize that the coincidental use of electrical equipment decreases as the number of dwelling units increases.</p><p><strong>Schools (220.86):</strong> The optional method for schools allows the feeder or service demand load to be calculated at 20 VA per square foot, with specific additions for special loads such as kitchen equipment and electric space heating.</p><p><strong>New Restaurants (220.88):</strong> For new restaurants where the total connected kitchen equipment load exceeds 200 kVA, the feeder or service demand load can be calculated using specific demand factors based on the total connected load.</p><h3>Maximum Demand Calculations</h3><p><strong>Determination of Maximum Demand (220.80):</strong> The maximum demand for a service or feeder is determined by computing the sum of all branch circuit loads, as determined per Part II, and applying any applicable demand factors from Parts III or IV.</p><p><strong>Motor Loads (220.50):</strong> Motor loads are calculated according to the provisions of Article 430. For multiple motors, the largest motor is typically calculated at 125% of its rated load, with other motors at 100%.</p><p><strong>Fixed Electric Space Heating (220.51):</strong> Fixed electric space heating loads can be subject to applicable demand factors provided in the tables or otherwise identified in Article 220. For systems with automatic sequential switching, the load may be calculated at the total connected load multiplied by the percentage in Table 220.60.</p><h3>Practical Application of Load Calculations</h3><p><strong>Step-by-Step Example for Dwelling Unit:</strong></p><ol><li>Calculate general lighting and receptacle load: (Square footage × 3 VA)</li><li>Add small appliance circuits: (2 circuits × 1500 VA)</li><li>Add laundry circuit: 1500 VA</li><li>Add fixed appliances: (Per nameplate ratings)</li><li>Add space heating or air conditioning: (Larger of the two)</li><li>Add range: (According to Table 220.55)</li><li>Apply demand factors: 100% for first 10,000 VA, 40% for remainder</li><li>Calculate minimum service size: Total VA ÷ Voltage</li></ol><p>This methodical approach ensures that the electrical service is properly sized to handle the maximum demand expected for the dwelling.</p><h3>Common Calculation Errors</h3><p><strong>Overlooking Demand Factors:</strong> One common error is failing to apply appropriate demand factors, which can result in oversized services and unnecessary costs.</p><p><strong>Incorrect Area Calculations:</strong> Miscalculating the square footage of a building or area can significantly affect the general lighting load calculation.</p><p><strong>Neglecting Diversity for Multiple Units:</strong> Not applying appropriate diversity factors for multiple dwelling units can lead to oversizing of feeders and services.</p><p><strong>Incorrect Appliance Calculations:</strong> Using incorrect values for ranges, dryers, and other appliances can distort the overall load calculation.</p><h3>Recent Code Changes</h3><p>Recent NEC editions have introduced several changes to Article 220:</p><ul><li>Updated general lighting load values for various occupancies</li><li>Clarified methods for calculating electric vehicle charging equipment loads</li><li>Revised demand factors for certain types of loads</li><li>Added provisions for energy management systems</li></ul><p>These changes reflect evolving technology and usage patterns in modern electrical systems, as well as a growing focus on energy efficiency.</p><p>Article 220 is fundamental to electrical design and installation, as it provides the basis for determining the capacity requirements of electrical systems. Accurate load calculations ensure that electrical systems are neither undersized (creating safety hazards) nor oversized (incurring unnecessary costs).</p>"""
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
                print(f"NEC article 220 update completed successfully.")
            else:
                print(f"NEC article 220 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 310 to the database."""
    # Article data
    article_data = {
        "article_number": "310",
        "title": "Conductors for General Wiring",
        "summary": "Article 310 covers the general requirements for conductors, including ampacity, sizing, and identification. It includes important conductor ampacity tables used throughout electrical installations.",
        "content": "<h3>Scope and General Provisions</h3><p>Article 310 is one of the most frequently referenced articles in the NEC, as it covers the general requirements for conductors used in electrical installations. It provides vital information on conductor sizing, ampacity, insulation types, and allowable applications. The article also contains the essential ampacity tables that electricians rely on to determine the current-carrying capacity of different types of conductors.</p><p>This article applies to all general wiring conductors, with some exceptions (such as those covered in other specific articles like communications circuits in Chapter 8). It addresses both power and lighting conductors used in typical electrical installations.</p><h3>Conductor Construction and Applications</h3><p><strong>Conductor Material (310.3):</strong> Conductors used in general wiring must be copper, aluminum, copper-clad aluminum, or other material approved as suitable for the purpose. Notably, when aluminum conductors are used, they must be an aluminum alloy designed specifically for electrical purposes. Modern aluminum conductors (AA-8000 series) have improved properties over older aluminum types that had connection problems in the 1960s-70s.</p><p><strong>Conductor Insulation (310.4 and 310.104):</strong> Conductors must have insulation that is rated for their operating environment and application. The article specifies requirements for conductor insulation, including temperature ratings, moisture resistance, and suitability for different environments. Common insulation types include:</p><ul><li>THHN/THWN-2: Thermoplastic, heat-resistant, rated 90°C dry/75°C wet, commonly used for general building wiring</li><li>XHHW: Cross-linked polyethylene, heat-resistant, rated 90°C dry/75°C wet, suitable for wet locations</li><li>USE: Underground Service Entrance cable, suitable for direct burial</li><li>RHW: Rubber heat-resistant, moisture-resistant, rated 75°C</li></ul><p><strong>Minimum Conductor Size (310.5):</strong> The minimum conductor size for general wiring applications is typically 14 AWG copper or 12 AWG aluminum, with some exceptions. For example, fixture wires and equipment leads may be smaller when part of a listed assembly.</p><h3>Conductor Ampacity</h3><p><strong>Definition of Ampacity:</strong> Ampacity is the maximum current, in amperes, that a conductor can carry continuously under the conditions of use without exceeding its temperature rating. It's a critical factor in conductor selection because overloaded conductors can overheat, damaging insulation and potentially causing fires.</p><p><strong>Ampacity Tables (Tables 310.15(B)):</strong> Article 310 provides tables for determining conductor ampacity based on:</p><ul><li>Conductor size (AWG or kcmil)</li><li>Conductor material (copper or aluminum)</li><li>Temperature rating of the insulation (60°C, 75°C, 90°C)</li><li>Installation conditions (ambient temperature, number of current-carrying conductors, etc.)</li></ul><p>The primary ampacity tables in Article 310 include:</p><ul><li><strong>Table 310.15(B)(16):</strong> The most commonly used table for determining ampacities of insulated conductors rated up to and including 2000 volts, in raceway, cable, or direct buried applications (not more than three current-carrying conductors).</li><li><strong>Table 310.15(B)(17):</strong> For single conductors in free air.</li><li><strong>Tables 310.15(B)(18) and (19):</strong> For conductors in underground electrical ducts.</li><li><strong>Tables 310.15(B)(20) and (21):</strong> For bare or covered conductors.</li></ul><p><strong>Adjustment Factors (310.15(C)):</strong> The ampacity values from these tables must be adjusted for actual installation conditions, including:</p><p><strong>1. Number of Conductors:</strong> When more than three current-carrying conductors are installed in a raceway or cable, the ampacity must be reduced according to Table 310.15(C)(1). For example, with 4-6 conductors, the ampacity is reduced to 80% of the table value.</p><p><strong>2. Ambient Temperature (310.15(B)(2)):</strong> The ampacity must be adjusted for ambient temperatures different from 30°C (86°F). For example, if the ambient temperature is 40°C (104°F), the ampacity for a 75°C rated conductor must be multiplied by 0.82.</p><p><strong>Rounding (310.15(B)):</strong> When calculated ampacity adjustment results in a decimal fraction, the result is permitted to be rounded up to the next higher ampere rating (for 800 amperes or less). This provides some flexibility when the calculated value falls just below a standard overcurrent device rating.</p><h3>Conductor Applications and Temperature Limitations</h3><p><strong>Terminal Temperature Limitations (110.14(C)):</strong> While Article 310 is primarily about conductors, their application is affected by the temperature limitations of terminations. Most standard equipment has terminals rated at 60°C or 75°C, not 90°C. Therefore, even if using a 90°C rated conductor (like THHN), its ampacity must be limited to the 75°C column of Table 310.15(B)(16) when connecting to standard equipment.</p><p><strong>Special Applications (310.10):</strong> The article includes specific provisions for conductors in special applications:</p><ul><li>Wet locations: Conductors must be approved for wet locations or have a moisture-impervious metal sheath.</li><li>Corrosive conditions: Conductors exposed to oils, greases, vapors, gases, or other substances with deteriorating effects must be of a type approved for the condition.</li><li>Direct burial: Conductors must be approved for direct burial and installed at proper depth.</li></ul><h3>Practical Applications and Examples</h3><p><strong>Example 1:</strong> Determining the minimum size conductor for a 30A, 240V circuit in a residential installation, with an ambient temperature of 30°C and no more than three current-carrying conductors in a raceway:</p><p>From Table 310.15(B)(16), a 10 AWG copper conductor with THHN insulation (90°C) has an ampacity of 40A when calculated using the 75°C column (due to terminal limitations). Since 40A exceeds the required 30A, 10 AWG is acceptable.</p><p><strong>Example 2:</strong> Determining the minimum size conductor for a feeder supplying 100A to a sub-panel, where the conductors will run through an attic with an ambient temperature of 50°C (122°F) and there will be 6 current-carrying conductors in the conduit:</p><p>From Table 310.15(B)(16), for a copper THHN conductor (75°C column due to terminations), we need a conductor with a base ampacity significantly higher than 100A because:</p><ul><li>Temperature correction factor for 50°C = 0.75 (from Table 310.15(B)(2)(a))</li><li>Adjustment factor for 6 conductors = 0.80 (from Table 310.15(C)(1))</li></ul><p>The adjusted ampacity needs to be at least 100A:<br>Required base ampacity = 100A ÷ (0.75 × 0.80) = 100A ÷ 0.60 = 167A</p><p>From Table 310.15(B)(16), a 3/0 AWG copper conductor with THHN insulation has an ampacity of 175A (using the 75°C column). Therefore, a 3/0 AWG copper conductor would be required for this application.</p><p>Understanding Article 310 is essential for electricians to ensure that conductors are properly sized to carry the intended load safely, preventing overheating and potential fire hazards. It also helps in ensuring compliance with code requirements and achieving cost-effective designs.</p>"
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
                print(f"NEC article 310 update completed successfully.")
            else:
                print(f"NEC article 310 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
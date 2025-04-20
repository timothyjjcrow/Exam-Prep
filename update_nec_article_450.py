import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 450 to the database."""
    article_data = {
        "article_number": "450",
        "title": "Transformers and Transformer Vaults",
        "summary": "Requirements for the installation of transformers, including their location, overcurrent protection, grounding, ventilation, marking, and special provisions for specific transformer types and installations.",
        "content": """
<h3>Scope and Purpose</h3>
<p>Article 450 covers the installation of all transformers except for specific exceptions like Class 2 and Class 3 transformers, sign and outline lighting transformers, and several other specialized types. The article provides requirements for transformer location, overcurrent protection, grounding, and transformer vaults to ensure safe and reliable operation of these critical power system components.</p>

<h3>General Requirements</h3>
<p><strong>450.3 Overcurrent Protection:</strong> This section provides detailed requirements for transformer overcurrent protection, with separate tables for transformers over 1000 volts and 1000 volts or less:</p>
<ul>
    <li>For transformers 1000 volts or less, primary and/or secondary protection requirements are based on the transformer's impedance and rating.</li>
    <li>For transformers over 600V, primary protection generally must not exceed 250% of rated primary current, though exceptions exist.</li>
    <li>Secondary protection may be required depending on the primary protection level, secondary conductor ampacity, and load characteristics.</li>
    <li>Tables 450.3(A) and 450.3(B) provide specific maximum rating percentages for both primary and secondary protection, based on transformer type and supervised/unsupervised installations.</li>
    <li>Special provisions apply to supervised industrial installations with qualified maintenance and monitoring.</li>
</ul>

<p><strong>450.4 Autotransformers:</strong> Requirements for autotransformers, which use a single winding with taps:</p>
<ul>
    <li>Autotransformers 1000V or less shall not be used to step down from a grounded system to supply ungrounded systems, unless specific power equipment is supplied and the system has ground fault protection.</li>
    <li>Buck-boost autotransformers can be used to raise or lower voltage by a small percentage, typically 5-10%.</li>
</ul>

<p><strong>450.5 Grounding:</strong> Requirements for transformer grounding:</p>
<ul>
    <li>Transformer secondary circuits must be grounded under the conditions specified in 250.20.</li>
    <li>If a transformer has a continuous metallic path between primary and secondary, the secondary must be grounded if the primary is grounded.</li>
    <li>For transformers with an ungrounded delta-connected secondary, at least one corner of the delta must be marked for testing.</li>
</ul>

<p><strong>450.6 Secondary Ties:</strong> When transformers are operated in parallel or with secondaries connected, appropriate overcurrent protection must be provided, and the connections must allow for circular current flows without overloading any transformer.</p>

<p><strong>450.7 Parallel Operation:</strong> For transformers operated in parallel on either primary or secondary sides, the impedance and turns ratio must be matched sufficiently to ensure proper load sharing.</p>

<h3>Transformer Location and Installation</h3>
<p><strong>450.8 Guarding and Protection:</strong> Transformer windings must be guarded against accidental contact, with exposed live parts such as terminals properly protected:</p>
<ul>
    <li>Dry-type transformers installed indoors must be provided with a means to minimize the entrance of foreign objects.</li>
    <li>Transformers exposed to physical damage must be suitably protected.</li>
    <li>Transformers must be properly supported and firmly secured in place.</li>
</ul>

<p><strong>450.9 Ventilation:</strong> Transformers shall be installed with adequate ventilation to prevent overheating:</p>
<ul>
    <li>Sufficient airflow must be maintained around transformers to dissipate heat.</li>
    <li>Transformers with ventilating openings must be installed so that the ventilating openings are not blocked.</li>
    <li>If a transformer is installed in a poorly ventilated area, it may need to be derated.</li>
</ul>

<p><strong>450.10 Grounding:</strong> Exposed non-current-carrying metal parts of transformer installations must be grounded according to Article 250:</p>
<ul>
    <li>Includes transformer frames, enclosures, and raceways.</li>
    <li>Exception applies to specific types of transformers where grounding is either impractical or not required.</li>
</ul>

<p><strong>450.11 Marking:</strong> Each transformer must be provided with a nameplate giving the following information:</p>
<ul>
    <li>Name of manufacturer</li>
    <li>Rated kilovolt-amperes</li>
    <li>Frequency</li>
    <li>Primary and secondary voltage</li>
    <li>Impedance for transformers 25 kVA and larger</li>
    <li>Required clearances for transformers with ventilating openings</li>
    <li>Amount and kind of insulating liquid where used</li>
    <li>Temperature class for dry-type transformers</li>
</ul>

<h3>Specific Transformer Types</h3>
<p><strong>450.21 through 450.23 Dry-Type Transformers:</strong> Installation requirements for dry-type transformers:</p>
<ul>
    <li><strong>1000 Volts or Less:</strong> Must be installed in accordance with ventilation requirements, with minimum clearances from combustible materials based on their rating and construction.</li>
    <li><strong>Over 1000 Volts:</strong> Must be installed in a transformer room of fire-resistant construction unless they are specifically designed for other locations.</li>
</ul>

<p><strong>450.24 through 450.28 Liquid-Filled Transformers:</strong> Requirements for transformers that use oil or other liquid insulation:</p>
<ul>
    <li><strong>100 kVA or Less:</strong> Specific safety requirements for indoor installations, including the use of fire-resistant rooms or vaults.</li>
    <li><strong>Over 100 kVA:</strong> More stringent requirements for indoor installations, generally requiring a vault unless specifically designed with reduced flammability.</li>
    <li><strong>Outdoor Installations:</strong> Must have proper containment for liquid spills and be located with regard for fire risk to buildings.</li>
</ul>

<p><strong>450.29 through 450.48 Transformer Vaults:</strong> Detailed requirements for the construction and ventilation of transformer vaults:</p>
<ul>
    <li><strong>Construction:</strong> Vaults must be constructed of fire-resistant materials with appropriate fire ratings, usually 3 hours.</li>
    <li><strong>Doors:</strong> Vault doors must swing out and be equipped with locks, with a personnel door that can be operated from inside without a key.</li>
    <li><strong>Ventilation:</strong> Vaults must have adequate ventilation to prevent excessive temperature rise, with ventilation openings protected against falling debris.</li>
    <li><strong>Drainage:</strong> Vaults containing liquid-filled transformers must have drainage systems to remove any accumulated liquid.</li>
    <li><strong>Water Pipes and Accessories:</strong> No water, sewer, or steam piping shall pass through transformer vaults, and no foreign systems shall be installed in the vault.</li>
    <li><strong>Storage:</strong> Transformer vaults shall not be used for storage of materials.</li>
</ul>

<h3>Common Installation Issues</h3>
<ul>
    <li><strong>Inadequate Clearances:</strong> Not maintaining required clearances around transformers for proper ventilation and heat dissipation.</li>
    <li><strong>Improper Overcurrent Protection:</strong> Installing overcurrent protection devices that don't comply with the requirements in Tables 450.3(A) and 450.3(B).</li>
    <li><strong>Incorrect Grounding:</strong> Failing to properly ground transformer enclosures or improperly grounding secondary systems.</li>
    <li><strong>Ventilation Issues:</strong> Blocking ventilation openings or installing transformers in areas with inadequate airflow.</li>
    <li><strong>Vault Construction Deficiencies:</strong> Transformer vaults that don't meet fire-resistance requirements or lack proper doors, ventilation, or drainage.</li>
    <li><strong>Liquid Containment:</strong> Inadequate containment provisions for liquid-filled transformers, potentially allowing environmentally hazardous spills.</li>
    <li><strong>Misapplication of Transformer Types:</strong> Using transformers in environments for which they are not rated or designed.</li>
</ul>

<h3>Practical Application</h3>
<p>When working with transformers and designing transformer installations, electricians should:</p>
<ul>
    <li><strong>Calculate Protection Requirements:</strong> Use Tables 450.3(A) and 450.3(B) to determine proper overcurrent protection for both primary and secondary circuits.</li>
    <li><strong>Consider Environment:</strong> Select transformer type (dry-type, liquid-filled, etc.) appropriate for the installation environment.</li>
    <li><strong>Plan for Maintenance:</strong> Ensure adequate working space around transformers for future maintenance and service.</li>
    <li><strong>Verify Ventilation:</strong> Calculate heat dissipation requirements and ensure adequate ventilation for the specific transformer type and rating.</li>
    <li><strong>Address Fire Safety:</strong> For liquid-filled transformers, incorporate appropriate fire containment measures, including vaults where required.</li>
    <li><strong>Ensure Proper Grounding:</strong> Follow the grounding requirements in Article 250 for both the transformer and the secondary system.</li>
</ul>

<h3>Recent Code Changes</h3>
<p>Recent updates to Article 450 have included:</p>
<ul>
    <li>Revised overcurrent protection requirements, particularly for supervised installations</li>
    <li>Updated requirements for transformers with environmentally friendly and less flammable insulating liquids</li>
    <li>Enhanced provisions for transformer vault construction and ventilation</li>
    <li>Modified requirements for dry-type transformers based on temperature ratings and construction</li>
    <li>Clarified grounding requirements for various transformer configurations</li>
</ul>

<p>Article 450 continues to evolve with transformer technology, with increased attention to fire safety, environmental concerns with insulating liquids, energy efficiency, and proper protection of these critical power distribution components.</p>
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
                print(f"NEC article 450 update completed successfully.")
            else:
                print(f"NEC article 450 update failed.")
    except Exception as e:
        print(f"Error updating NEC article 450: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
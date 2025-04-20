import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 90 to the database."""
    # Article data
    article_data = {
        "article_number": "90",
        "title": "Introduction",
        "summary": "Article 90 of the NEC serves as the code's introduction, outlining the purpose, scope, and general arrangement of the Code, as well as providing guidance on how the NEC is to be applied and enforced.",
        "content": "<h3>Purpose and Scope of the NEC</h3><p><strong>Purpose (90.1):</strong> The NEC's primary aim is the <em>practical safeguarding of persons and property</em> from electrical hazards. Article 90 clarifies that the Code is not a design manual or an instruction guide for untrained persons, but a set of minimum requirements focused on safety. It emphasizes that compliance with NEC rules should result in an installation that is essentially free from electrical danger&#8203;:contentReference[oaicite:0]{index=0}.</p><p><strong>Scope (90.2):</strong> Article 90 defines where the NEC applies. Generally, it covers all electrical installations in buildings and structures that aren't under exclusive control of utilities. It does <em>not</em> cover installations like utility company equipment (e.g. power generation, transmission, and distribution), vehicles, ships, aircraft, or underground mines. The NEC is intended for premises wiring (including yards, lots, and installations connected to an electrical supply)&#8203;:contentReference[oaicite:1]{index=1}&#8203;:contentReference[oaicite:2]{index=2}.</p><h3>Code Arrangement and Enforcement</h3><p><strong>Code Arrangement (90.3):</strong> The NEC is arranged in chapters (1–9), and Article 90 explains this structure. Chapters 1–4 apply generally, chapters 5–7 supplement or modify those general rules for special occupancies or equipment, and Chapter 8 (communications systems) and Chapter 9 (tables) have distinct applications. Article 90 underscores that where Chapters 5–7 conflict with earlier chapters, the special rules prevail.</p><p><strong>Enforcement (90.4):</strong> The NEC itself is a model code and gains legal force when adopted by local jurisdictions. Enforcement is by the <em>Authority Having Jurisdiction (AHJ)</em> – typically local electrical inspectors or building officials&#8203;:contentReference[oaicite:3]{index=3}. They interpret rules, grant special permissions or exceptions, and ensure installations meet code. Article 90.4 gives the AHJ authority to enforce the code and to require upgrades in installations that are found unsafe.</p><h3>Interpretation of Code Language</h3><p>Article 90.5 helps users understand how to read the NEC: it distinguishes <strong>mandatory rules</strong>, <strong>permissive rules</strong>, and explanatory material&#8203;:contentReference[oaicite:4]{index=4}. <ul><li><em>Mandatory rules</em> use terms like \"shall\" or \"shall not,\" indicating requirements that must be followed&#8203;:contentReference[oaicite:5]{index=5}.</li><li><em>Permissive rules</em> use phrases like \"shall be permitted\" or \"shall not be required,\" allowing certain actions as options&#8203;:contentReference[oaicite:6]{index=6}.</li><li><em>Explanatory material</em> (informational notes and fine-print notes) is provided for clarity and is not enforceable as code&#8203;:contentReference[oaicite:7]{index=7}. Informative Annexes in the back of the NEC are also non-mandatory guidance.</li></ul>This structure ensures the Code's intent is clear, balancing safety mandates with allowable practices.</p><h3>Other Provisions in Article 90</h3><p><strong>Not a Design Specification:</strong> Article 90 notes the NEC is not intended to be a design specification or an instruction manual for untrained people. It sets minimum safety standards – designers and installers can always exceed code minimums for greater safety or performance.</p><p><strong>Equipment Examination (90.7):</strong> Installations of equipment must consider listing or labeling. Article 90 points out that listed equipment (evaluated by a testing lab) is considered to meet safety standards. Unlisted equipment may require special AHJ approval after examination for safety.</p><p><strong>Units of Measurement (90.9):</strong> The NEC uses SI (metric) units with inch-pound units in parentheses. Only the SI units are official, but both are provided for convenience.</p>"
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
                print(f"NEC article 90 update completed successfully.")
            else:
                print(f"NEC article 90 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
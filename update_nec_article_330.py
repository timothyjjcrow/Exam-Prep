import sys
import os
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC Article 330 to the database."""
    article_data = {
        "article_number": "330",
        "title": "Metal-Clad Cable: Type MC",
        "summary": "Requirements for the installation of Metal-Clad Cable (Type MC) including uses permitted, uses not permitted, construction specifications, installation, and ampacity ratings.",
        "content": """
<h3>Scope and Purpose</h3>
<p>Article 330 covers the use, installation, and construction specifications for Metal-Clad Cable (Type MC). Metal-clad cable provides a durable wiring method with enhanced mechanical protection compared to many other cable types. The metal sheath provides physical protection for the conductors and can serve as an equipment grounding conductor when properly installed.</p>

<h3>Cable Construction</h3>
<p><strong>330.104 Conductors:</strong> MC cable conductors must be of copper, aluminum, copper-clad aluminum, nickel or nickel-coated copper, solid or stranded. The minimum conductor size is 18 AWG copper and 12 AWG aluminum or copper-clad aluminum.</p>

<p><strong>330.108 Equipment Grounding Conductor:</strong> MC cable must contain an equipment grounding conductor. This can be:</p>
<ul>
    <li>A separate equipment grounding conductor</li>
    <li>An insulated or uninsulated conductor</li>
    <li>The metallic sheath itself, in specific listed types of MC cable</li>
</ul>

<p><strong>330.116 Sheath:</strong> The metallic sheath must be:</p>
<ul>
    <li>Continuous and close-fitting</li>
    <li>Made of aluminum, copper, or steel (smooth or corrugated)</li>
    <li>Impervious to moisture</li>
</ul>

<h3>Uses Permitted</h3>
<p><strong>330.10 Uses Permitted:</strong> Type MC cable can be used in the following locations:</p>
<ul>
    <li>For services, feeders, and branch circuits</li>
    <li>In cable trays</li>
    <li>In dry, damp, or wet locations</li>
    <li>Exposed or concealed</li>
    <li>Direct buried where identified for such use</li>
    <li>In hazardous (classified) locations where specifically permitted by other articles</li>
    <li>In underground runs if protected against physical damage and corrosion</li>
    <li>Embedded in poured concrete if identified for this use</li>
</ul>

<h3>Uses Not Permitted</h3>
<p><strong>330.12 Uses Not Permitted:</strong> Type MC cable shall not be used:</p>
<ul>
    <li>Where exposed to destructive corrosive conditions, such as direct burial in the earth, in concrete, or where exposed to cinder fills, strong chlorides, caustic alkalis, etc., unless the metallic sheath is suitable for the conditions or is protected by material suitable for the conditions</li>
    <li>Where subject to physical damage (during installation or afterward) unless protected</li>
</ul>

<h3>Installation</h3>
<p><strong>330.24 Bending Radius:</strong> Bends in MC cable shall be made so that the cable will not be damaged, and the radius of the curve of the inner edge of any bend shall not be less than shown in the following:</p>
<ul>
    <li>Smooth sheath:
        <ul>
            <li>10 times the external diameter for cables not more than 3/4 inch in external diameter</li>
            <li>12 times the external diameter for cables more than 3/4 inch but not more than 1-1/2 inches in external diameter</li>
            <li>15 times the external diameter for cables more than 1-1/2 inches in external diameter</li>
        </ul>
    </li>
    <li>Interlocked or corrugated sheath:
        <ul>
            <li>7 times the external diameter for cables not more than 3/4 inch in external diameter</li>
            <li>10 times the external diameter for cables more than 3/4 inch but not more than 1-1/2 inches in external diameter</li>
            <li>12 times the external diameter for cables more than 1-1/2 inches in external diameter</li>
        </ul>
    </li>
</ul>

<p><strong>330.30 Securing and Supporting:</strong> MC cables must be supported and secured at intervals not exceeding 6 feet, with the following exceptions:</p>
<ul>
    <li>Where the cable is fished between access points through concealed spaces and supporting is impracticable</li>
    <li>Lengths not exceeding 6 feet from a luminaire terminal connection for tap connections to luminaires</li>
    <li>Cables containing four or fewer conductors, not larger than 10 AWG, where fastened at intervals not exceeding 12 inches and within 12 inches of every box, cabinet, or fitting</li>
</ul>

<p><strong>330.31 Single Conductors:</strong> When single conductors are installed, all phase conductors and the neutral conductor (where used) shall be grouped to minimize induced voltage on the sheath.</p>

<p><strong>330.40 Boxes and Fittings:</strong> Fittings used for connecting Type MC cable to boxes, cabinets, or other equipment shall be listed and identified for such use. Where single-conductor cables enter ferrous metal boxes or cabinets, the installation shall comply with 300.20 to prevent inductive heating.</p>

<p><strong>330.80 Ampacity:</strong> The ampacity of MC cable shall be determined in accordance with 310.15. The installation conditions must be addressed when determining the allowable ampacity of the conductors.</p>

<h3>Common Installation Issues and Best Practices</h3>
<ul>
    <li><strong>Termination:</strong> The most common issues with MC cable occur at terminations. The anti-short bushing (red head or similar device) must be properly installed to prevent the metal sheath from damaging conductor insulation.</li>
    
    <li><strong>Strapping:</strong> Inadequate support is a common violation. MC cable must be secured within 12 inches of every box or fitting and at intervals not exceeding 6 feet (with exceptions as noted above).</li>
    
    <li><strong>Bending:</strong> Overbending can damage the cable and potentially damage conductor insulation. Minimum bending radius requirements must be followed.</li>
    
    <li><strong>Corrosion Protection:</strong> In wet or damp locations, proper fittings must be used to prevent water entry, and in corrosive environments, special consideration must be given to the suitability of the metal sheath.</li>
    
    <li><strong>Selection:</strong> Different types of MC cable are available for various applications (e.g., standard MC, MC-HL for hazardous locations, MC with isolated ground). Selecting the proper type for the application is essential.</li>
</ul>

<h3>Special Applications</h3>
<p>MC cable is commonly used in:</p>
<ul>
    <li><strong>Commercial Construction:</strong> Office buildings, retail spaces, and institutional facilities often use MC cable for branch circuits</li>
    
    <li><strong>Healthcare Facilities:</strong> MC cable with redundant equipment grounding paths may be used in certain healthcare facility applications</li>
    
    <li><strong>Industrial Settings:</strong> Where physical protection of conductors is required but conduit may be impractical</li>
    
    <li><strong>Hazardous Locations:</strong> Special types of MC cable (MC-HL) are designed for use in certain hazardous (classified) locations</li>
</ul>

<h3>Comparison to Other Wiring Methods</h3>
<p>Compared to other wiring methods, MC cable offers:</p>
<ul>
    <li>Greater mechanical protection than NM cable or AC cable</li>
    <li>Faster installation than conduit and wire methods</li>
    <li>Better fire resistance than many other cable types</li>
    <li>Protection against electromagnetic interference for sensitive circuits (when using MC cable with continuous corrugated aluminum sheath)</li>
</ul>

<h3>Recent Code Changes</h3>
<p>Recent NEC updates have affected Article 330 in several ways:</p>
<ul>
    <li>Clarification of requirements for supporting and securing MC cable</li>
    <li>Updated provisions for MC cable in hazardous locations</li>
    <li>Recognition of various types of equipment grounding conductors in MC cable</li>
    <li>Clarification of listing requirements for fittings</li>
</ul>

<p>Understanding and correctly applying the requirements of Article 330 is essential for ensuring safe and compliant installations of Metal-Clad Cable.</p>
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
                print(f"NEC article 330 update completed successfully.")
            else:
                print(f"NEC article 330 update failed.")
    except Exception as e:
        print(f"Error updating NEC article 330: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
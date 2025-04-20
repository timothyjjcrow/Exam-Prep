import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 440 to the database."""
    # Article data
    article_data = {
        "article_number": "440",
        "title": "Air Conditioning and Refrigeration Equipment",
        "summary": "Article 440 covers the electrical requirements for air conditioning and refrigeration equipment, including hermetic refrigerant motor-compressors, and the branch circuits and controllers for such equipment. It provides specific rules for disconnecting means, overload protection, and branch circuit sizing.",
        "content": "<h3>Scope and Applicability</h3><p>Article 440 covers air conditioning and refrigeration equipment that incorporates a hermetic refrigerant motor-compressor, including the equipment's electrical components, branch circuits, and controllers. This article applies to units like heat pumps, air conditioners, refrigerators, freezers, and other cooling equipment found in residential, commercial, and industrial applications.</p><p>The article works in conjunction with Articles 430 (Motors) and 422 (Appliances), providing specific requirements that modify or supplement these general rules when dealing with refrigeration equipment. Article 440 takes precedence when it contains requirements that differ from other articles.</p><h3>Nameplate and Marking Requirements</h3><p><strong>Hermetic Refrigerant Motor-Compressor Nameplate (440.4):</strong> These specialized motors must have a nameplate marked with the manufacturer's name, rated voltage, phase frequency, full-load current, locked-rotor current (or code letter), and nominal horsepower. This information is essential for proper circuit sizing and protection.</p><p><strong>Multimotor Equipment (440.4(B)):</strong> Equipment with multiple motors or motor-compressors must be marked with the full-load current of each motor-compressor, the rating of the branch-circuit short-circuit and ground-fault protective device, and the maximum rating of the branch-circuit short-circuit and ground-fault protective device if applicable.</p><p>These markings are crucial because they provide the information needed for properly sizing the conductors, branch-circuit protection, and disconnecting means for the equipment.</p><h3>Branch Circuit Requirements</h3><p><strong>Branch Circuit Sizing (440.32 and 440.33):</strong> The branch-circuit conductors supplying a single motor-compressor must have an ampacity of not less than 125% of either the motor-compressor rated-load current or the branch-circuit selection current, whichever is greater.</p><p>For equipment that operates on a voltage range (for example, 208-230V), the branch circuit should be sized based on the maximum operating current. This ensures that under all conditions, the circuit can safely handle the load.</p><p><strong>Multimotor Equipment (440.6):</strong> For equipment with multiple motors or motor-compressors, the branch-circuit rating and ampacity must be based on the total of the rated-load currents or branch-circuit selection currents, whichever is greater, and the total of all other load currents that might operate simultaneously.</p><p><strong>Short-Circuit and Ground-Fault Protection (440.22):</strong> The branch-circuit protective device (usually a circuit breaker or fuses) must be capable of handling the starting current of the motor. Generally, the maximum rating of the branch-circuit short-circuit and ground-fault protective device is 175% of the motor-compressor rated-load current or branch-circuit selection current, whichever is greater.</p><h3>Disconnecting Means</h3><p><strong>General Requirement (440.12):</strong> A disconnecting means must be provided for each motor-compressor and for each motor in the refrigeration system. This allows for safe servicing of components while isolating them from the power source.</p><p><strong>Rating and Interrupting Capacity (440.12(A)):</strong> The disconnecting means must have an ampere rating at least 115% of the nameplate rated-load current or branch-circuit selection current, whichever is greater. This ensures it can safely interrupt the power supply.</p><p><strong>Location (440.14):</strong> The disconnecting means must be located within sight from and readily accessible from the air conditioning or refrigeration equipment. However, a single disconnecting means can be used for a group of these units if they're within one room and visible from the disconnect.</p><p>There's an exception for units in one- and two-family dwellings, where the disconnect can be up to 50 feet away if it can be locked in the open position, which prevents someone from accidentally turning on the power while maintenance is being performed.</p><h3>Overload Protection</h3><p><strong>Overload Protection for Motor-Compressors (440.52):</strong> Each motor-compressor must have overload protection to prevent it from operating under a condition that exceeds its full-load current rating by a specific percentage. This protection can be:</p><ul><li>A separate overload relay selected according to manufacturer's data</li><li>A thermal protector integral with the motor-compressor, approved for use with the motor-compressor</li><li>A fuse or inverse time circuit breaker sized according to the article's requirements</li></ul><p><strong>Application of Overload Relay (440.52(A)):</strong> When a separate overload relay is used, it must be sized at not more than 140% of the motor-compressor rated-load current. This provides protection against sustained overloads while allowing for the high starting currents typical of these motors.</p><p><strong>Thermal Protection (440.52(A)(3)):</strong> Many modern motor-compressors have built-in thermal protection that senses the temperature of the compressor and shuts it down if it gets too hot. This provides excellent protection because it directly measures the heat that could damage the motor.</p><h3>Special Provisions for Room Air Conditioners</h3><p><strong>Definition (440.60):</strong> Room air conditioners are specific types of air conditioners that are typically installed in windows or through-the-wall and are not connected to ducts. They usually come as a packaged unit with the evaporator, condenser, and motor-compressor in one assembly.</p><p><strong>Branch-Circuit Requirements (440.62):</strong> A room air conditioner is considered a single-motor appliance when it comes to branch-circuit requirements. The total marked rating of the unit should not exceed 80% of the branch-circuit rating if no other loads are supplied by the same circuit.</p><p><strong>Ground-Fault Circuit-Interrupter (GFCI) Protection (440.65):</strong> Cord-connected room air conditioners must have GFCI protection for personnel. This is typically provided as part of the attachment plug or in the power supply cord within 12 inches of the attachment plug.</p><h3>Special Applications</h3><p><strong>Commercial Refrigeration (440.4(B) and 440.22(B)):</strong> Commercial refrigeration systems often have multiple compressors and motors. Special provisions apply to the marking and protection of these systems. The branch-circuit conductors must be adequately sized to handle the combined loads of all compressors that might operate simultaneously.</p><p><strong>Industrial Refrigeration (440.11 and 440.12(B)):</strong> Industrial refrigeration systems might have very large motors and compressors. The disconnecting means must be sized appropriately for these larger loads, and special provisions may apply for the control circuits.</p><p><strong>Hermetic Refrigerant Motor-Compressors with Internal Thermal Protection (440.52(D)):</strong> For motor-compressors with internal thermal protection that has been certified and marked as such, additional external overload protection may not be required.</p><h3>Common Compliance Issues</h3><p><strong>Disconnect Location:</strong> One common code violation is placing the disconnecting means too far from the equipment or in a location not visible from the equipment. The disconnect must generally be within sight and readily accessible from the equipment.</p><p><strong>Branch Circuit Sizing:</strong> Improperly sized branch circuits that don't account for the marked branch-circuit selection current or locked-rotor current of the compressor can lead to overheating, tripping breakers, or damage to the equipment.</p><p><strong>Equipment Protection:</strong> Failing to provide proper short-circuit, ground-fault, and overload protection tailored to the specific requirements of refrigeration equipment can lead to equipment damage or unsafe conditions.</p><p>Understanding Article 440 is crucial for electricians working on air conditioning and refrigeration systems to ensure safety, reliability, and compliance with the NEC. The specific requirements for these specialized motor-compressors help prevent electrical hazards while accommodating the unique operating characteristics of refrigeration equipment.</p>"
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
                print(f"NEC article 440 update completed successfully.")
            else:
                print(f"NEC article 440 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
import sys
import os

# Import directly from app
from app import create_app, db
from models import NECArticle

def update_nec_article():
    """Update or add NEC article 445 to the database."""
    # Article data
    article_data = {
        "article_number": "445",
        "title": "Generators",
        "summary": "Article 445 covers the installation of generators, including requirements for location, mounting, overcurrent protection, disconnecting means, grounding, and marking. It applies to both portable and permanently installed generators in various applications.",
        "content": "<h3>Scope and Overview</h3><p>Article 445 covers the installation, operation, and maintenance requirements for generators in various applications. This includes portable generators, permanently installed standby generators, and large industrial generators. The article addresses general requirements applicable to all generators, with specific provisions based on their size, application, and whether they're portable or permanently installed.</p><p>Generators are increasingly common in both residential and commercial settings for backup power during outages, prime power in areas without reliable utility service, and peak load management. Understanding Article 445 is essential for safe and compliant generator installations.</p><h3>General Installation Requirements</h3><p><strong>Location (445.10):</strong> Generators must be installed in locations that minimize hazards. They should be placed in areas with adequate ventilation to dissipate heat and exhaust gases. Generators must also be protected from physical damage, weather exposure (if not rated for outdoor use), and contact by unqualified persons.</p><p><strong>Mounting (445.11):</strong> Generators must be mounted securely on substantial structures or foundations to prevent vibration and displacement during operation. Portable generators are exempt from this requirement.</p><p><strong>Terminal Housings (445.13):</strong> All energized parts of generators operating at more than 50 volts must be enclosed in terminal housings. These housings protect against accidental contact with live parts and must provide proper connection points for conductors.</p><p><strong>Bushings (445.16):</strong> Where conductors pass through openings in generator enclosures, suitable bushings, conduit fittings, or other means must be used to protect the conductors from abrasion or other damage.</p><h3>Overcurrent Protection</h3><p><strong>Generator Protection (445.12):</strong> Generators must be protected from overloads and short-circuits with suitable overcurrent protective devices (typically fuses or circuit breakers). The protection must be coordinated with the generator's characteristics to prevent damage while allowing normal operation.</p><p><strong>Ampacity of Conductors (445.13):</strong> The ampacity of the conductors from the generator terminals to the first distribution device containing overcurrent protection must not be less than 115% of the nameplate current rating of the generator. For a generator with no overcurrent protection, the conductor ampacity must not be less than 115% of the full-load current.</p><p>This 115% sizing factor accounts for the generator's continuous duty rating and provides a margin of safety. The conductors need to be sized larger than the generator's rated current to prevent overheating during extended operation.</p><h3>Disconnecting Means</h3><p><strong>Requirement (445.18):</strong> A disconnecting means must be provided for each generator that operates at more than 50 volts. This disconnect allows for safe servicing of the generator by providing a means to isolate it from the electrical system.</p><p><strong>Location (445.18(A)):</strong> The disconnecting means must be readily accessible and located within sight of the generator. For small generators, the generator's stop switch can serve as the disconnecting means if it meets certain requirements.</p><p><strong>Multiple Supplies (445.18(C)):</strong> Where a generator and another source (such as a utility service) operate in parallel, a placarding requirement applies. The disconnect must indicate all sources of power, as personnel working on the system need to be aware of all possible sources that could energize the circuits.</p><h3>Grounding Requirements</h3><p><strong>Grounding Frame (445.11):</strong> Generator frames must be grounded in accordance with Article 250 if they operate at more than 50 volts. This grounding is crucial for safety to prevent the frame from becoming energized in the event of an internal fault.</p><p><strong>System Grounding (250.20, 250.30):</strong> Although not specifically part of Article 445, system grounding for generators is a critical safety consideration covered in Article 250. Generators that serve as separately derived systems must have their neutral bonded to ground at the generator, while those that operate in parallel with other services typically have the neutral-to-ground bond at the service equipment.</p><p><strong>Portable Generators (445.20):</strong> The grounding electrode conductor connection requirements depend on whether the portable generator supplies premises wiring or only cord-and-plug-connected equipment. Specific rules in 250.34 detail when portable generators must be connected to a grounding electrode.</p><h3>Ground Fault Protection</h3><p><strong>Ground Fault Protection of Equipment (445.20):</strong> The requirements for ground-fault protection depend on the generator's application and size. In general, generators that supply premises wiring systems and operate as separately derived systems require ground-fault protection in accordance with Articles 210, 215, and 230.</p><p><strong>Exception for Portable Generators (445.20):</strong> Portable generators are not required to have ground-fault protection for their output circuits when used to supply only equipment mounted on the generator, cord-and-plug-connected equipment through receptacles mounted on the generator, or both.</p><h3>Special Applications</h3><p><strong>Residential Standby Generators (445.18):</strong> For permanently installed generators in residences, a disconnecting means must be provided at a readily accessible location. In one- and two-family dwellings, this disconnect is often integrated with the transfer switch or load panel.</p><p><strong>Health Care Facilities (517.30, 517.35):</strong> Generators used in health care facilities have additional requirements specified in Article 517, including connections to the essential electrical system, testing requirements, and specific regulations for emergency power.</p><p><strong>Emergency and Standby Systems (700.12, 701.12, 702.12):</strong> Generators used for emergency, legally required standby, or optional standby systems must meet the requirements of Articles 700, 701, and 702, respectively. These include specific fuel supply requirements, testing provisions, and requirements for transfer equipment.</p><h3>Marking and Documentation</h3><p><strong>Nameplate (445.11):</strong> Generators must be provided with a nameplate giving the manufacturer's name, rated frequency, power factor, number of phases, rating in kilowatts or kilovolt-amperes, normal volts and amperes, and rated ambient temperature.</p><p><strong>Diagram (445.11):</strong> A permanent diagram or schedule showing the correct wiring connections should be provided with the generator. This is particularly important for larger generators with multiple connection options.</p><p><strong>Warning Signs (445.18(D)):</strong> For generators intended to operate in parallel with the utility supply, warning signs must be installed at the service entrance to indicate the type and location of on-site generator sources.</p><h3>Portable Generator Safety</h3><p><strong>Carbon Monoxide Hazards:</strong> While not explicitly part of the NEC, safety with portable generators is a critical concern. Generators must never be operated indoors or in enclosed spaces due to the risk of carbon monoxide poisoning. Modern portable generators often include CO sensors and automatic shutdown features.</p><p><strong>Connections to Premises Wiring (445.20):</strong> Portable generators must not be connected to premises wiring unless through a transfer switch that prevents interconnection with the utility supply. This requirement prevents backfeeding, which can be deadly to utility workers.</p><p><strong>Receptacles (445.20):</strong> Receptacles on portable generators must have appropriate GFCI protection based on the environment and application. This protects users from shock hazards, particularly in potentially wet conditions.</p><p>Understanding and properly applying Article 445 is essential for electricians installing generator systems. The requirements ensure generators operate safely, protecting both the equipment and the people who use or maintain it. As generators become more common in residential and commercial settings, proper installation according to the NEC becomes increasingly important.</p>"
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
                print(f"NEC article 445 update completed successfully.")
            else:
                print(f"NEC article 445 update failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
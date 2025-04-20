#!/usr/bin/env python3
import json
from app import create_app, db
from models import NECArticle, TheoryTopic

# Data for remaining NEC articles and theory topics
DATA = {
  "NEC_articles": [
    {
      "article_number": 230,
      "title": "Services",
      "summary": """Article 230 covers service conductors and equipment – essentially the interface between the utility and a building's electrical system. It details requirements for service drops/laterals, service entrance conductors, and service equipment (the main disconnect and related hardware).""",
      "high_frequency": True
    },
    {
      "article_number": 240,
      "title": "Overcurrent Protection",
      "summary": """Article 240 provides the requirements for overcurrent protection devices (OCPDs) such as fuses and circuit breakers and how they must be sized and installed to protect circuits.""",
      "high_frequency": True
    },
    {
      "article_number": 242,
      "title": "Overvoltage Protection (Surge Protection)",
      "summary": """Article 242 covers surge protective devices (SPDs) and surge arresters – equipment that protects electrical systems from transient overvoltages (like lightning or switching surges). It consolidates what used to be in older NEC Articles 280 and 285 into one article.""",
      "high_frequency": True
    },
    {
      "article_number": 300,
      "title": "General Requirements for Wiring Methods",
      "summary": """Article 300 lays out general rules that apply to most wiring methods (raceways, cables, etc.) regarding how and where conductors can be installed. It addresses protection from damage, conductor grouping, spacing, supporting, and environmental considerations.""",
      "high_frequency": True
    },
    {
      "article_number": 310,
      "title": "Conductors for General Wiring",
      "summary": """Article 310 covers the types and uses of conductors (wires) used in general electrical installations. It specifies allowable conductor materials (copper, aluminum, copper-clad) and insulation types and their temperature ratings.""",
      "high_frequency": True
    },
    {
      "article_number": 312,
      "title": "Cabinets, Cutout Boxes, and Meter Sockets",
      "summary": """Article 312 covers cabinets, cutout boxes, and meter socket enclosures – essentially electrical boxes with hinged or removable covers that house circuit breakers, switches, or metering equipment. It provides construction and installation requirements to ensure safety.""",
      "high_frequency": True
    },
    {
      "article_number": 314,
      "title": "Outlet, Device, Pull and Junction Boxes; Conduit Bodies; Fittings; Handhole Enclosures",
      "summary": """Article 314 covers all types of electrical boxes (junction boxes, switch/outlet boxes, conduit bodies, etc.) and handholes, focusing on their sizing, usage, and installation.""",
      "high_frequency": True
    },
    {
      "article_number": 330,
      "title": "Metal-Clad Cable: Type MC",
      "summary": """Article 330 pertains to Type MC cable, which is a factory assembly of insulated conductors in a flexible metal cladding (armor). It describes where and how MC cable can be used.""",
      "high_frequency": True
    },
    {
      "article_number": 334,
      "title": "Nonmetallic-Sheathed Cable: Types NM, NMC, NMS",
      "summary": """Article 334 covers NM cable (often known by the trade name "Romex"), which is a flexible cable assembly with nonmetallic (usually PVC) outer sheath, used predominantly in residential and light commercial wiring.""",
      "high_frequency": True
    },
    {
      "article_number": 342,
      "title": "Intermediate Metal Conduit: Type IMC",
      "summary": """Article 342 covers Intermediate Metal Conduit (IMC), a steel conduit with a wall thickness between that of Electrical Metallic Tubing (EMT) and Rigid Metal Conduit (RMC).""",
      "high_frequency": True
    },
    {
      "article_number": 344,
      "title": "Rigid Metal Conduit: Type RMC",
      "summary": """Article 344 is the governing article for Rigid Metal Conduit, the thick-wall, threaded metal raceway. It allows RMC to be used in all environments – exposed, concealed, underground, wet locations, and hazardous areas – as long as appropriate fittings and corrosion protections are used.""",
      "high_frequency": True
    },
    {
      "article_number": 348,
      "title": "Flexible Metal Conduit: Type FMC",
      "summary": """Article 348 covers Flexible Metal Conduit (FMC), a spiraled, flexible metal raceway commonly used for equipment connections subject to vibration or where routing a rigid conduit is impractical.""",
      "high_frequency": True
    },
    {
      "article_number": 350,
      "title": "Liquidtight Flexible Metal Conduit: Type LFMC",
      "summary": """Article 350 addresses LFMC, which is similar to FMC but with a plastic outer jacket that makes it liquidtight. LFMC (sometimes called "Sealtite") is used for flexible connections in wet or outdoor locations.""",
      "high_frequency": True
    },
    {
      "article_number": 352,
      "title": "Rigid Polyvinyl Chloride Conduit: Type PVC",
      "summary": """Article 352 covers rigid PVC conduit – a nonmetallic raceway often used for underground or corrosive environments. PVC conduit is immune to rust and is an electrical insulator, but it requires attention to thermal expansion and support.""",
      "high_frequency": True
    },
    {
      "article_number": 358,
      "title": "Electrical Metallic Tubing: Type EMT",
      "summary": """Article 358 details EMT, which is a thin-walled metal tubing used as a raceway for electrical conductors. EMT is unthreaded (it uses compression or set-screw connectors) and is often called "conduit," though technically classified as tubing.""",
      "high_frequency": True
    },
    {
      "article_number": 404,
      "title": "Switches",
      "summary": """Article 404 covers switches of all types (snap switches like toggle light switches, dimmer switches, knife switches, etc.) and their installation requirements.""",
      "high_frequency": True
    },
    {
      "article_number": 406,
      "title": "Receptacles, Cord Connectors, and Attachment Plugs (Caps)",
      "summary": """Article 406 is all about outlets – receptacle sockets, the matching plugs (attachment caps), and similar devices. It includes requirements for where receptacles must be Tamper-Resistant.""",
      "high_frequency": True
    },
    {
      "article_number": 410,
      "title": "Luminaires, Lampholders, and Lamps",
      "summary": """Article 410 covers lighting fixtures (luminaires), lamp holders (sockets), and lamps (bulbs) – basically, the installation of lighting equipment. It includes requirements to prevent fire and shock hazards.""",
      "high_frequency": True
    },
    {
      "article_number": 422,
      "title": "Appliances",
      "summary": """Article 422 applies to electrical appliances – equipment such as water heaters, ovens, dishwashers, garbage disposals, HVAC appliances, etc. It addresses things like disconnecting means and overcurrent protection for appliances.""",
      "high_frequency": True
    },
    {
      "article_number": 440,
      "title": "Air-Conditioning and Refrigeration Equipment",
      "summary": """Article 440 covers equipment like central air-conditioners, heat pumps, and large refrigeration units – essentially motor-driven air-conditioning equipment. It has specialized rules because these devices have motors and often multiple loads in one unit.""",
      "high_frequency": True
    },
    {
      "article_number": 445,
      "title": "Generators",
      "summary": """Article 445 covers generators and sets standards for their installation, including requirements for overcurrent protection and disconnects.""",
      "high_frequency": True
    },
    {
      "article_number": 450,
      "title": "Transformers and Transformer Vaults",
      "summary": """Article 450 contains requirements for power transformers – including how to protect them from overcurrent and how to install them safely (sometimes in fire-rated vaults).""",
      "high_frequency": True
    },
    {
      "article_number": 625,
      "title": "Electric Vehicle Charging Systems",
      "summary": """Article 625 covers the installation of Electric Vehicle Supply Equipment (EVSE) – i.e., EV chargers for cars. These systems have unique requirements because of high continuous loads and the need for safety where users plug in vehicles.""",
      "high_frequency": True
    },
    {
      "article_number": 680,
      "title": "Swimming Pools, Spas, Hot Tubs, Fountains",
      "summary": """Article 680 contains very specific and critical rules for electrical installations around water – to prevent electric shock drowning and other hazards. It covers bonding of all metal parts in and around pools/spas.""",
      "high_frequency": True
    },
    {
      "article_number": 690,
      "title": "Solar Photovoltaic (PV) Systems",
      "summary": """Article 690 is a comprehensive article for solar electric systems. It spans PV module wiring, inverters, disconnects, and safety devices.""",
      "high_frequency": True
    },
    {
      "article_number": 700,
      "title": "Emergency Systems",
      "summary": """Article 700 covers those parts of an electrical system intended to supply power to essential safety loads in an emergency – things like egress (exit) lighting, fire alarm systems, hospital emergency power, etc.""",
      "high_frequency": True
    }
  ],
  "Theory_topics": [
    {
      "title": "Alternating Current (AC) Fundamentals",
      "category": "Foundational",
      "explanation": """Alternating Current (AC) is an electric current that periodically reverses direction, unlike Direct Current (DC) which flows in only one direction. In most power systems, AC follows a sinusoidal wave form – voltage and current rise and fall in a sine wave pattern, switching polarity at a fixed frequency (60 Hz in the US, meaning 60 cycles per second).""",
      "equations": [
        "V_{rms} = 0.707 \\times V_{peak}",
        "f = \\frac{1}{T}",
        "v(t) = V_{peak} \\sin(2\\pi f t)"
      ]
    },
    {
      "title": "Grounding vs. Bonding Basics",
      "category": "Foundational",
      "explanation": """Grounding and bonding are safety principles that often confuse people. Grounding typically means connecting part of the electrical system to the earth itself (true ground). For instance, the neutral of a service is grounded – tied to earth via ground rods, water pipes, etc.""",
      "equations": []
    },
    {
      "title": "AC Reactance and Impedance",
      "category": "Advanced",
      "explanation": """In AC circuits, especially those with inductors or capacitors, resistors are not the only opposition to current – we also have reactance. Inductive reactance (X_L) is the opposition an inductor provides to AC, measured in ohms. It increases with frequency: a coil has X_L = 2π f L, meaning at higher frequency or with a larger inductance L, it's harder for AC to flow.""",
      "equations": [
        "X_L = 2\\pi f L",
        "X_C = \\frac{1}{2\\pi f C}",
        "Z = \\sqrt{R^2 + (X_L - X_C)^2}"
      ]
    },
    {
      "title": "AC Power and Power Factor",
      "category": "Advanced",
      "explanation": """AC power comes in three flavors: real power (P) measured in watts (W), reactive power (Q) measured in volt-amperes reactive (VAR), and apparent power (S) measured in volt-amperes (VA). Real power is actual work done (heat, motion, light), whereas reactive power oscillates between source and load.""",
      "equations": [
        "P = V I \\cos\\phi",
        "Q = V I \\sin\\phi",
        "PF = \\frac{P}{S} = \\cos\\phi",
        "S = \\sqrt{P^2 + Q^2}"
      ]
    },
    {
      "title": "Three-Phase Power Systems",
      "category": "Advanced",
      "explanation": """Three-phase power systems use three AC voltages, phased 120° apart, to deliver power more efficiently, especially for motors and heavy loads. In a three-phase system, we often talk about line-to-line voltages (e.g., 208 V, 480 V) and line currents.""",
      "equations": [
        "V_{LL} = \\sqrt{3} \\; V_{LN}",
        "P_{3\\phi} = \\sqrt{3} \\, V_{LL} \\, I_{L} \\, \\cos\\phi",
        "I_{phase} = I_{line} \\text{ (wye connection)}"
      ]
    },
    {
      "title": "Transformers",
      "category": "Advanced",
      "explanation": """Transformers are devices that transfer AC power between circuits through electromagnetic induction, usually changing the voltage in the process. Key principles: The ratio of the voltages equals the ratio of the turns on the coils.""",
      "equations": [
        "\\frac{V_p}{V_s} = \\frac{N_p}{N_s} = \\frac{I_s}{I_p}",
        "P_{primary} \\approx P_{secondary} = V_p I_p = V_s I_s",
        "I_{secondary} = \\frac{V_p}{V_s} I_{primary}"
      ]
    },
    {
      "title": "Electric Motors",
      "category": "Advanced",
      "explanation": """Electric motors convert electrical energy into mechanical work. For AC motors (like the common three-phase induction motor), several concepts are important: synchronous speed – the speed of the rotating magnetic field, given by 120 * frequency / number of poles.""",
      "equations": [
        "n_{sync} = \\frac{120 f}{P}\\text{ (speed in RPM)}",
        "1 \\text{ hp} = 746 \\text{ W}",
        "T (\\text{lb-ft}) = \\frac{5252 \\times \\text{hp}}{n(\\text{RPM})}"
      ]
    },
    {
      "title": "Voltage Drop Calculations",
      "category": "Foundational",
      "explanation": """Voltage drop is the reduction in voltage as current flows through the resistance of conductors. While the NEC doesn't always mandate voltage drop limits in every scenario, it provides recommended practices (often aiming for no more than 3% drop on a branch circuit and 5% overall).""",
      "equations": [
        "V_{drop} = I \\times R_{total}",
        "R_{total} = 2 \\times R_{per\\_ft} \\times L \\text{ (for round-trip length)}",
        "%V_{drop} = \\frac{V_{drop}}{V_{source}} \\times 100\\%"
      ]
    }
  ]
}

def format_nec_content(article):
    """Format NEC article content for database storage"""
    html_content = f"""
    <h3>Article {article['article_number']} - {article['title']}</h3>
    <p>{article['summary']}</p>
    """
    
    if article.get('high_frequency', False):
        html_content += "<p><strong>Note:</strong> This is a high-frequency topic that appears regularly on exams.</p>"
        
    return html_content

def format_theory_content(topic):
    """Format theory topic content for database storage"""
    html_content = f"""
    <h3>{topic['title']}</h3>
    <p>{topic['explanation']}</p>
    """
    
    if topic.get('equations'):
        html_content += "<h4>Key Equations:</h4><ul>"
        for equation in topic['equations']:
            html_content += f"<li><code>{equation}</code></li>"
        html_content += "</ul>"
        
    return html_content

def populate_remaining_nec_articles():
    """Populate the database with remaining NEC articles"""
    articles_added = 0
    articles_skipped = 0
    
    print("Populating Remaining NEC Articles...")
    
    for article_data in DATA.get('NEC_articles', []):
        # Check if article already exists
        existing_article = NECArticle.query.filter_by(
            article_number=article_data['article_number']).first()
        
        if existing_article:
            # Update existing article with any new information
            if existing_article.title != article_data['title'] or existing_article.summary != article_data['summary']:
                existing_article.title = article_data['title']
                existing_article.summary = article_data['summary']
                existing_article.content = format_nec_content(article_data)
                db.session.add(existing_article)
                print(f"Updated existing article: {article_data['article_number']} - {article_data['title']}")
                articles_added += 1
            else:
                print(f"Skipping unchanged article: {article_data['article_number']} - {article_data['title']}")
                articles_skipped += 1
            continue
        
        # Create new article
        new_article = NECArticle(
            article_number=article_data['article_number'],
            title=article_data['title'],
            summary=article_data['summary'],
            content=format_nec_content(article_data)
        )
        
        db.session.add(new_article)
        articles_added += 1
        print(f"Added article: {article_data['article_number']} - {article_data['title']}")
    
    try:
        db.session.commit()
        print(f"Successfully added/updated {articles_added} NEC articles ({articles_skipped} skipped)")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding NEC articles: {e}")

def populate_remaining_theory_topics():
    """Populate the database with remaining theory topics"""
    topics_added = 0
    topics_skipped = 0
    
    print("Populating Remaining Theory Topics...")
    
    for topic_data in DATA.get('Theory_topics', []):
        # Check if topic already exists
        existing_topic = TheoryTopic.query.filter_by(
            title=topic_data['title']).first()
        
        if existing_topic:
            # Update existing topic with any new information
            if existing_topic.category != topic_data['category']:
                existing_topic.category = topic_data['category']
                existing_topic.content = format_theory_content(topic_data)
                db.session.add(existing_topic)
                print(f"Updated existing topic: {topic_data['title']}")
                topics_added += 1
            else:
                print(f"Skipping unchanged topic: {topic_data['title']}")
                topics_skipped += 1
            continue
        
        # Create new topic
        new_topic = TheoryTopic(
            title=topic_data['title'],
            category=topic_data['category'],
            content=format_theory_content(topic_data)
        )
        
        db.session.add(new_topic)
        topics_added += 1
        print(f"Added topic: {topic_data['title']}")
    
    try:
        db.session.commit()
        print(f"Successfully added/updated {topics_added} theory topics ({topics_skipped} skipped)")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding theory topics: {e}")

def main():
    # Create app and push context
    app = create_app()
    with app.app_context():
        try:
            # Populate NEC articles
            populate_remaining_nec_articles()
            
            # Populate electrical theory topics
            populate_remaining_theory_topics()
            
            print("Remaining data population complete!")
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 
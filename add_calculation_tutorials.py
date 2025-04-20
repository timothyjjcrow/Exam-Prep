#!/usr/bin/env python3
import json
from app import create_app, db
from models import CalculationTutorial

# Data for calculation tutorials
DATA = {
  "calculation_tutorials": [
    {
      "title": "Voltage Drop Calculation",
      "content": "<h3>Overview</h3>\n<p><strong>Voltage drop</strong> is the reduction in voltage as electricity flows through conductors due to resistance. Excessive voltage drop can cause dim lights or poor equipment performance. The NEC (National Electrical Code) does not mandate a maximum voltage drop, but it provides an <em>Informational Note</em> recommending a drop of no more than 3% on branch circuits and 5% overall (feeder + branch) for efficiency.</p>\n<h3>Formula and Key Concepts</h3>\n<p>The basic formula for voltage drop in a DC or single-phase AC circuit is <code>V_drop = I * R_total</code>, where <code>I</code> is the current and <code>R_total</code> is the total resistance of the conductors (round-trip). For a two-conductor circuit (out and back), an extended formula is often used:</p>\n<p><code>V_drop = 2 * L * I * R_cable_per_ft</code>, where <code>L</code> is the one-way length of the run (in feet) and <code>R_cable_per_ft</code> is the resistance per foot of the conductor (ohms per foot). The factor 2 accounts for the complete circuit (out and back).</p>\n<p>The percentage voltage drop is calculated as <code>%V_drop = (V_drop / V_source) * 100%</code>. If this percentage exceeds recommendations, a larger conductor or shorter run is needed.</p>\n<h3>Step-by-Step Calculation</h3>\n<ol>\n  <li><strong>Determine the load current (I).</strong> For example, if you have a 120 V circuit with a 15 A load, <code>I = 15 A</code>.</li>\n  <li><strong>Find the conductor resistance.</strong> Use wire resistance data (for copper at standard temperatures, #14 AWG is about 2.525 Ω per 1000 ft, #12 AWG about 1.588 Ω per 1000 ft, etc.). Calculate the resistance for the run length. For instance, for 100 ft one-way using #12 copper: <code>R_total = 2 * 100 * (1.588 Ω/1000 ft) = 0.3176 Ω</code>.</li>\n  <li><strong>Calculate the voltage drop.</strong> <code>V_drop = I * R_total</code>. In our example, <code>V_drop = 15 A * 0.3176 Ω ≈ 4.76 V</code>.</li>\n  <li><strong>Calculate the percentage drop.</strong> <code>%V_drop = (4.76 V / 120 V) * 100% ≈ 3.97%</code>. This is slightly above the 3% guideline. To reduce it, you could use a larger gauge wire (lower resistance) or shorten the run.</li>\n</ol>\n<h3>Example and Solution</h3>\n<p>Suppose a well pump draws 10 A at 240 V and is 250 feet away from the panel. Using #10 AWG copper (approx 1.0 Ω per 1000 ft):</p>\n<ul>\n  <li>One-way length <code>L = 250 ft</code>, so round-trip <code>2L = 500 ft</code>.</li>\n  <li>Conductor resistance for 500 ft: <code>R_total = 500 ft * (1.0 Ω / 1000 ft) = 0.5 Ω</code>.</li>\n  <li>Voltage drop: <code>V_drop = 10 A * 0.5 Ω = 5 V</code>.</li>\n  <li>Percentage drop: <code>(5 V / 240 V) * 100% = 2.08%</code>, which is within the recommended 3% for a branch circuit.</li>\n</ul>\n<p>In summary, always calculate voltage drop for long runs or heavily loaded circuits and adjust conductor size as needed to keep the drop within acceptable limits for good performance.</p>",
      "related_nec_articles": "210.19(A) Informational Note, 215.2(A)(1) Informational Note"
    },
    {
      "title": "Box Fill Calculation",
      "content": "<h3>Understanding Box Fill</h3>\n<p><strong>Box fill</strong> calculations ensure that electrical outlet/switch boxes have enough volume to safely accommodate the conductors, devices, and fittings inside without overheating or damaging insulation. The NEC provides specific volume allowances per conductor based on wire gauge, and requires that the box's internal volume (in cubic inches) is at least the sum of all required conductor volumes (NEC 314.16).</p>\n<h3>Volume Allowances per Conductor</h3>\n<p>Per NEC 314.16(B), each insulated conductor (that isn't a pigtail) counts as one "fill unit" and has an assigned volume based on gauge (e.g., 2.00 in3 for #14 AWG, 2.25 in3 for #12 AWG). All ground wires together count as a single conductor (one fill unit of the largest ground wire size). Each internal clamp or support counts as one unit of the largest conductor present. Each yoke (strap) containing a device (switch, receptacle) counts as two conductor volumes of the largest wire connected to that device.</p>\n<h3>Step-by-Step Calculation</h3>\n<ol>\n  <li><strong>Identify all conductors entering the box.</strong> Include all insulated circuit conductors (hot, neutral, travelers, etc.) that originate outside and terminate or pass through, and all pigtails that originate inside and exit the box (note: pigtails that stay entirely in the box do <em>not</em> count).</li>\n  <li><strong>Count grounding conductors.</strong> All equipment grounding conductors together count as one conductor fill unit (use the largest EGC size in the box for volume).</li>\n  <li><strong>Count devices or clamps.</strong> For each switch or receptacle (device) on a strap, add two conductor units of the largest size connected to it. If the box has internal cable clamps or similar that take up space, add one conductor unit of the largest wire present for all clamps together.</li>\n  <li><strong>Determine required volume.</strong> Multiply the number of conductor units for each wire gauge by the volume per conductor (from NEC 314.16(B) Table). Sum these volumes to get the minimum cubic inches required.</li>\n  <li><strong>Choose an appropriate box.</strong> Compare the required volume to the internal volume stamped on the box (or listed in NEC 314.16(A) for standard boxes). The box's volume must be equal or greater. If not, use a larger box or a box extension.</li>\n</ol>\n<h3>Example Calculation</h3>\n<p>Consider a scenario: a box contains two 14/2 cables (each with one hot and one neutral) entering, and one 14/2 cable exiting (feed-through) – all are #14 AWG. Additionally, there is one switch in the box controlling the outgoing cable's hot. The box has an internal clamp.</p>\n<ul>\n  <li>Insulated conductors: 2 cables * 2 conductors each (incoming) + 1 cable * 2 conductors (outgoing) = 6 conductor units (all #14).</li>\n  <li>Grounds: All ground wires together = 1 unit (#14, since all cables are #14).</li>\n  <li>Device: The switch on one yoke = 2 units (#14, the hot connected to switch is #14).</li>\n  <li>Clamp: Internal clamp present = 1 unit (#14).</li>\n  <li>Total units = 6 + 1 + 2 + 1 = 10 units of #14 AWG.</li>\n  <li>Volume per #14 AWG unit = 2.00 in3 (from NEC table).</li>\n  <li>Required box volume = 10 * 2.00 in3 = 20.0 in3.</li>\n  <li>Solution: Select a box with at least 20 in3 internal volume (for instance, a standard double-gang plastic box often has around 22 in3, which would be sufficient).</li>\n</ul>\n<p>This method ensures the box is large enough to dissipate heat and accommodate wires without crowding, maintaining a safe installation as required by code.</p>",
      "related_nec_articles": "314.16(A), 314.16(B)"
    },
    {
      "title": "Conduit Fill Calculation",
      "content": "<h3>Understanding Conduit Fill</h3>\n<p><strong>Conduit fill</strong> calculations ensure that conductors can safely fit inside a conduit without exceeding space limits that could cause overheating or damage during pulling. The NEC limits the percentage of the conduit cross-sectional area that the conductors can occupy. According to NEC Chapter 9, Table 1 (notes): one conductor can fill up to 53% of a conduit, two conductors up to 31%, and three or more conductors up to 40% of the conduit's area.</p>\n<h3>Key Data from NEC Tables</h3>\n<p>To perform a conduit fill calculation, gather two key pieces of data:</p>\n<ul>\n  <li><strong>Conduit area:</strong> The internal cross-sectional area of the conduit (in square inches). Find this in NEC Chapter 9, Table 4 for the type and size of conduit.</li>\n  <li><strong>Conductor area:</strong> The cross-sectional area of each conductor or cable (in square inches), from NEC Chapter 9, Table 5 (for insulated conductors) or manufacturer specs if not standard.</li>\n</ul>\n<h3>Step-by-Step Calculation</h3>\n<ol>\n  <li><strong>List conductors and sizes:</strong> Identify each conductor or cable going in the conduit, including AWG size and insulation type (e.g., three #12 THHN wires).</li>\n  <li><strong>Find each conductor's area:</strong> From NEC Chapter 9, Table 5, look up the area for each conductor type and size. For example, #12 AWG THHN is about 0.0133 in2 per conductor.</li>\n  <li><strong>Sum the areas:</strong> Add up the areas of all conductors to get a total fill area. If using multi-conductor cables in a conduit, use the cable's overall area (if allowed in conduit).</li>\n  <li><strong>Determine allowable fill:</strong> Based on the number of conductors, apply the fill percentage (1=53%, 2=31%, ≥3=40%). Multiply the conduit's internal area by this percentage to get the maximum permitted fill area.</li>\n  <li><strong>Select conduit size:</strong> Choose a conduit with an internal area that meets or exceeds the required area. In practice, you might try a size and check: if the conductor total area is less than the max fill for that conduit, it works; if not, go up a size.</li>\n</ol>\n<h3>Example Calculation</h3>\n<p>Suppose we need to run four #10 AWG THHN copper conductors in EMT (Electrical Metallic Tubing).</p>\n<ul>\n  <li>Area of #10 THHN: ~0.0211 in2 each.</li>\n  <li>Total area for 4 conductors: 4 * 0.0211 = 0.0844 in2.</li>\n  <li>With 4 conductors, max fill = 40% of conduit area.</li>\n  <li>Check 1/2-inch EMT (internal area ~0.304 in2): 40% of 0.304 = 0.1216 in2 allowed. Our 0.0844 in2 need is below 0.1216 in2, so 1/2-inch EMT is sufficient.</li>\n  <li>If the needed area had exceeded 0.1216 in2, we would try 3/4-inch EMT (internal ~0.533 in2; 40% = 0.213 in2, etc.).</li>\n</ul>\n<p>Following these steps ensures the conduit is not overfilled, preventing excessive heat buildup and making wire pulls easier and safer, in compliance with NEC conduit fill rules.</p>",
      "related_nec_articles": "Chapter 9, Table 1; Table 4; Table 5"
    }
  ]
}

def populate_calculation_tutorials():
    """Populate the database with calculation tutorials"""
    tutorials_added = 0
    tutorials_skipped = 0
    
    print("Populating Calculation Tutorials...")
    
    for tutorial_data in DATA.get('calculation_tutorials', []):
        # Check if tutorial already exists
        existing_tutorial = CalculationTutorial.query.filter_by(
            title=tutorial_data['title']).first()
        
        if existing_tutorial:
            # Update existing tutorial with any new information
            if existing_tutorial.content != tutorial_data['content'] or existing_tutorial.related_nec_articles != tutorial_data.get('related_nec_articles', ''):
                existing_tutorial.content = tutorial_data['content']
                existing_tutorial.related_nec_articles = tutorial_data.get('related_nec_articles', '')
                db.session.add(existing_tutorial)
                print(f"Updated existing tutorial: {tutorial_data['title']}")
                tutorials_added += 1
            else:
                print(f"Skipping unchanged tutorial: {tutorial_data['title']}")
                tutorials_skipped += 1
            continue
        
        # Create new tutorial
        new_tutorial = CalculationTutorial(
            title=tutorial_data['title'],
            content=tutorial_data['content'],
            related_nec_articles=tutorial_data.get('related_nec_articles', '')
        )
        
        db.session.add(new_tutorial)
        tutorials_added += 1
        print(f"Added tutorial: {tutorial_data['title']}")
    
    try:
        db.session.commit()
        print(f"Successfully added/updated {tutorials_added} calculation tutorials ({tutorials_skipped} skipped)")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding calculation tutorials: {e}")

def main():
    # Create app and push context
    app = create_app()
    with app.app_context():
        try:
            # Populate calculation tutorials
            populate_calculation_tutorials()
            
            print("Calculation tutorials population complete!")
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 
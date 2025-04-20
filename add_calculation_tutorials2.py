#!/usr/bin/env python3
import json
from app import create_app, db
from models import CalculationTutorial

# Data for calculation tutorials (part 2)
DATA = {
  "calculation_tutorials": [
    {
      "title": "General Lighting and Receptacle Load Calculations",
      "content": "<h3>Overview</h3>\n<p>General lighting and receptacle loads in dwelling units are calculated based on floor area as specified by the NEC. Rather than counting each receptacle or fixture wattage, the code assigns a standard unit load per square foot. This provides a baseline for sizing circuits and the service.</p>\n<h3>Unit Load per Square Foot</h3>\n<p>NEC 220.12 requires a general lighting load of <strong>3 volt-amperes (VA) per square foot</strong> for dwelling units. This covers general-use receptacles and lighting outlets. To compute the load:</p>\n<ul>\n  <li><strong>Determine floor area:</strong> Calculate the floor area in square feet (using outside dimensions, excluding garages, porches, and unused or unfinished areas).</li>\n  <li><strong>Multiply by 3 VA:</strong> e.g., a 1200 sq ft house: <code>1200 sq ft * 3 VA/sq ft = 3600 VA</code> of general load.</li>\n</ul>\n<h3>Small Appliance and Laundry Circuits</h3>\n<p>In addition to the 3 VA/sq ft general load, the code mandates specific circuits for kitchen and laundry that must be included:</p>\n<ul>\n  <li><strong>Kitchen Small-Appliance Circuits:</strong> At least two 20A circuits for kitchen/dining (NEC 210.11(C)(1)), each counted as 1500 VA (NEC 220.52(A)). So two circuits add <code>2 * 1500 VA = 3000 VA</code>.</li>\n  <li><strong>Laundry Circuit:</strong> One 20A laundry circuit (NEC 210.11(C)(2)), counted as 1500 VA (NEC 220.52(B)).</li>\n</ul>\n<p>Add these loads to the general lighting load.</p>\n<h3>Demand Factor for General Loads</h3>\n<p>NEC 220.42 permits a demand factor because not all lights/outlets are used at once. For dwellings, you take 100% of the first 3000 VA of these combined loads, and 35% of the rest.</p>\n<p><em>Example:</em> For a 1200 sq ft house: General 3600 VA + Small appliance/laundry 4500 VA = 8100 VA. Demand: first 3000 VA at 100% = 3000 VA; remaining 5100 VA at 35% = 1785 VA. Total = 4785 VA effective load for service calculation.</p>\n<h3>Circuit-Level Considerations</h3>\n<p>When designing individual branch circuits, 15A or 20A circuits are typical for lighting and receptacles. The 3 VA/sq ft calculation is for service load calc, not for counting receptacles per circuit. However, a design rule of thumb often used is 180 VA per receptacle (as in commercial calcs). For a 20A circuit (2400 VA at 120V), that suggests a maximum of 13 receptacles. This is not an NEC requirement for dwellings, but it helps ensure circuits are not overloaded in practice.</p>\n<p>By using the code's unit loads and demand factors, you can accurately estimate the contribution of lighting and receptacles to a dwelling's total load and size the service and feeders appropriately.</p>",
      "related_nec_articles": "220.12, 220.42, 220.52, 210.11(C)"
    },
    {
      "title": "Appliance Circuit Load Calculations (Ranges, Dryers, etc.)",
      "content": "<h3>Overview</h3>\n<p>Large appliances (ranges, ovens, dryers, water heaters, etc.) often have dedicated circuits and significant loads. The NEC provides specific calculation methods and demand factors for these when sizing the service or feeders. Also, branch circuit requirements ensure each appliance circuit is properly sized.</p>\n<h3>Electric Range Calculation</h3>\n<p>For household cooking appliances, NEC 220.55 provides demand factors. A single range is typically counted at its nameplate rating for a dwelling load calc, but ranges over 8.75 kW can be derated. For example, a 12 kW range can be counted as 8 kW (per Table 220.55, note for Column C) in the service load calculation.</p>\n<p>Branch circuit: A 12 kW range at 240 V draws 50 A, so a 50 A breaker with #6 AWG copper is a typical branch circuit.</p>\n<h3>Clothes Dryer Calculation</h3>\n<p>NEC 220.54 specifies at least 5000 VA (5 kW) for an electric dryer (or the nameplate if higher). This is taken at 100% for one dryer in a dwelling. (If multiple dryers in multifamily, demand factors apply, but not for a single dwelling.)</p>\n<p>Branch circuit: A 5 kW, 240 V dryer draws ~21 A. A 30 A breaker with #10 AWG copper is typical. (125% of 21 A = 26.25 A, so 30 A is fine.)</p>\n<h3>Water Heater and Other Appliances</h3>\n<p>An electric water heater (e.g., 4500 W at 240 V ~ 18.75 A) is often treated as a continuous load (if on >3 hours). Branch circuit = 125% * 18.75 A = 23.4 A, so use a 25 or 30 A breaker with #10 AWG. In service calc, use 4.5 kVA at 100%. If you have 4 or more fixed appliances (fastened in place) on top of those already counted, NEC 220.53 allows a 75% demand on their total.</p>\n<h3>HVAC Appliances</h3>\n<p>Large appliances include HVAC equipment like furnaces or heat pumps. Electric heat (strip heat) is usually continuous and taken at 100% (no demand reduction). Air conditioning is calculated by motor rules or using the nameplate (MCA and max fuse). We typically include the larger of heating or cooling in the service calculation, not both.</p>\n<h3>Example Calculation</h3>\n<p>Consider a dwelling with: one 8 kW range, one 5 kW dryer, one 4.5 kW water heater, and a 1 kW dishwasher.</p>\n<ul>\n  <li>Range: 8 kW (under 8.75, so no reduction; count 8 kW).</li>\n  <li>Dryer: 5 kW.</li>\n  <li>Water heater: 4.5 kW.</li>\n  <li>Dishwasher: 1 kW (fastened in place).</li>\n  <li>Total appliance load = 8 + 5 + 4.5 + 1 = 18.5 kW (18,500 VA).</li>\n  <li>Demand factors: Range at 8 (no reduction needed), Dryer at 5, other appliances (DW+WH = 5.5 kW, only 2 appliances so 75% rule not applicable).</li>\n  <li>Service load contribution = 18.5 kW.</li>\n  <li>Service current: 18,500 VA / 240 V ≈ 77 A (this portion).</li>\n  <li>Branch circuits: Range on 50 A, Dryer on 30 A, Water heater on 30 A, Dishwasher on 15 or 20 A.</li>\n</ul>\n<p>Following NEC guidelines for appliance loads ensures both branch circuits and the overall service are sized to handle these loads safely.</p>",
      "related_nec_articles": "220.55, 220.54, 220.53"
    },
    {
      "title": "Dwelling Unit Service Load Calculation (Standard Method)",
      "content": "<h3>Overview</h3>\n<p>The <strong>Standard Method</strong> for sizing a dwelling unit service or feeder (NEC 220 Part III) accounts for all loads with various demand factors. It is detailed and often yields a higher calculated load than the optional method. Below is a step-by-step outline:</p>\n<h3>Step-by-Step (Standard Method)</h3>\n<ol>\n  <li><strong>General Lighting/Receptacles:</strong> 3 VA per sq ft of living space (NEC 220.12) plus 1500 VA for each small-appliance circuit (2 minimum) and 1500 VA for laundry (NEC 220.52). Sum these. Apply demand: 100% of first 3000 VA, 35% of the rest (NEC 220.42).</li>\n  <li><strong>Appliances:</strong> Include all fixed appliances (dishwasher, disposal, microwave, etc.) at nameplate. If there are 4 or more (not counting those already required circuits), apply 75% to their total (NEC 220.53).</li>\n  <li><strong>Clothes Dryer:</strong> Add 5000 VA (or nameplate if larger) for a dryer (NEC 220.54).</li>\n  <li><strong>Cooking Equipment:</strong> Add ranges/ovens. Use demand from NEC 220.55. (One typical range: use its rating, or if over 8.75 kW, use permitted demand value.)</li>\n  <li><strong>Largest HVAC Load:</strong> Add the larger of heating vs cooling. If electric heat vs AC, include the one with greater amperage (NEC 220.60). For heat pumps with electric strip heat, include compressor + 25% of largest motor or per nameplate MCA.</li>\n  <li><strong>Other Loads:</strong> Include water heater, well pump, EV charger, etc., at 100%. Also add 25% of the largest motor load (NEC 220.50) if not already accounted for in HVAC (this often covers a well pump or AC compressor extra starting load).</li>\n</ol>\n<h3>Total and Service Size</h3>\n<p>Sum all the above adjusted loads (in VA). Divide by the service voltage (240 V for single-phase) to get amperage. Choose a service disconnect and conductor size that meets/exceeds this ampacity (round up to standard breaker size per NEC 240.6).</p>\n<h3>Example</h3>\n<p>For a 1500 sq ft home with typical loads:</p>\n<ul>\n  <li>General load: 1500 * 3 = 4500 VA; +2 small app (3000) + laundry (1500) = 9000 VA; demand: 3000 + 35% of 6000 = 3000 + 2100 = 5100 VA.</li>\n  <li>Appliances: dishwasher 1200, disposal 800 = 2000 VA (only 2 appliances, no 75% reduction).</li>\n  <li>Dryer: 5000 VA.</li>\n  <li>Range: 8 kW = 8000 VA.</li>\n  <li>HVAC: AC 3500 VA vs electric heat 6000 VA – use 6000 VA (heat larger).</li>\n  <li>Water heater: 4500 VA.</li>\n  <li>Largest motor: AC compressor ~3500 VA, add 25% = 875 VA.</li>\n  <li>Total ≈ 5100 + 2000 + 5000 + 8000 + 6000 + 4500 + 875 = 31,475 VA.</li>\n  <li>Service at 240 V: 31,475 VA / 240 V ≈ 131 A → choose a 150 A service (next standard size), with appropriate conductors (e.g., 1/0 Cu or 3/0 Al).</li>\n</ul>\n<p>The standard method ensures the service is sized for worst-case demand, providing a safety margin for the installation.</p>",
      "related_nec_articles": "220.12, 220.42, 220.52, 220.53, 220.54, 220.55, 220.60, 220.50"
    },
    {
      "title": "Dwelling Unit Service Load Calculation (Optional Method)",
      "content": "<h3>Overview</h3>\n<p>The <strong>Optional Method</strong> (NEC 220.82) is a simplified calculation for a dwelling unit's service or feeder load. It often results in a lower calculated load than the standard method by taking broad demand reductions. It applies if you have a single dwelling unit service/feed of 100A or larger (120/240V or 120/208V).</p>\n<h3>Step-by-Step (Optional Method)</h3>\n<ol>\n  <li><strong>Sum all base loads (minus HVAC):</strong> Add up the general lighting/receptacle load (3 VA/sq ft), plus 2 small-appliance circuits (3000 VA) and laundry (1500 VA), plus all appliances (range, dryer, water heater, etc.) at their nameplate VA, plus any other loads (well pump, etc.). This gives the total non-HVAC load.</li>\n  <li><strong>Apply demand factor to base load:</strong> Take 100% of the first 10 kVA of that total, and 40% of the remainder (NEC 220.82(B)). This reduction accounts for load diversity in a simpler way than the standard method.</li>\n  <li><strong>Add largest HVAC load:</strong> Determine the larger of the heating or cooling load and add it on (NEC 220.82(C)). For example, if you have either a 5 kW AC or an 8 kW electric heat, add whichever is bigger after any allowed reduction (for electric heat, up to 65% if certain conditions). For heat pumps with electric strip heat, add 100% of the compressor + 65% of the strip heat if that combination is the worst case.</li>\n  <li><strong>Calculate service size:</strong> Add the results of step 2 and 3 to get the total calculated VA, then divide by service voltage (240 V) to find amperage. Select the next standard breaker size at or above this amperage (NEC 240.6) and size conductors accordingly (NEC 310.12 for dwelling services).</li>\n</ol>\n<h3>Example</h3>\n<p>For a 2000 sq ft house with: general load 3 VA/ sq ft, two small appliance circuits, one laundry, 5 kW range, 5 kW dryer, 4.5 kW water heater, 1 kW dishwasher, and either 5 kW AC or 8 kW heat:</p>\n<ul>\n  <li>Non-HVAC load: 2000 * 3 = 6000 VA; +3000 (SA circuits) +1500 (laundry) +5000 (range) +5000 (dryer) +4500 (WH) +1000 (DW) = 26,000 VA.</li>\n  <li>Demand on non-HVAC: 10,000 VA @100% = 10,000; remaining 16,000 @40% = 6400; subtotal = 16,400 VA.</li>\n  <li>HVAC: AC = 5000 VA, Heat = 8000 VA (if electric, can reduce to 65% = 5200 VA). The larger effective load is 5200 VA (heat wins).</li>\n  <li>Total load = 16,400 + 5200 = 21,600 VA.</li>\n  <li>Service current = 21,600 / 240 = 90 A → a 100 A service can handle this.</li>\n</ul>\n<p>Using the optional method acknowledges that not all loads run at once and gives a more forgiving calculation for service size, as long as the dwelling qualifies for this method.</p>",
      "related_nec_articles": "220.82, 220.85"
    },
    {
      "title": "Feeder Sizing Calculation",
      "content": "<h3>Overview</h3>\n<p>A <strong>feeder</strong> is a set of conductors that supply power from the main panel (or source) to a subpanel or other distribution point. Sizing a feeder means determining the load it must carry and then selecting conductors and a breaker to handle that load safely per NEC rules.</p>\n<h3>Determining Feeder Load</h3>\n<p>First, calculate the load that the feeder will carry (in VA or amperes). This is similar to calculating a service load but just for the portion of the system the feeder supplies. For example, if a feeder supplies a subpanel for an addition or a detached garage, list all the circuits and their loads in that area (lighting at 3 VA/sq ft, appliance loads, etc.) and sum them with demand factors like a mini service calculation.</p>\n<p>Sometimes the load on a feeder is already known (e.g., a subpanel with 50 A of load at 240 V = 12,000 VA). Otherwise, perform a calculation to determine it.</p>\n<h3>Selecting Conductor Size</h3>\n<p>Once you know the load (amps), choose a conductor size with adequate ampacity. NEC 215.2(A)(1) says feeder conductors must have ampacity ≥ the load. If there are continuous loads (running >3 hours), size for 125% of those. Use NEC 310.16 to find a conductor gauge that can carry the required amps (after any adjustments for temperature or bundling).</p>\n<p>For dwelling feeders 100A or larger, NEC 310.12 allows the use of certain smaller conductors (aluminum or copper-clad) based on service cable rules (e.g., 1 AWG Al for 100A). Always verify the conductor chosen meets or exceeds the required ampacity.</p>\n<h3>Overcurrent Protection</h3>\n<p>The feeder's breaker or fuse must be rated to protect the conductors. Usually, you pick the nearest standard size at or just above the calculated load (240.6 standard sizes), ensuring it doesn't exceed the conductor's rating. For instance, a 54 A calc might use a 60 A breaker with conductors rated ≥60 A.</p>\n<h3>Example</h3>\n<p>Suppose a feeder will supply a workshop subpanel. The calculated load is 9600 VA at 240 V (40 A). The continuous load portion is 8 A of lighting.</p>\n<ul>\n  <li>Total amps = 40 A (noncontinuous + continuous).</li>\n  <li>Continuous load adjustment: 8 A * 125% = 10 A for that portion, so design load ~ (32 A noncont + 10 A cont) = 42 A.</li>\n  <li>Conductor: #8 AWG copper THHN is rated 50 A (at 75°C). That covers 42 A. If using NM cable (60°C), #8 is only 40 A, so we'd go to #6 Cu (55 A at 60°C) for safety.</li>\n  <li>Breaker: Next standard size above 42 A is 50 A. Using #6 Cu (rated 55 A) with a 50 A breaker is acceptable. (If we stuck to #8 THHN in conduit, a 50 A breaker is fine since #8 THHN = 50 A rating.)</li>\n</ul>\n<p>In summary: calculate the feeder load, adjust for continuous loads, pick conductors that handle the load (with any needed adjustments), and then choose a breaker that protects those conductors and serves the load.</p>",
      "related_nec_articles": "215.2(A)(1), 310.16, 310.12, 240.6"
    }
  ]
}

def populate_calculation_tutorials():
    """Populate the database with calculation tutorials (part 2)"""
    tutorials_added = 0
    tutorials_skipped = 0
    
    print("Populating Calculation Tutorials (Part 2)...")
    
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
            
            print("Calculation tutorials (part 2) population complete!")
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 
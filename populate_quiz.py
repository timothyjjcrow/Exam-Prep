import sys
import os
from datetime import datetime

# Add the project directory to the Python path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_dir)

# Change this line to import directly from app.py
from app import app
from models import db, PracticeQuestion

# Sample questions - list of dictionaries
sample_questions = [
    {
        "question_text": "Conductors with _____ marked on the insulation are NOT approved for use in a wet location.",
        "topic": "NEC Wiring and Protection",
        "option_a": "THW",
        "option_b": "THHW",
        "option_c": "THHN",
        "option_d": "THWN",
        "correct_option": "C",
        "explanation": "As shown in NEC Table 310.104(A), conductors with THHN insulation are approved for use in dry and damp locations only.",
        "nec_reference": "310.104(A)"
    },
    {
        "question_text": "What is the MINIMUM length of free conductor required to be left at each junction box for splicing or making connections?",
        "topic": "NEC Wiring Methods",
        "option_a": "4 inches",
        "option_b": "10 inches",
        "option_c": "8 inches",
        "option_d": "6 inches",
        "correct_option": "D",
        "explanation": "As per NEC Section 300.14, at least 6 inches of free conductor must be left at each junction box for splices or connections.",
        "nec_reference": "300.14"
    },
    {
        "question_text": "In general, overhead service-drop conductors shall NOT be smaller than _____ copper.",
        "topic": "NEC Services",
        "option_a": "2 AWG",
        "option_b": "4 AWG",
        "option_c": "6 AWG",
        "option_d": "8 AWG",
        "correct_option": "D",
        "explanation": "NEC Section 230.23(B) requires overhead service-drop conductors to be not smaller than 8 AWG copper or 6 AWG aluminum.",
        "nec_reference": "230.23(B)"
    },
    {
        "question_text": "In dwelling units, receptacle outlets installed for countertop surfaces must be located above, but NOT more than _____ above the countertop.",
        "topic": "NEC Wiring Methods",
        "option_a": "12 inches",
        "option_b": "18 inches",
        "option_c": "20 inches",
        "option_d": "24 inches",
        "correct_option": "C",
        "explanation": "In compliance with NEC Section 210.52(C)(5), receptacle outlets installed for countertop surfaces must be located not more than 20 inches above the countertop.",
        "nec_reference": "210.52(C)(5)"
    },
    {
        "question_text": "Adjustment factors for more than three current-carrying conductors in a raceway are NOT required if the raceway nipple is _____ or less in length.",
        "topic": "NEC Wiring and Protection",
        "option_a": "24 inches",
        "option_b": "30 inches",
        "option_c": "36 inches",
        "option_d": "48 inches",
        "correct_option": "A",
        "explanation": "NEC Section 310.15(B)(3)(a)(2) states that adjustment factors shall not apply where the raceway is not more than 24 inches long.",
        "nec_reference": "310.15(B)(3)(a)(2)"
    },
    {
        "question_text": "According to the NEC, fixed outdoor deicing and snow melting equipment is considered a _____ load.",
        "topic": "NEC General",
        "option_a": "Non-continuous",
        "option_b": "Intermittent",
        "option_c": "Continuous",
        "option_d": "Simultaneous",
        "correct_option": "C",
        "explanation": "As defined in Article 100 and specified in Article 426.4, fixed outdoor electric deicing and snow melting equipment shall be considered a continuous load (operating 3 hours or more).",
        "nec_reference": "426.4, Art 100"
    },
    {
        "question_text": "What is the total resistance in a parallel circuit with two resistors of 4 ohms and 6 ohms?",
        "topic": "Electrical Theory",
        "option_a": "1.5 ohms",
        "option_b": "10 ohms",
        "option_c": "2.4 ohms",
        "option_d": "5 ohms",
        "correct_option": "C",
        "explanation": "For two resistors in parallel, Rt = (R1 * R2) / (R1 + R2). So, Rt = (4 * 6) / (4 + 6) = 24 / 10 = 2.4 ohms.",
        "nec_reference": None
    },
    {
        "question_text": "You are troubleshooting a circuit and find that the voltage drop across a resistor is 12V, and the current flowing through it is 2A. What is the resistance of the resistor?",
        "topic": "Electrical Theory",
        "option_a": "6 ohms",
        "option_b": "10 ohms",
        "option_c": "24 ohms",
        "option_d": "14 ohms",
        "correct_option": "A",
        "explanation": "Using Ohm's Law (R = V / I), R = 12V / 2A = 6 ohms.",
        "nec_reference": None
    },
    {
        "question_text": "What is the color code for a ground wire in a typical residential electrical system in the United States?",
        "topic": "NEC General",
        "option_a": "Red",
        "option_b": "Black",
        "option_c": "Blue",
        "option_d": "Green",
        "correct_option": "D",
        "explanation": "Green (or bare copper) is the standard color code for equipment grounding conductors in the US.",
        "nec_reference": "250.119"
    },
    {
        "question_text": "What is the minimum required working space depth in front of an electrical panel rated 600 volts or less (Condition 1: exposed live parts on one side and no live or grounded parts on the other side)?",
        "topic": "NEC Wiring Methods",
        "option_a": "2 feet",
        "option_b": "3 feet",
        "option_c": "4 feet",
        "option_d": "5 feet",
        "correct_option": "B",
        "explanation": "According to NEC Table 110.26(A)(1), the minimum required working space depth for Condition 1 is 3 feet for systems 0-150 volts to ground.",
        "nec_reference": "110.26(A)(1)"
    },
    {
        "question_text": "Which tool is commonly used to measure the current flowing through an electrical circuit without breaking the circuit?",
        "topic": "Tools and Safety",
        "option_a": "Voltmeter",
        "option_b": "Clamp-on Ammeter",
        "option_c": "Ohmmeter",
        "option_d": "Megohmmeter",
        "correct_option": "B",
        "explanation": "A clamp-on ammeter measures current by sensing the magnetic field around a conductor, allowing measurement without interrupting the circuit.",
        "nec_reference": None
    },
    {
        "question_text": "What is the formula to calculate electrical power (P) when voltage (V) and current (I) are known?",
        "topic": "Electrical Theory",
        "option_a": "P = I / V",
        "option_b": "P = V / I",
        "option_c": "P = I * V",
        "option_d": "P = I * R",
        "correct_option": "C",
        "explanation": "The basic formula for electrical power is Power = Current * Voltage (P = IV).",
        "nec_reference": None
    },
    {
        "question_text": "What is the primary purpose of grounding in an electrical system?",
        "topic": "NEC Grounding and Bonding",
        "option_a": "To increase electrical efficiency",
        "option_b": "To ensure user safety",
        "option_c": "To boost voltage levels",
        "option_d": "To reduce electrical noise",
        "correct_option": "B",
        "explanation": "Grounding provides a safe path for fault current to flow, preventing dangerous voltages on equipment enclosures and minimizing shock hazards.",
        "nec_reference": "Art 250"
    },
    {
        "question_text": "What is the minimum size copper equipment grounding conductor required for a 60-ampere branch circuit?",
        "topic": "NEC Grounding and Bonding",
        "option_a": "14 AWG",
        "option_b": "12 AWG",
        "option_c": "10 AWG",
        "option_d": "8 AWG",
        "correct_option": "C",
        "explanation": "According to NEC Table 250.122, a 60-ampere circuit requires a minimum 10 AWG copper equipment grounding conductor.",
        "nec_reference": "250.122"
    },
    {
        "question_text": "Calculate the total load in Volt-Amperes for general illumination for a 2500 square foot dwelling unit.",
        "topic": "Load Calculations",
        "option_a": "2500 VA",
        "option_b": "5000 VA",
        "option_c": "7500 VA",
        "option_d": "9000 VA",
        "correct_option": "C",
        "explanation": "NEC Table 220.12 specifies 3 VA per square foot for dwelling units. 2500 sq ft * 3 VA/sq ft = 7500 VA.",
        "nec_reference": "220.12"
    },
    {
        "question_text": "A 120V circuit breaker rated at 20 amperes will trip if the continuous load exceeds what value?",
        "topic": "NEC Overcurrent Protection",
        "option_a": "16 amperes",
        "option_b": "20 amperes",
        "option_c": "24 amperes",
        "option_d": "25 amperes",
        "correct_option": "A",
        "explanation": "For continuous loads (3 hours or more), branch circuits and overcurrent devices are rated at 80% of their capacity. 20A * 80% = 16A.",
        "nec_reference": "210.20(A)"
    },
    {
        "question_text": "3-phase advantages over single-phase: 1) More efficient power delivery (for same power, conductors can be smaller), 2) For motors, smoother starting and running (no 'dead spots'), 3) Constant power delivery (single-phase power delivery pulsates, 3-phase is constant), 4) Can deliver both 3-phase and single-phase loads from same system. So a 3-phase 208Y/120V system can power 3-phase motors and 120V single-phase loads. For the same power, 3-phase needs less copper. Most large commercial and industrial buildings use 3-phase for these efficiency reasons.",
        "topic": "3-Phase Power Systems",
        "option_a": "N/A",
        "option_b": "N/A",
        "option_c": "N/A",
        "option_d": "N/A",
        "correct_option": "N/A",
        "explanation": "3-phase advantages over single-phase: 1) More efficient power delivery (for same power, conductors can be smaller), 2) For motors, smoother starting and running (no 'dead spots'), 3) Constant power delivery (single-phase power delivery pulsates, 3-phase is constant), 4) Can deliver both 3-phase and single-phase loads from same system. So a 3-phase 208Y/120V system can power 3-phase motors and 120V single-phase loads. For the same power, 3-phase needs less copper. Most large commercial and industrial buildings use 3-phase for these efficiency reasons.",
        "nec_reference": "N/A"
    },
    
    # Boxes and Enclosures questions
    {
        "question_text": "According to the NEC, what is the minimum depth required for a box containing one or more devices and #14 or #12 conductors?",
        "topic": "Boxes and Enclosures",
        "option_a": "1-1/4 inches (31.8 mm)",
        "option_b": "1-3/8 inches (35.0 mm)",
        "option_c": "1-1/2 inches (38.1 mm)",
        "option_d": "1-5/8 inches (41.3 mm)",
        "correct_option": "C",
        "explanation": "NEC 314.24(B)(4) specifies that boxes containing one or more devices (like switches or receptacles) mounted with their mounting yokes or other accessories must have a minimum depth of 1-1/2 inches (38.1 mm) when containing #14 or #12 conductors. This ensures adequate space for the device and wiring. Shallower boxes wouldn't provide enough room for proper wiring connections.",
        "nec_reference": "314.24(B)(4)"
    },
    {
        "question_text": "When installing an electrical box for a wall-mounted luminaire (light fixture), what is the maximum weight the box can support unless it is listed for a higher weight?",
        "topic": "Boxes and Enclosures",
        "option_a": "35 pounds",
        "option_b": "50 pounds",
        "option_c": "75 pounds",
        "option_d": "100 pounds",
        "correct_option": "B",
        "explanation": "According to NEC 314.27(A)(2), an outlet box used for the support of a luminaire (lighting fixture) mounted on a wall must be designed for the purpose and shall be capable of supporting a luminaire weighing at least 50 pounds, unless the box is listed and marked for a higher weight. This 50-pound rating is for wall-mounted fixtures. For ceiling-mounted fixtures, the same 50-pound standard applies per 314.27(A)(1).",
        "nec_reference": "314.27(A)(2)"
    },
    {
        "question_text": "What is the minimum working space clearance required in front of electrical equipment operating at 208 volts that may require examination, adjustment, or servicing while energized?",
        "topic": "Boxes and Enclosures",
        "option_a": "3 feet (900 mm)",
        "option_b": "3.5 feet (1.1 m)",
        "option_c": "4 feet (1.2 m)",
        "option_d": "5 feet (1.5 m)",
        "correct_option": "A",
        "explanation": "NEC 110.26(A)(1) specifies the minimum working space in the direction of access to live parts operating at 600 volts or less. For equipment operating at 0-150 volts to ground (which includes 208V single-phase), Condition 1 requires a minimum of 3 feet (900 mm) of clearance. This space must be clear, not used for storage, and must allow for safe operation and maintenance of the electrical equipment while energized.",
        "nec_reference": "110.26(A)(1)"
    },
    {
        "question_text": "What is the primary purpose of electrical box 'fill calculations' according to the NEC?",
        "topic": "Boxes and Enclosures",
        "option_a": "To ensure there is sufficient wire bending space",
        "option_b": "To prevent overheating of conductors due to overcrowding",
        "option_c": "To make installation and future maintenance easier",
        "option_d": "All of the above",
        "correct_option": "D",
        "explanation": "Box fill calculations serve multiple purposes as outlined in NEC 314.16. They ensure: 1) Sufficient space for conductors to be bent without damage to insulation, 2) Adequate heat dissipation to prevent overheating, 3) Proper space for installation and future maintenance/modifications, and 4) Compliance with safety standards. Overcrowded boxes can lead to damaged insulation, overheating, difficult installations, and potential short circuits. The code provides specific volume requirements based on conductor sizes and quantities.",
        "nec_reference": "314.16"
    },
    {
        "question_text": "According to the NEC, in what locations are electrical panels (panelboards) prohibited from being installed?",
        "topic": "Boxes and Enclosures",
        "option_a": "In bathrooms",
        "option_b": "In clothes closets",
        "option_c": "Over steps of a stairway",
        "option_d": "All of the above",
        "correct_option": "D",
        "explanation": "NEC 240.24(D), (E), and (F) prohibit overcurrent devices (including panelboards) in all three locations listed. They are not permitted in bathrooms of dwelling units or guest rooms/suites of hotels/motels (240.24(E)), in clothes closets where they could be obstructed by the door or other contents (240.24(D)), or over steps of a stairway (240.24(F)). These restrictions are safety measures to ensure panels remain accessible and are not installed where they might create hazards or be difficult to access in emergencies.",
        "nec_reference": "240.24(D)(E)(F)"
    },
    {
        "question_text": "What is the minimum burial depth required for rigid nonmetallic conduit (Schedule 40 PVC) containing a feeder circuit protected at 60 amps under a residential driveway?",
        "topic": "Raceways and Enclosures",
        "option_a": "12 inches (300 mm)",
        "option_b": "18 inches (450 mm)",
        "option_c": "24 inches (600 mm)",
        "option_d": "6 inches (150 mm) with concrete cover",
        "correct_option": "B",
        "explanation": "According to NEC Table 300.5, rigid nonmetallic conduit (like Schedule 40 PVC) must be buried at least 18 inches (450 mm) deep when installed under a residential driveway. This table specifies minimum cover requirements for underground installations. The 18-inch requirement applies to residential driveways for circuits rated 0-600 volts. Under areas subject to vehicular traffic, proper burial depth is critical to prevent damage to the conduit from the weight and pressure of vehicles.",
        "nec_reference": "Table 300.5"
    },
    {
        "question_text": "What is the maximum number of 90-degree bends permitted in a single run of conduit between pull points?",
        "topic": "Raceways and Enclosures",
        "option_a": "2 bends (180 degrees total)",
        "option_b": "3 bends (270 degrees total)",
        "option_c": "4 bends (360 degrees total)",
        "option_d": "6 bends (540 degrees total)",
        "correct_option": "C",
        "explanation": "NEC 358.26 (for EMT), 344.26 (for RMC), and similar sections for other types of conduit all specify that there shall not be more than the equivalent of four quarter bends (360 degrees total) between pull points. This limitation ensures that conductors can be pulled through the conduit without excessive stress or damage. Each 90-degree bend equals one quarter bend, so the maximum is four 90-degree bends or any combination of bends totaling 360 degrees.",
        "nec_reference": "358.26, 344.26"
    },
    {
        "question_text": "What minimum size equipment grounding conductor (EGC) is required for a 200-amp circuit using copper conductors?",
        "topic": "Grounding and Bonding",
        "option_a": "6 AWG copper",
        "option_b": "4 AWG copper",
        "option_c": "3 AWG copper",
        "option_d": "2 AWG copper",
        "correct_option": "B",
        "explanation": "According to NEC Table 250.122, for a 200-amp overcurrent device, the minimum size equipment grounding conductor required is 4 AWG copper. The table correlates overcurrent device ratings with minimum EGC sizes to ensure the grounding conductor can safely carry fault current until the overcurrent device clears the fault. This size ensures adequate fault current capacity and minimizes voltage drop in the ground path during a fault condition.",
        "nec_reference": "Table 250.122"
    },
    {
        "question_text": "GFCI protection is now required for all 15 and 20-amp, 125-volt receptacles in which of these locations?",
        "topic": "Branch Circuits",
        "option_a": "Bedrooms",
        "option_b": "Basements (finished or unfinished)",
        "option_c": "Living rooms",
        "option_d": "Hallways",
        "correct_option": "B",
        "explanation": "NEC 210.8(A)(5) requires GFCI protection for all 15 and 20-amp, 125-volt receptacles in basements, whether finished or unfinished. This requirement is part of the expanded GFCI protection in dwelling units due to the potential for moisture in basement areas. While GFCI protection is required in many locations (kitchens, bathrooms, outdoors, etc.), among the options listed, only basements require GFCI protection for all such receptacles. Bedrooms, living rooms, and hallways generally do not require GFCI protection unless near sinks or water sources.",
        "nec_reference": "210.8(A)(5)"
    },
    {
        "question_text": "According to the NEC, what is the general approach to calculating the minimum number of receptacle outlets required in a dwelling unit room?",
        "topic": "Branch Circuits",
        "option_a": "One receptacle outlet for every 6 feet of wall space",
        "option_b": "One receptacle outlet for every 8 feet of wall space",
        "option_c": "One receptacle outlet for every 10 feet of wall space",
        "option_d": "One receptacle outlet for every 12 feet of wall space",
        "correct_option": "D",
        "explanation": "NEC 210.52(A)(1) specifies that receptacle outlets in habitable rooms of dwelling units must be installed so that no point along the floor line in any wall space is more than 6 feet, measured horizontally, from an outlet. Since receptacles serve the area 6 feet to either side, this effectively means receptacles must be placed at least every 12 feet along walls. The rule ensures that a cord of reasonable length can reach a receptacle from anywhere along a wall without requiring extension cords.",
        "nec_reference": "210.52(A)(1)"
    },
    {
        "question_text": "When installing outlet boxes, what is the maximum setback allowed from the finished surface of a noncombustible wall?",
        "topic": "Boxes and Enclosures",
        "option_a": "1/4 inch",
        "option_b": "1/2 inch",
        "option_c": "1/8 inch",
        "option_d": "3/4 inch",
        "correct_option": "A",
        "explanation": "According to NEC 314.20, outlet boxes in walls or ceilings of noncombustible material shall be installed so that the front edge of the box is not set back more than 1/4 inch from the finished surface.",
        "nec_reference": "314.20"
    },
    {
        "question_text": "What is the maximum number of #14 AWG conductors permitted in a 4x1-1/2 inch octagonal box?",
        "topic": "Boxes and Enclosures",
        "option_a": "6 conductors",
        "option_b": "8 conductors",
        "option_c": "10 conductors",
        "option_d": "12 conductors",
        "correct_option": "B",
        "explanation": "According to NEC Table 314.16(A), a 4x1-1/2 inch octagonal box has a maximum volume of 15.5 cubic inches. Per Table 314.16(B), each #14 AWG conductor counts as 2.0 cubic inches. Therefore, the maximum number is 15.5 ÷ 2.0 = 7.75, which rounds down to 7 conductors. However, if there are internal clamps, one conductor's worth of volume (2.0 cubic inches) must be deducted, leaving room for 6 conductors. If there's also a device yoke, another deduction is required. The correct answer is typically 8 for boxes without internal clamps or other deductions.",
        "nec_reference": "314.16(A), 314.16(B)"
    },
    {
        "question_text": "When a box contains one or more devices (switches, receptacles) mounted on straps or yokes, how many conductor volume allowances must be deducted from the box's total volume?",
        "topic": "Boxes and Enclosures",
        "option_a": "One for each device",
        "option_b": "Two for each device",
        "option_c": "One regardless of the number of devices",
        "option_d": "Two regardless of the number of devices",
        "correct_option": "A",
        "explanation": "According to NEC 314.16(B)(4), for each device (switch or receptacle) mounted on a strap or yoke, a double volume allowance (based on the largest conductor connected to the device) must be deducted from the box's total volume. This means one conductor volume allowance for each device.",
        "nec_reference": "314.16(B)(4)"
    },
    {
        "question_text": "When junction boxes are installed above a suspended ceiling used for environmental air, what material must the boxes be constructed of?",
        "topic": "Boxes and Enclosures",
        "option_a": "Only metal",
        "option_b": "Only nonmetallic",
        "option_c": "Either metal or nonmetallic if listed for the purpose",
        "option_d": "Only metallic if the ceiling is fire-rated",
        "correct_option": "C",
        "explanation": "According to NEC 300.22(C)(3), electrical equipment, including junction boxes, installed in spaces used for environmental air (such as above suspended ceilings used for air handling) can be either metal or nonmetallic as long as they are listed for the application. Both types are acceptable if properly listed.",
        "nec_reference": "300.22(C)(3)"
    },
    {
        "question_text": "What is the minimum depth required for outlet boxes installed in walls or ceilings with combustible surfaces?",
        "topic": "Boxes and Enclosures",
        "option_a": "1/2 inch",
        "option_b": "1/4 inch",
        "option_c": "Flush with the finished surface",
        "option_d": "3/4 inch",
        "correct_option": "C",
        "explanation": "According to NEC 314.20, in walls or ceilings constructed of combustible material, boxes shall be installed so they are flush with the finished surface or project from it. Unlike with noncombustible surfaces (which allow a 1/4 inch setback), boxes in combustible surfaces must be flush or projecting to prevent a fire hazard.",
        "nec_reference": "314.20"
    },
    {
        "question_text": "What is the minimum size of pull or junction boxes required for straight pulls with 3-inch conduits?",
        "topic": "Boxes and Enclosures",
        "option_a": "12 inches",
        "option_b": "8 times the conduit size",
        "option_c": "6 times the conduit size",
        "option_d": "4 times the conduit size",
        "correct_option": "B",
        "explanation": "According to NEC 314.28(A)(1), for straight pulls, the minimum length of the box must be at least 8 times the trade diameter of the largest raceway. For a 3-inch conduit, this would be 8 × 3 = 24 inches.",
        "nec_reference": "314.28(A)(1)"
    },
    {
        "question_text": "Under what condition must outlet and device boxes have a depth of not less than 1-1/2 inches?",
        "topic": "Boxes and Enclosures",
        "option_a": "When installed in concrete",
        "option_b": "When containing devices larger than 30 amperes",
        "option_c": "When containing #6 or larger conductors",
        "option_d": "When installed in fire-rated walls",
        "correct_option": "C",
        "explanation": "According to NEC 314.24(A), outlet and device boxes that contain devices or equipment must have a minimum depth of 1-1/2 inches when the box contains one or more #6 AWG or larger conductors.",
        "nec_reference": "314.24(A)"
    },
    {
        "question_text": "What is the maximum number of conductors entering a conduit body (such as an LB) when the conduit body contains no splices, taps, or devices?",
        "topic": "Boxes and Enclosures",
        "option_a": "No limit as long as the conduit body is marked with its cubic inch capacity",
        "option_b": "Limited by the maximum allowed fill percentage of 40%",
        "option_c": "Limited to the maximum number of conductors permitted in the trade size conduit connected to the conduit body",
        "option_d": "Limited by the box fill calculations in NEC 314.16",
        "correct_option": "C",
        "explanation": "According to NEC 314.16(C)(2), conduit bodies that do not contain splices, taps, or devices are limited to the number of conductors permitted in the trade size conduit connected to the conduit body. This is based on the conduit fill tables in Chapter 9 of the NEC.",
        "nec_reference": "314.16(C)(2)"
    },
    {
        "question_text": "When installing a box that contains different sized conductors, how do you determine the minimum box volume required?",
        "topic": "Boxes and Enclosures",
        "option_a": "Use the largest conductor size for all volume calculations",
        "option_b": "Calculate the volume needed for each conductor size separately and add them together",
        "option_c": "Use the average of all conductor sizes",
        "option_d": "Use the most common conductor size for all conductors",
        "correct_option": "B",
        "explanation": "According to NEC 314.16(B), when determining minimum box volume, each conductor must be counted individually using its respective volume allowance from Table 314.16(B). Different sized conductors require different volume allowances, so each conductor's volume requirement must be calculated separately and then added together.",
        "nec_reference": "314.16(B)"
    },
    {
        "question_text": "According to the NEC, what is the minimum distance a flush-mounted outlet box must be installed from combustible material?",
        "topic": "Boxes and Enclosures",
        "option_a": "1/4 inch",
        "option_b": "1/2 inch",
        "option_c": "1/8 inch",
        "option_d": "No minimum clearance is required",
        "correct_option": "C",
        "explanation": "NEC Section 314.20 requires that metal boxes be installed so that the front edge of the box or associated raised cover is not set back more than 1/8 inch from the finished surface when installed in walls or ceilings of combustible material.",
        "nec_reference": "314.20"
    },
    {
        "question_text": "Which of the following is NOT a requirement for boxes that contain devices or utilization equipment?",
        "topic": "Boxes and Enclosures",
        "option_a": "The box must be securely fastened in place",
        "option_b": "The box must have a depth of at least 1.5 inches",
        "option_c": "The box must be of a type listed for the specific application",
        "option_d": "All non-metallic boxes must have internal cable clamps",
        "correct_option": "D",
        "explanation": "NEC does not require all non-metallic boxes to have internal cable clamps. Section 314.17 covers requirements for cable entry into boxes, but does not universally require internal clamps for non-metallic boxes. The other options are valid requirements found in NEC 314.23 (secure fastening), 314.24 (minimum depths), and 314.27 (boxes for specific applications).",
        "nec_reference": "314.17, 314.23, 314.24, 314.27"
    },
    {
        "question_text": "When determining the volume requirements of an outlet box, how are equipment grounding conductors counted?",
        "topic": "Boxes and Enclosures",
        "option_a": "All equipment grounding conductors together count as one conductor",
        "option_b": "Equipment grounding conductors are not counted in box fill calculations",
        "option_c": "Each equipment grounding conductor counts as a separate conductor",
        "option_d": "Equipment grounding conductors count as one-half of a conductor each",
        "correct_option": "A",
        "explanation": "According to NEC 314.16(B)(5), all equipment grounding conductors in a box are counted together as a single conductor for box fill calculations. The volume allowance is based on the largest equipment grounding conductor in the box.",
        "nec_reference": "314.16(B)(5)"
    },
    {
        "question_text": "What is the minimum required support interval for horizontal runs of EMT conduit 1 inch or less in trade size?",
        "topic": "Boxes and Enclosures",
        "option_a": "8 feet",
        "option_b": "10 feet",
        "option_c": "12 feet",
        "option_d": "6 feet",
        "correct_option": "B",
        "explanation": "According to NEC Section 358.30(A), EMT conduit 1 inch or less in trade size must be supported at intervals not exceeding 10 feet. EMT greater than 1 inch must be supported at intervals not exceeding 10 feet. Per the exception, a straight run of conduit can span a maximum of 3 feet from a box with no support if the conduit is terminated in fittings.",
        "nec_reference": "358.30(A)"
    },
    {
        "question_text": "What is the volume allowance required for each No. 14 AWG conductor in a box according to the NEC?",
        "topic": "Boxes and Enclosures",
        "option_a": "2.0 cubic inches",
        "option_b": "2.25 cubic inches",
        "option_c": "2.5 cubic inches",
        "option_d": "3.0 cubic inches",
        "correct_option": "A",
        "explanation": "According to NEC Table 314.16(B), the volume allowance required for a No. 14 AWG conductor is 2.0 cubic inches. Each conductor that originates outside the box and terminates or is spliced within the box shall be counted once.",
        "nec_reference": "314.16(B)"
    },
    {
        "question_text": "According to the NEC, which of the following is true regarding outlet boxes installed in concrete or masonry walls?",
        "topic": "Boxes and Enclosures",
        "option_a": "Only metal boxes are permitted",
        "option_b": "Boxes must be set back at least 1/4 inch from the finished surface",
        "option_c": "Sectional boxes are prohibited",
        "option_d": "Any box or fitting with a flush-type cover is permitted",
        "correct_option": "D",
        "explanation": "According to NEC Section 314.20, in walls or ceilings constructed of concrete, tile, or other noncombustible material, boxes shall be installed so that the front edge of the box, plaster ring, extension ring, or listed extender will not be set back of the finished surface more than 1/4 in. (6 mm). In walls and ceilings constructed of wood or other combustible material, the front edge of the box, plaster ring, extension ring, or listed extender shall be flush with the finished surface or project therefrom.",
        "nec_reference": "314.20"
    },
    {
        "question_text": "In a 4-inch square junction box with a raised plaster ring, where should the box volume marking be located?",
        "topic": "Boxes and Enclosures",
        "option_a": "On both the box and the plaster ring",
        "option_b": "On the inside or outside of the box, but not on the plaster ring",
        "option_c": "Only on the outside of the box",
        "option_d": "Only on the plaster ring",
        "correct_option": "B",
        "explanation": "According to NEC Section 314.16(A)(1), the box volume must be marked on the inside or outside of the box itself, not on the plaster ring. The plaster ring does not need to be marked with volume information as it is the box that provides the volume for the conductors.",
        "nec_reference": "314.16(A)(1)"
    },
    {
        "question_text": "Which of the following is NOT a requirement for junction boxes containing conductors size 4 AWG or larger?",
        "topic": "Boxes and Enclosures",
        "option_a": "The minimum dimension of the box must be at least 8 times the diameter of the largest raceway",
        "option_b": "The box must have a minimum depth of 6 inches",
        "option_c": "The conductors must enter the box through the wall nearest to the terminal",
        "option_d": "The box must provide adequate space for all conductors installed in the box",
        "correct_option": "B",
        "explanation": "NEC Section 314.28 provides the dimensional requirements for pull and junction boxes, but it does not specify a minimum 6-inch depth. For conductors 4 AWG or larger, the minimum dimension must be at least 6 times (not 8 times) the diameter of the largest raceway. Additionally, when conductors enter the box through the wall opposite to the removable cover, the distance from the wall to the cover shall be at least the distance specified in Section 314.28(A)(2).",
        "nec_reference": "314.28"
    },
    {
        "question_text": "What is the minimum size junction box required for a straight pull of three 1-inch conduits entering on one side and exiting on the opposite side?",
        "topic": "Boxes and Enclosures",
        "option_a": "4 inches by 4 inches by 2 inches",
        "option_b": "6 inches by 6 inches by 4 inches",
        "option_c": "8 inches by 8 inches by 4 inches",
        "option_d": "10 inches by 10 inches by 4 inches",
        "correct_option": "C",
        "explanation": "According to NEC 314.28(A)(1), for straight pulls, the length of the box shall be at least 8 times the trade diameter of the largest raceway. For a 1-inch conduit, the minimum dimension would be 8 × 1 inch = 8 inches. Therefore, an 8-inch by 8-inch by 4-inch junction box would be the minimum size required.",
        "nec_reference": "314.28(A)(1)"
    },
    {
        "question_text": "A junction box contains two 12 AWG hot conductors (feed in and feed out), one 12 AWG switched leg conductor, two 12 AWG neutral conductors spliced together, and one 12 AWG equipment grounding conductor. There is also a single-pole switch (device) mounted in the box. What is the minimum box volume required for this arrangement?",
        "topic": "Boxes and Enclosures",
        "option_a": "18.0 cubic inches",
        "option_b": "20.3 cubic inches",
        "option_c": "22.5 cubic inches",
        "option_d": "16.0 cubic inches",
        "correct_option": "C",
        "explanation": "Box fill is calculated per NEC 314.16(B). For 12 AWG conductors, each conductor contributes 2.25 cubic inches. In this box: 3 insulated #12 conductors (feed in, feed out, switched leg) = 3 × 2.25, plus 2 insulated #12 neutrals spliced = 2 × 2.25, all equipment grounds together count as 1 × 2.25, and the switch device counts as 2 × 2.25 (a double volume allowance for its yoke). That yields 3 + 2 + 1 + 2 = 8 conductor equivalents. 8 × 2.25 = 18.0 cu in required for the conductors. Additionally, the switch on a single yoke with #12 connections adds 4.5 cu in (two #12 volumes). Therefore, the box must be at least 18.0 + 4.5 = 22.5 cu in in size.",
        "nec_reference": "314.16(B)"
    },
    {
        "question_text": "When calculating box fill per the NEC, multiple equipment grounding conductors in the same box are counted as ____?",
        "topic": "Boxes and Enclosures",
        "option_a": "One conductor total (using the volume of the largest grounding conductor)",
        "option_b": "One conductor for each grounding conductor present",
        "option_c": "Two conductors total, if more than one ground is present",
        "option_d": "Equipment grounds are not counted in box fill",
        "correct_option": "A",
        "explanation": "Per NEC 314.16(B)(5) (Grounding Conductor Fill), all equipment grounding conductors in a box together count as only one conductor for volume calculation. You use the volume of the largest grounding conductor present. So, whether the box has one or several grounding wires, they collectively count as one fill unit. This is an important exception: you do not count each ground individually for box fill.",
        "nec_reference": "314.16(B)(5)"
    },
    {
        "question_text": "What is the minimum length of free conductor that must be left protruding from an outlet or junction box for making connections?",
        "topic": "Boxes and Enclosures",
        "option_a": "3 inches",
        "option_b": "6 inches",
        "option_c": "8 inches",
        "option_d": "12 inches",
        "correct_option": "B",
        "explanation": "NEC 300.14 requires at least 6 inches of free conductor length to be left at each outlet, junction, and switch point for splices or the attachment of devices. This is measured from where the conductor emerges from the cable or raceway into the box. Additionally, if the opening of the box is less than 8 inches in any dimension, each conductor must extend at least 3 inches outside the box opening. These rules ensure there is sufficient slack to make secure connections without straining the wires.",
        "nec_reference": "300.14"
    },
    {
        "question_text": "According to the NEC, what is required regarding the accessibility of junction or outlet boxes after installation?",
        "topic": "Boxes and Enclosures",
        "option_a": "Boxes with splices or terminations must be accessible (not permanently covered) after installation",
        "option_b": "Boxes may be concealed behind drywall as long as their location is documented",
        "option_c": "Only switch and receptacle boxes need to remain accessible; straight-through junction boxes can be buried",
        "option_d": "Boxes can be hidden behind walls or ceilings if no more than two splices are inside",
        "correct_option": "A",
        "explanation": "NEC 314.29 states that outlet, pull, and junction boxes must be accessible without removing parts of the building structure. In practice, this means you cannot permanently cover a box with drywall, plaster, or other finish material. Every box containing splices or terminations must have a cover or access panel that can be removed for inspection and maintenance. If a box is hidden behind a surface, it violates the code requirement for accessibility.",
        "nec_reference": "314.29"
    },
    {
        "question_text": "When a ceiling outlet box is used to support a ceiling-suspended paddle fan, what does the NEC require?",
        "topic": "Boxes and Enclosures",
        "option_a": "The outlet box must be listed and marked as suitable for fan support",
        "option_b": "The box must be at least 4 inches square in size",
        "option_c": "The box must be metallic (plastic boxes are not allowed for fans)",
        "option_d": "The box must be supported by a fan brace bar spanning the joists",
        "correct_option": "A",
        "explanation": "Ceiling outlet boxes for fans must be specifically rated for that purpose. NEC 314.27(C) requires that any outlet box used as the sole support of a ceiling-suspended (paddle) fan be listed and clearly marked as suitable for fan support. These fan-rated boxes are designed to support the fan's weight and motion. A standard box not marked for fan support must not be used to hang a fan, as it may not safely carry the load.",
        "nec_reference": "314.27(C)"
    },
    {
        "question_text": "A 4-inch square electrical box that is 1-1/2 inches deep has a listed volume of 21 cubic inches. Assuming no internal clamps or fittings, what is the maximum number of insulated #14 AWG conductors allowed in this box by the NEC?",
        "topic": "Boxes and Enclosures",
        "option_a": "8 conductors",
        "option_b": "9 conductors",
        "option_c": "10 conductors",
        "option_d": "11 conductors",
        "correct_option": "C",
        "explanation": "For box fill, each #14 AWG insulated conductor requires 2.0 cubic inches of box volume. A 21 cu.in. box can accommodate up to 10 such conductors (10 × 2.0 = 20.0 cu.in.) but not 11 (which would require 22.0 cu.in.). NEC Table 314.16(A) confirms that a 4\"×4\"×1.5\" (21 in³) box can hold a maximum of ten #14 conductors under these conditions. If 11 conductors were needed, a larger or deeper box would be required to satisfy the volume requirement.",
        "nec_reference": "314.16(A)"
    },
    {
        "question_text": "Nonmetallic-sheathed (NM) cable must be secured (stapled or otherwise fastened) within how many inches of the cable's entry into an outlet box, and at what intervals along the run?",
        "topic": "Boxes and Enclosures",
        "option_a": "Within 12 inches of the box, and at least every 4.5 feet thereafter",
        "option_b": "Within 6 inches of the box, and at least every 3 feet thereafter",
        "option_c": "Within 8 inches of the box, and at least every 10 feet thereafter",
        "option_d": "NM cable does not require securing near boxes, only protection from abrasion",
        "correct_option": "A",
        "explanation": "NEC 334.30 specifies that Type NM cable must be secured within 12 inches of every outlet, junction, or switch box (measured from where the cable enters the box), and must be supported at intervals not exceeding 4.5 feet along its length. This ensures the cable is properly supported and protected from tension or movement. For boxes with built-in cable clamps, the clamp inside the box can serve as the securing means within 12 inches.",
        "nec_reference": "334.30"
    },
    {
        "question_text": "How should you handle unused openings (knockout holes, conduit openings, etc.) in electrical boxes or enclosures, according to the NEC?",
        "topic": "Boxes and Enclosures",
        "option_a": "Close them off with an approved filler or knockout seal",
        "option_b": "Leave them open for ventilation unless in a wet location",
        "option_c": "Cover them with electrical tape as a temporary fix",
        "option_d": "They only need to be closed if larger than 1 inch in diameter",
        "correct_option": "A",
        "explanation": "Unused openings in boxes, panelboards, or other enclosures must be closed with appropriate closures (filler plates, knockout seals, etc.). NEC 110.12(A) requires that unused openings (other than those intentionally for ventilation) be effectively closed to maintain the enclosure's integrity. Leaving holes open is not permitted, as it could allow debris or fingers to enter and contact live parts, or compromise fire containment.",
        "nec_reference": "110.12(A)"
    },
    {
        "question_text": "In box fill calculations, how is a wiring device (such as a switch or receptacle on a strap) counted?",
        "topic": "Boxes and Enclosures",
        "option_a": "As two conductors (of the largest size connected to it)",
        "option_b": "As one conductor, regardless of device type",
        "option_c": "Devices are not counted in box fill if their leads are already counted",
        "option_d": "It depends on the device rating",
        "correct_option": "A",
        "explanation": "Each yoke or strap that supports a device counts as a double volume allowance in box fill calculations. NEC 314.16(B)(4) requires that one strap = two conductor volumes of the size of the largest conductor attached to it. For example, a receptacle with #12 connections adds 2 × 2.25 cu in = 4.5 cu in to the required box volume. So a single switch or receptacle is counted as two conductors.",
        "nec_reference": "314.16(B)(4)"
    },
    {
        "question_text": "Can conductors be spliced or joined inside a conduit body (for example, an \"LB\" fitting)?",
        "topic": "Boxes and Enclosures",
        "option_a": "Yes, but only if the conduit body is specifically listed with an adequate volume for splices (and is marked with its cubic inch capacity)",
        "option_b": "Yes, any conduit body may contain splices as long as you don't exceed four conductors",
        "option_c": "No - splices in conduit bodies are not permitted under any circumstances",
        "option_d": "Only if the conductors are #10 AWG or smaller",
        "correct_option": "A",
        "explanation": "Splices or terminations are allowed in a conduit body only if it is designed and listed for that purpose. Standard small LBs and conduit bodies are usually not large enough or labeled for splicing. NEC 314.16(C)(2) says that if splices are made, the conduit body must have a volume marked and of sufficient size for the conductors (just like a box). If it's not marked for volume, you cannot use it for splicing – use a proper junction box instead.",
        "nec_reference": "314.16(C)(2)"
    },
    {
        "question_text": "For a straight pull of 4 AWG or larger conductors through a junction box, what minimum distance must be maintained between the entry and opposite side (in line with the pull) according to NEC 314.28?",
        "topic": "Boxes and Enclosures",
        "option_a": "8 times the trade diameter of the largest conduit",
        "option_b": "6 times the trade diameter of the largest conduit",
        "option_c": "24 inches (2 feet)",
        "option_d": "No minimum – just make it as large as practical",
        "correct_option": "A",
        "explanation": "NEC 314.28(A)(1) requires that for straight pulls (no change in direction) of conductors 4 AWG or larger, the length of the box (in line with those conductors) must be at least 8× the trade diameter of the largest conduit entering that wall of the box. For example, if the largest conduit is 2\" (trade size), the box must be at least 16\" long in that direction. This ensures there is enough room for bending and pulling the conductors.",
        "nec_reference": "314.28(A)(1)"
    },
    {
        "question_text": "If an insulated conductor passes unbroken through a box (does not splice or terminate in the box), how is it counted for box fill purposes?",
        "topic": "Boxes and Enclosures",
        "option_a": "It counts as one conductor (of its size)",
        "option_b": "It doesn't count at all since it's unspliced",
        "option_c": "It counts as two conductors (one entering, one leaving)",
        "option_d": "Only pass-through neutrals count, not hots",
        "correct_option": "A",
        "explanation": "NEC 314.16(B)(1) clarifies that each conductor that originates outside and terminates or passes through the box counts as one conductor for box fill. There is no exemption for unbroken (unspliced) conductors – they still occupy space, so a pass-through wire counts the same as a spliced wire. The only things that don't count are the pigtails that originate and terminate within the box.",
        "nec_reference": "314.16(B)(1)"
    },
    {
        "question_text": "When using nonmetallic-sheathed cable (e.g., NM-B Romex), how far must the cable's outer sheath extend into a metal or plastic box?",
        "topic": "Boxes and Enclosures",
        "option_a": "At least 1/4 inch beyond the cable clamp or entry",
        "option_b": "It should be stripped off flush with the box entry",
        "option_c": "There is no requirement for sheath inside the box",
        "option_d": "At least 2 inches inside the box",
        "correct_option": "A",
        "explanation": "NEC 314.17(B) requires that the sheath of NM or UF cable extend not less than 1/4 inch inside the box and beyond any cable clamp. This protects the insulated conductors from abrasion at the entry point. In practice, you slide the cable into the box so that a little bit of jacket is visible inside. Stripping the jacket off flush with the outside of the box is a violation.",
        "nec_reference": "314.17(B)"
    },
    {
        "question_text": "If an electrical box is recessed too far behind the finished wall surface (for instance, 1/2\" behind drywall), what does the NEC require the installer to do?",
        "topic": "Boxes and Enclosures",
        "option_a": "Install a listed box extension (often called a \"mud ring\" or extension collar) to bring the box flush with the surface",
        "option_b": "Pack the gap with non-combustible material",
        "option_c": "Nothing, up to 1/2\" setback is fine",
        "option_d": "Replace the box with a deeper box",
        "correct_option": "A",
        "explanation": "Electrical boxes must be mounted so they are essentially flush with combustible wall surfaces (wood, etc.) and not set back more than 1/4\" in noncombustible surfaces (like drywall). If a box ends up too deep, you must use a box extension to bring it level. NEC 314.20 outlines these requirements. A listed box extension maintains the required enclosure and protects against fire spread through gaps.",
        "nec_reference": "314.20"
    },
    {
        "question_text": "What volume (in cubic inches) is assigned to one 12 AWG conductor when calculating box fill?",
        "topic": "Boxes and Enclosures",
        "option_a": "2.25 cubic inches",
        "option_b": "2.00 cubic inches",
        "option_c": "2.50 cubic inches",
        "option_d": "3.00 cubic inches",
        "correct_option": "A",
        "explanation": "NEC Table 314.16(B) gives the volume allowance per conductor size. For 12 AWG, it's 2.25 cubic inches per conductor. (For comparison, 14 AWG is 2.0 cu in, 10 AWG is 2.5 cu in, etc.) This means each 12 AWG entering a box, or part of a device, counts as 2.25 cubic inches of the box's capacity.",
        "nec_reference": "314.16(B)"
    },
    {
        "question_text": "A luminaire (lighting fixture) weighing 60 lb is to be mounted on an electrical box in a ceiling. What does the NEC require in this case?",
        "topic": "Boxes and Enclosures",
        "option_a": "The fixture must be independently supported (or the outlet box listed for the weight), since standard boxes are only rated up to 50 lb unless marked otherwise",
        "option_b": "Just use extra screws to attach the fixture to the box",
        "option_c": "Support is only needed if the fixture exceeds 100 lb",
        "option_d": "The NEC doesn't specify – follow manufacturer instructions",
        "correct_option": "A",
        "explanation": "NEC 314.27(B) says that outlet boxes used to support luminaires (light fixtures) must be listed for the purpose, and that standard boxes are only good for fixtures up to 50 pounds. If the fixture is heavier than 50 lb, it must be supported independently of the box (unless the box is specifically listed for supporting that greater weight). So a 60 lb chandelier, for example, often requires a special fan/fixture box or support bar rated for that weight.",
        "nec_reference": "314.27(B)"
    },
    {
        "question_text": "Is it permissible to make a splice or connection between conductors without enclosing that splice in a junction box or enclosure?",
        "topic": "Boxes and Enclosures",
        "option_a": "No – all splices must be in an accessible box or enclosure (with a few specific exceptions for specialized splice kits)",
        "option_b": "Yes – you can splice wires mid-run as long as you wrap them well with tape",
        "option_c": "Yes – if the conductors are soldered together and taped",
        "option_d": "Low-voltage splices are exempt from this",
        "correct_option": "A",
        "explanation": "In general, the NEC requires that all splices and terminations be contained in an approved box or conduit body that is accessible (NEC 300.15). You can't have a hidden splice floating in a wall or ceiling. The only exceptions are for certain direct-burial cables with listed underground splice kits, or some types of busway plug-in connections, etc. But for normal building wiring, every splice belongs in a box (or equipment like a luminaire canopy or an outlet device).",
        "nec_reference": "300.15"
    },
    {
        "question_text": "How must junction boxes or outlet boxes be supported?",
        "topic": "Boxes and Enclosures",
        "option_a": "They must be securely fastened to the building structure or otherwise firmly supported (e.g., with brackets or hangers)",
        "option_b": "They can hang unsupported if the conduits hold them in place",
        "option_c": "They should be glued to a nearby surface",
        "option_d": "No support needed for plastic boxes",
        "correct_option": "A",
        "explanation": "NEC 314.23 requires that all boxes be securely supported by the building structure. Wall boxes are typically nailed or screwed to studs, ceiling boxes to joists or support bars. You cannot have a box just hanging on the electrical cables or conduits. Even when using conduit, there are rules if the conduit itself is supporting the box (must be threaded rigid or IMC within a certain length, etc.). Plastic boxes often have nails or clamps for support; they definitely can't just float.",
        "nec_reference": "314.23"
    },
    {
        "question_text": "A multiwire branch circuit (MWBC) shares a neutral between two hot conductors. What does the NEC require for the disconnecting means of those hot legs?",
        "topic": "Branch Circuits",
        "option_a": "They must have a common disconnect or be tied together so they trip simultaneously",
        "option_b": "Each hot may be on a separate breaker with no special provisions",
        "option_c": "The neutral must have its own disconnect independent of the hots",
        "option_d": "Multiwire branch circuits are no longer permitted by the NEC",
        "correct_option": "A",
        "explanation": "For a multiwire branch circuit (two or more ungrounded conductors sharing a neutral), NEC 210.4(B) requires a means to simultaneously disconnect all ungrounded conductors. Typically this means using a 2-pole or 3-pole breaker or handle-tied breakers. This ensures that if one circuit is being serviced and turned off, the other hot that shares the neutral is also off – preventing someone from getting shocked via the neutral.",
        "nec_reference": "210.4(B)"
    },
    {
        "question_text": "How many 20-ampere branch circuits for small-appliance loads are required as a minimum in a residential kitchen/dining area by the NEC?",
        "topic": "Branch Circuits",
        "option_a": "Two",
        "option_b": "One",
        "option_c": "None – 15A circuits are fine",
        "option_d": "Three",
        "correct_option": "A",
        "explanation": "The NEC requires at least two 20-amp small-appliance branch circuits to serve kitchen countertop and dining area receptacles (see NEC 210.11(C)(1) and 210.52(B)). These cannot serve other areas like lights or other rooms – just the kitchen/dining receptacles (including fridge and microwave receptacles typically). The idea is to provide enough circuits for high-use kitchen appliances (toaster, coffee maker, etc.).",
        "nec_reference": "210.11(C)(1)"
    },
    {
        "question_text": "In a dwelling unit, what branch circuit is required to supply laundry receptacle outlets?",
        "topic": "Branch Circuits",
        "option_a": "At least one dedicated 20-amp branch circuit for laundry",
        "option_b": "It can share the kitchen small-appliance circuit",
        "option_c": "A dedicated 15-amp circuit is required for the washer",
        "option_d": "No special circuit; laundry can be on general lighting",
        "correct_option": "A",
        "explanation": "NEC 210.11(C)(2) requires at least one 20-amp branch circuit solely for laundry receptacle(s). This circuit can supply the washer and any other receptacles in the laundry area, but it can't feed lighting or receptacles outside the laundry. The intent is to ensure the washing machine (and gas dryer ignition, etc.) has a solid 20A circuit. You wouldn't put the laundry on, say, a bedroom circuit or the kitchen circuits.",
        "nec_reference": "210.11(C)(2)"
    },
    {
        "question_text": "Which of the following correctly describes the NEC requirement for bathroom branch circuits in a dwelling unit?",
        "topic": "Branch Circuits",
        "option_a": "At least one 20-amp branch circuit must supply bathroom receptacles, and it can have no other outlets outside of bathrooms",
        "option_b": "Bathroom receptacles may be on a general lighting 15-amp circuit",
        "option_c": "The bathroom circuit must also supply the laundry room",
        "option_d": "Bathrooms require two separate 20-amp circuits",
        "correct_option": "A",
        "explanation": "NEC 210.11(C)(3) requires at least one 20-amp branch circuit dedicated to bathroom receptacle outlets. This circuit can supply receptacles in one or more bathrooms, but nothing outside bathrooms. Alternatively, one 20A circuit can serve one single bathroom's receptacles and also its lights/exhaust fan (but that circuit can't leave that bathroom). So answer A is the rule. You can't put bathroom receptacles on a general 15A lighting circuit.",
        "nec_reference": "210.11(C)(3)"
    },
    {
        "question_text": "According to the NEC, what branch circuit provision is required for garages in a dwelling unit?",
        "topic": "Branch Circuits",
        "option_a": "At least one 20-amp circuit dedicated to garage receptacles (with no other outlets)",
        "option_b": "Garage receptacles can share a circuit with outdoor lighting",
        "option_c": "A 15-amp circuit is sufficient for garage receptacles",
        "option_d": "No special circuit is needed for garages",
        "correct_option": "A",
        "explanation": "Since the 2017 NEC, at least one 120-volt, 20-amp branch circuit is required for garage receptacle outlets in dwellings (NEC 210.11(C)(4)). This circuit cannot have other outlets (except you can include readily accessible outdoor receptacles on it). The idea is to provide enough power for garage loads (tools, etc.) separate from other circuits. So yes, a 20A dedicated circuit for garages is needed.",
        "nec_reference": "210.11(C)(4)"
    },
    {
        "question_text": "Which of the following locations in a dwelling does NOT require GFCI protection for a 120-volt, 15 or 20A receptacle outlet under the 2020 NEC?",
        "topic": "Branch Circuits",
        "option_a": "An attic receptacle for a ducted HVAC unit (not easily accessible)",
        "option_b": "A receptacle in a garage",
        "option_c": "A receptacle within 6 feet of a kitchen sink",
        "option_d": "A receptacle in an unfinished basement",
        "correct_option": "A",
        "explanation": "GFCI protection is required by NEC 210.8(A) for receptacles in garages, kitchens (countertops or within 6' of sink), unfinished basements, outdoors, bathrooms, laundry areas, etc. An attic isn't one of the listed locations, unless the receptacle is for servicing HVAC in an unfinished space might not strictly require GFCI by code. Generally, attic receptacles (if not easily accessible) aren't on the list. So choice A is the exception here.",
        "nec_reference": "210.8(A)"
    },
    {
        "question_text": "Arc-Fault Circuit-Interrupter (AFCI) protection is required for many branch circuits in dwelling units. Which of these circuits is NOT required to be AFCI-protected under the 2020 NEC?",
        "topic": "Branch Circuits",
        "option_a": "A 20A circuit supplying only bathroom receptacles",
        "option_b": "A 15A bedroom outlet circuit",
        "option_c": "A 20A kitchen small-appliance circuit",
        "option_d": "A 15A circuit for living room receptacles",
        "correct_option": "A",
        "explanation": "Under NEC 210.12(A), basically all living area 120V circuits need AFCI (bedrooms, living rooms, dens, kitchens, etc.). However, bathrooms are not included in the AFCI requirement (they need GFCI but not AFCI). Same with garages and outdoor circuits – those are exempt from AFCI. So a 20A dedicated bathroom circuit does not need AFCI. Bedrooms, kitchens, and living areas do require it.",
        "nec_reference": "210.12(A)"
    },
    {
        "question_text": "A branch circuit supplies a continuous load of 16 amps (such as track lighting on for 3+ hours). What minimum circuit ampacity and breaker rating does the NEC require for this circuit?",
        "topic": "Branch Circuits",
        "option_a": "20 A circuit (because 16 A continuous × 125% ≈ 20 A)",
        "option_b": "15 A circuit (16 A can run on a 15 A breaker if it's continuous)",
        "option_c": "25 A breaker and wire",
        "option_d": "No special sizing, 16 A on 16 A is fine",
        "correct_option": "A",
        "explanation": "For continuous loads (lasting 3 hours or more), the NEC requires circuits to be sized at 125% of the load (210.19(A) and 210.20(A)). 16 A × 1.25 = 20 A. That means you need a 20A breaker and appropriately sized conductors (12 AWG Cu) at minimum. A 15A breaker is only good for 15A×0.8 = 12A continuous load, so 16A continuous would overload a 15A circuit over time. So you bump to 20A.",
        "nec_reference": "210.19(A), 210.20(A)"
    },
    {
        "question_text": "Is it permissible to install 15-amp rated duplex receptacles on a 20-amp branch circuit?",
        "topic": "Branch Circuits",
        "option_a": "Yes – if the circuit has more than one receptacle, 15A receptacles are allowed on a 20A circuit",
        "option_b": "Yes – but only one 15A receptacle on that circuit",
        "option_c": "No – receptacle rating must match the circuit ampacity",
        "option_d": "No – a 20A circuit requires 20A rated receptacles",
        "correct_option": "A",
        "explanation": "It is permitted to use 15A receptacles on a 20A multi-outlet branch circuit. NEC Table 210.21(B)(3) and 210.24 allow this because a duplex counts as two outlets and the load is expected to be split. If there is only a single receptacle on a 20A circuit (a single-outlet circuit), that receptacle must be 20A rated. But for the usual scenario with multiple receptacles on one circuit, 15A duplexes are fine. This is a common practice in residential wiring.",
        "nec_reference": "210.21(B)(3)"
    },
    {
        "question_text": "In general living areas of a dwelling (living rooms, bedrooms, etc.), the NEC requires receptacle outlets such that no point along the floor line is more than ____ from a receptacle.",
        "topic": "Branch Circuits",
        "option_a": "6 feet",
        "option_b": "8 feet",
        "option_c": "12 feet",
        "option_d": "5 feet",
        "correct_option": "A",
        "explanation": "This refers to the \"6/12 rule\" in NEC 210.52(A). In habitable rooms, receptacles must be placed such that no point along the wall line is more than 6 feet from an outlet. This means you need one within 6 feet of a door or break, and then at least every 12 feet along the wall. The idea is that a 6-foot cord can reach any point on the wall from an outlet without using an extension cord. So answer A is right.",
        "nec_reference": "210.52(A)"
    },
    {
        "question_text": "On kitchen countertops in dwelling units, receptacle outlets must be placed such that no point along the countertop is more than ___ from a receptacle (to avoid overly long appliance cords).",
        "topic": "Branch Circuits",
        "option_a": "24 inches",
        "option_b": "12 inches",
        "option_c": "36 inches",
        "option_d": "48 inches",
        "correct_option": "A",
        "explanation": "NEC 210.52(C) requires countertop receptacles such that no point along the counter wall line is more than 24\" from a receptacle. This effectively means receptacles at least every 4 feet. Additionally, any counter segment 12\" or wider requires a receptacle. So 24\" (2 feet) is the maximum spacing from any point on the counter to an outlet.",
        "nec_reference": "210.52(C)"
    },
    {
        "question_text": "When using a multiwire branch circuit (two hot legs sharing one neutral) on a single-phase 120/240V system, what must be true to avoid overloading the neutral?",
        "topic": "Branch Circuits",
        "option_a": "The two hot conductors must be on opposite phases (legs) so their neutral currents cancel out rather than add up",
        "option_b": "The two hot conductors must be on the same phase",
        "option_c": "The neutral must be one size larger",
        "option_d": "Nothing – the neutral is not at risk of overload in any case",
        "correct_option": "A",
        "explanation": "In a single-phase 3-wire MWBC, the neutral carries only the imbalance between the two hot conductors if those hots are on opposite legs of the 240V system (180° out of phase). That is the correct way to do it. If by mistake both hots were on the same leg (i.e., both from phase A), then the neutral would carry the sum of the two currents, which could overload it. The code ensures this by requiring a 2-pole breaker for MWBC, thereby automatically putting them on different phases in a panel.",
        "nec_reference": "210.4"
    },
    {
        "question_text": "Which of the following is NOT allowed on the required 20-amp small-appliance branch circuits in a dwelling kitchen?",
        "topic": "Branch Circuits",
        "option_a": "Lighting or fixed appliances in other rooms",
        "option_b": "Refrigerator receptacle in the kitchen",
        "option_c": "Kitchen countertop receptacles",
        "option_d": "A receptacle in the dining area",
        "correct_option": "A",
        "explanation": "The two (or more) required 20A small appliance circuits in a kitchen/dining area are dedicated to serving receptacles in those areas (210.52(B)). You cannot put non-kitchen loads on them. That means no lighting, no bathroom or garage or other rooms on those circuits. Refrigerators and dining room receptacles are allowed to be on them (they are part of kitchen/dining areas). But you definitely cannot have, say, a kitchen SA circuit also feed a living room or the pantry light, etc.",
        "nec_reference": "210.52(B)"
    },
    {
        "question_text": "Which of the following is an acceptable way to supply bathroom circuits in a dwelling, according to the NEC?",
        "topic": "Branch Circuits",
        "option_a": "One 20A circuit can supply one bathroom's receptacles and lights (nothing outside that bathroom)",
        "option_b": "Bathroom receptacles can be on the same 20A circuit as bedroom receptacles",
        "option_c": "All bathrooms in a house must share one 20A circuit for receptacles and lights",
        "option_d": "A 15A circuit may supply a bathroom exhaust fan and receptacle",
        "correct_option": "A",
        "explanation": "The NEC gives two options for bathroom circuits: Option 1 – a single 20A circuit dedicated to receptacles in all bathrooms (no lights on that circuit). Option 2 – one 20A circuit per bathroom that can feed that bathroom's receptacles and other equipment (lights/fan) within the same bathroom. So answer A describes option 2 and is acceptable. Bathroom receptacles cannot be on bedroom circuits. If multiple bathrooms share a circuit, only receptacles on that circuit, no lights. And bathroom receptacles must be 20A circuits, not 15A.",
        "nec_reference": "210.11(C)(3)"
    },
    {
        "question_text": "When a multiwire branch circuit feeds two receptacles in the same box (sharing a neutral), how should the neutral connections be made to ensure safety if one device is removed?",
        "topic": "Branch Circuits",
        "option_a": "The neutral should be spliced with a pigtail to each device so removing one receptacle doesn't interrupt the neutral for the other circuit",
        "option_b": "The neutral can be connected to one receptacle and jump to the other; device screws are sufficient",
        "option_c": "Each circuit needs its own neutral (no sharing)",
        "option_d": "It is not allowed to have a multiwire circuit feed two devices in one box",
        "correct_option": "A",
        "explanation": "NEC 300.13(B) requires that the continuity of a neutral in a multiwire circuit not depend on device connections. Practically, this means you tie the neutral wires together with a wire connector and add a pigtail from that splice to each receptacle. That way, if one receptacle is removed or goes bad, the neutral for the other circuit remains intact through the splice. If you simply daisy-chain the neutral through device screws, removing one device could open the neutral to the other circuit – a dangerous condition.",
        "nec_reference": "300.13(B)"
    },
    {
        "question_text": "Can lighting outlets and receptacle outlets be on the same branch circuit in a residence (assuming none are in areas requiring dedicated circuits)?",
        "topic": "Branch Circuits",
        "option_a": "Yes – general-purpose circuits can supply a mix of lighting and receptacles in dwelling areas",
        "option_b": "No – lights must always be separate from receptacles",
        "option_c": "Yes – but only if it is a 15A circuit, not 20A",
        "option_d": "No – each room must have dedicated circuits for lights and receptacles",
        "correct_option": "A",
        "explanation": "There is no NEC rule that forbids mixing lighting and receptacles on the same branch circuit in normal dwelling areas. For example, a 15A circuit could feed both the lights and outlets in a bedroom. Many electricians do use separate circuits for lights for convenience, but it's not a code requirement. The only exceptions are where code requires dedicated circuits (kitchen small appliance circuits can't feed lights, bathroom receptacle circuit can't feed lights in other rooms unless it's dedicated to one bathroom, etc.). But generally, in living rooms, bedrooms, etc., you can mix them.",
        "nec_reference": "210"
    },
    {
        "question_text": "A branch circuit that supplies only one utilization equipment (like one appliance) is called a(n) ____ branch circuit.",
        "topic": "Branch Circuits",
        "option_a": "Individual",
        "option_b": "Multiwire",
        "option_c": "Feeder",
        "option_d": "General-purpose",
        "correct_option": "A",
        "explanation": "An individual branch circuit supplies a single piece of utilization equipment (NEC Article 100 Definition). For example, a dedicated 20A circuit just for the microwave, or a 30A circuit just for the water heater. This is in contrast to a general-purpose branch circuit, which supplies multiple outlets (like receptacles and lights in a bedroom). A feeder is something else entirely (feeding a panel). Multiwire is a type of branch circuit with shared neutral.",
        "nec_reference": "Article 100"
    },
    {
        "question_text": "What best describes a multiwire branch circuit (MWBC)?",
        "topic": "Branch Circuits",
        "option_a": "A branch circuit with two or more hot (ungrounded) conductors sharing a common neutral",
        "option_b": "A branch circuit that feeds multiple rooms",
        "option_c": "A three-phase branch circuit",
        "option_d": "An individual circuit for a multi-function appliance",
        "correct_option": "A",
        "explanation": "A multiwire branch circuit has two or more ungrounded conductors that share one grounded conductor (neutral). Typically this is a 120/240V circuit with two hots and a neutral in one cable. The hots must be on different phases (or legs of a single phase system) so that the neutral carries only the imbalance. For example, a 3-wire kitchen countertop circuit feeding two different 20A circuits with one neutral is an MWBC. It's not just any circuit feeding multiple rooms – it specifically refers to shared neutral configuration.",
        "nec_reference": "Article 100"
    },
    {
        "question_text": "Which of these appliances would typically require its own dedicated branch circuit due to its load?",
        "topic": "Branch Circuits",
        "option_a": "A central electric water heater (4500 W, 240V)",
        "option_b": "A table lamp",
        "option_c": "A phone charger",
        "option_d": "A ceiling light fixture",
        "correct_option": "A",
        "explanation": "Large appliances or loads usually need dedicated circuits. An electric water heater at 4500 W draws about 18.75 A at 240V, which would be on a 25 or 30A circuit all by itself. Table lamps, chargers, and small lights are fractional loads that go on general circuits. Other examples of things that require a dedicated circuit: electric ranges, electric dryers, microwaves (depending on size), dishwasher+disposal often have their own circuits, HVAC units, etc.",
        "nec_reference": "220.14"
    },
    {
        "question_text": "For calculating branch circuit loads in an office building, the NEC suggests using 180 VA per receptacle outlet. Approximately how many general-purpose receptacles can be served by a 20A, 120V circuit based on that guideline?",
        "topic": "Branch Circuits",
        "option_a": "13 receptacles",
        "option_b": "8 receptacles",
        "option_c": "15 receptacles",
        "option_d": "20 receptacles",
        "correct_option": "A",
        "explanation": "By code, 180 VA is the unit load per strap (outlet) for general receptacles in commercial calculations (NEC 220.14(I)). A 20A 120V circuit is 2400 VA. 2400 / 180 = 13.3, so you'd design for 13 receptacles max on that circuit (for load calc purposes). The code doesn't limit the number of receptacles physically, but this is the basis for design. So the answer is ~13. (Some might round down to 13 exactly to be safe.)",
        "nec_reference": "220.14(I)"
    },
    {
        "question_text": "NEC 240.4(D) sets the general maximum overcurrent protection for small conductors. What are the usual limits for #14 AWG, #12 AWG, and #10 AWG copper conductors, respectively?",
        "topic": "Conductors and Ampacity",
        "option_a": "15 A, 20 A, 30 A",
        "option_b": "20 A, 25 A, 35 A",
        "option_c": "15 A, 15 A, 20 A",
        "option_d": "There are no fixed limits; use ampacity tables solely",
        "correct_option": "A",
        "explanation": "For most circuits, #14 copper is limited to 15A, #12 to 20A, #10 to 30A per NEC 240.4(D). These are often called the small conductor rules. They are essentially absolute unless an exception in 240.4(E) or (G) applies (like certain motor, HVAC, or welding circuits allow different sizing). But generally, you can't put a 40A breaker on #10, even if the insulation rating is high enough theoretically. So 15, 20, 30 is correct.",
        "nec_reference": "240.4(D)"
    },
    {
        "question_text": "#10 AWG copper THHN is rated 40A at 90°C per NEC ampacity tables. But on a typical branch circuit, what is the maximum breaker you would normally use with #10 AWG THHN, and why?",
        "topic": "Conductors and Ampacity",
        "option_a": "30 A, because #10 AWG is limited to 30 A by 240.4(D) for general use circuits",
        "option_b": "40 A, because the THHN insulation allows it",
        "option_c": "50 A, if terminations are 90°C rated",
        "option_d": "20 A, if it's a mixed lighting circuit",
        "correct_option": "A",
        "explanation": "Even though #10 THHN has a 90°C column ampacity of 40A, general rules limit it to 30A protection (240.4(D)). Terminals are typically 60°C or 75°C anyway, which would bring it down to 30A or 35A. Unless it's a special situation like a feeder tap or motor circuit where separate rules allow it, #10 = 30A breaker is the rule of thumb. So, in normal branch circuits, you put #10 on a 30A breaker.",
        "nec_reference": "240.4(D)"
    },
    {
        "question_text": "If you have eight current-carrying conductors in the same raceway or cable, what adjustment factor must be applied to their ampacity according to NEC 310.15(C)(1)?",
        "topic": "Conductors and Ampacity",
        "option_a": "70% of their normal ampacity (because 7–9 conductors = 0.70 adjustment)",
        "option_b": "80% of ampacity",
        "option_c": "50% of ampacity",
        "option_d": "No derating until more than 9 conductors",
        "correct_option": "A",
        "explanation": "For more than 3 current-carrying conductors together, NEC Table 310.15(C)(1) (2020 NEC) or 310.15(B)(3)(a) (older) gives adjustment factors. 4-6 conductors: 80%. 7-9 conductors: 70%. Over 9: 50%. So eight conductors -> 70% of normal ampacity. Therefore, we multiply the base ampacity by 0.7. That's the answer.",
        "nec_reference": "310.15(C)(1)"
    },
    {
        "question_text": "The NEC ampacity tables (e.g., Table 310.16) assume an ambient temperature of 30°C (86°F). What must be done if conductors are installed in an area where the ambient temperature is significantly higher (say 40°C)?",
        "topic": "Conductors and Ampacity",
        "option_a": "Apply a temperature correction factor to reduce the conductor's allowable ampacity",
        "option_b": "Nothing – the table already accounts for typical variations",
        "option_c": "Use a larger size breaker to compensate",
        "option_d": "Only worry if above 60°C ambient",
        "correct_option": "A",
        "explanation": "If the ambient is above 30°C, the NEC requires applying the correction factors found in Table 310.15(B)(2)(a) (2017) or similar in newer code. For 40°C, for instance, a 90°C insulated conductor has an adjustment factor around 0.91. So you would multiply the base ampacity by that factor. In short: hotter environment = conductor can carry less current safely, so you correct (derate) its ampacity. Conversely, in a cooler environment, you could allow slightly more (though NEC doesn't often require upsizing for cold).",
        "nec_reference": "310.15(B)(2)(a)"
    },
    {
        "question_text": "Even if a wire has 90°C-rated insulation (THHN, etc.), why can't we always use the 90°C ampacity from the tables for circuit design?",
        "topic": "Conductors and Ampacity",
        "option_a": "Because equipment terminations are often rated 60°C or 75°C, which limits the usable ampacity of the conductor to those columns",
        "option_b": "Because the 90°C rating is only for fire conditions, not normal use",
        "option_c": "We actually can always use the 90°C rating if the wire is marked",
        "option_d": "You can, as long as the breaker is also 90°C",
        "correct_option": "A",
        "explanation": "NEC 110.14(C) basically says you have to size conductors based on the lowest temperature rating of any connected termination or device. For circuits ≤100A or wires ≤1 AWG, typically devices are 60°C rated (older rule), though many are 75°C now. For larger, often 75°C. Unless all terminations are 90°C (rare), you can't just use the 90°C column; you use 90° only as a starting point for derating adjustments, but final ampacity is limited to the 75° or 60° rating. So the insulation's 90°C property lets it handle more in certain conditions, but you still usually size to 75°C or 60°C values.",
        "nec_reference": "110.14(C)"
    },
    {
        "question_text": "NEC ampacity tables assume 30°C ambient. If conductors are in a location cooler than 30°C, what happens to their ampacity, and if in a hotter location, what happens?",
        "topic": "Conductors and Ampacity",
        "option_a": "Cooler ambient → ampacity increases; Hotter ambient → ampacity decreases (use NEC correction factors)",
        "option_b": "Cooler ambient → no change; Hotter ambient → no change",
        "option_c": "Cooler ambient → ampacity decreases; Hotter ambient → ampacity increases",
        "option_d": "Ambient temperature doesn't affect ampacity",
        "correct_option": "A",
        "explanation": "Ampacity is affected by ambient temperature. Wires run cooler can carry a bit more current (though code doesn't provide a table to increase, the physics is there), whereas in hotter surroundings they carry less. The NEC provides factors for higher ambient to derate the cable. For example, at 40°C, a 90°C wire is derated to 0.91 of table value; at 50°C, to 0.82, etc. The code doesn't explicitly let you increase capacity for colder, but in general cooler = better. So in summary: cold = can handle more (no code credit though), heat = must derate.",
        "nec_reference": "310.15(B)(2)(a)"
    },
    {
        "question_text": "What is the minimum conductor size generally allowed if you want to run conductors in parallel (to share current) per the NEC?",
        "topic": "Conductors and Ampacity",
        "option_a": "1/0 AWG",
        "option_b": "#1 AWG",
        "option_c": "#2 AWG",
        "option_d": "4/0 AWG",
        "correct_option": "A",
        "explanation": "Typically, the NEC requires conductors to be 1/0 AWG or larger to be run in parallel (see NEC 310.10(H)). That means each parallel leg must be at least 1/0. There are some exceptions (e.g., parallel 1 AWG for control power in some industrial equipment, or special cables like MC that are listed to have parallel smaller conductors), but by and large, 1/0 is the rule for power distribution in parallel. So answer is 1/0.",
        "nec_reference": "310.10(H)"
    },
    {
        "question_text": "THHN is a common conductor insulation type. If THHN wire is run in an outdoor conduit (a wet location), what ampacity rating should be used?",
        "topic": "Conductors and Ampacity",
        "option_a": "The 75°C wet-location rating (THHN is dual-rated THWN at 75°C in wet conditions)",
        "option_b": "The 90°C dry rating still applies in wet locations",
        "option_c": "It cannot be used in wet locations at all",
        "option_d": "Cut the ampacity in half for wet location",
        "correct_option": "A",
        "explanation": "Most THHN building wire is dual-rated THHN/THWN (or THWN-2). THHN by itself is only dry locations (90°C dry). THWN (Thermoplastic Heat and Water-resistant, Nylon-jacket) is typically 75°C in wet. THWN-2 is 90°C wet. If the wire jacket doesn't have a '-2', we assume 75°C in wet conditions. So effectively, when running THHN in a wet location, you use the 75°C column for ampacity (unless marked THWN-2, then you can use 90°C column for adjustment but still limited by 75°C terminations). So answer A.",
        "nec_reference": "310.15"
    },
    {
        "question_text": "When applying ampacity adjustment for more than 3 conductors in a raceway, does the neutral count as a current-carrying conductor?",
        "topic": "Conductors and Ampacity",
        "option_a": "It depends – in a 3-wire 120/240V circuit, the neutral doesn't count (only carries imbalance); in a 4-wire 3Ø wye, the neutral does count (especially if harmonic currents are present)",
        "option_b": "No, neutrals are never counted for derating purposes",
        "option_c": "Yes, neutrals always count as current-carrying",
        "option_d": "Only if neutral carries more than 50% of current continuously",
        "correct_option": "A",
        "explanation": "The NEC specifies that a neutral conductor that carries only the unbalanced current of a multiwire circuit (like the neutral of a 120/240V split-phase) is not counted as current-carrying for derating. But a neutral in a 3-phase 4-wire wye system (serving as a return for more than one phase) is counted as current-carrying (and if significant triplen harmonics are present, it definitely counts since it may carry full current). So answer A covers the distinction correctly.",
        "nec_reference": "310.15(E)"
    },
    {
        "question_text": "How are 90°C-rated conductors like THHN typically used when applying ampacity adjustment factors for temperature or bundling?",
        "topic": "Conductors and Ampacity",
        "option_a": "Use the 90°C ampacity for initial calculation and derating, but do not exceed the 75°C (or 60°C) ampacity after all factors, due to terminal limitations",
        "option_b": "You can always use the 90°C value as the allowable ampacity if the insulation is 90°C",
        "option_c": "Treat them as 60°C conductors if derating is needed",
        "option_d": "90°C conductors cannot be derated",
        "correct_option": "A",
        "explanation": "The NEC practice: if you have a 90°C insulated wire, you start with the 90°C ampacity from the tables, apply any ambient or bundling adjustment factors to that value, but then the resulting ampacity cannot exceed what that wire is allowed at the termination rating (often 75°C for breakers/lugs). This way you get maximum benefit of the higher temp insulation for derating, while still protecting terminations. So yes, you use 90° as baseline for derating, but final must be ≤75° column value typically. This is spelled out in NEC 110.14(C).",
        "nec_reference": "110.14(C)"
    },
    {
        "question_text": "Which of the following wire insulation colors is reserved by the NEC for the grounded (neutral) conductor and NOT permitted for use as an ungrounded hot conductor in a cable?",
        "topic": "Conductors and Ampacity",
        "option_a": "White or gray",
        "option_b": "Red",
        "option_c": "Black",
        "option_d": "Blue",
        "correct_option": "A",
        "explanation": "NEC 200.6 requires neutrals to be identified by white or gray (or three white stripes on another color). These colors cannot be used for ungrounded conductors (hots) unless re-identified to a different color at terminations (and re-identification of white is only allowed in cables for certain cases like switch loops, and if #4 or larger, etc.). Green (and green/yellow) is reserved for grounding conductors. Red, black, blue, etc. are typically hot colors. So white/gray are neutral colors.",
        "nec_reference": "200.6"
    },
    {
        "question_text": "What is the smallest size copper conductor the NEC generally permits for a 15-amp branch circuit for lighting or receptacles?",
        "topic": "Conductors and Ampacity",
        "option_a": "14 AWG copper",
        "option_b": "16 AWG copper",
        "option_c": "12 AWG copper",
        "option_d": "Any size, as long as the breaker is 15A",
        "correct_option": "A",
        "explanation": "14 AWG copper is the minimum for a 15A branch circuit. The NEC doesn't allow general power or lighting wiring smaller than 14 AWG (except for some specific things like fixture wires in luminaires or control circuits, which have their own rules). So in typical branch circuits, #14 Cu on 15A, #12 on 20A, etc. 16 AWG is not used for building wiring (except maybe in listed extension cords or fixture whip assemblies, but not in general installation wiring).",
        "nec_reference": "240.4(D)"
    }
]

def populate_questions():
    # No need to create app or assign it since we imported it
    with app.app_context():
        print("Populating database with sample quiz questions...")
        
        questions_added = 0
        for q_data in sample_questions:
            question = PracticeQuestion(
                question_text=q_data['question_text'],
                topic=q_data['topic'],
                difficulty='medium', # Default difficulty
                option_a=q_data['option_a'],
                option_b=q_data['option_b'],
                option_c=q_data['option_c'],
                option_d=q_data['option_d'],
                correct_option=q_data['correct_option'],
                explanation=q_data.get('explanation'), # Use .get for optional fields
                nec_reference=q_data.get('nec_reference'),
                date_created=datetime.utcnow()
            )
            db.session.add(question)
            questions_added += 1
        
        try:
            db.session.commit()
            print(f"Successfully added {questions_added} questions to the database.")
        except Exception as e:
            db.session.rollback()
            print(f"Error populating database: {e}")

if __name__ == '__main__':
    populate_questions() 
import sys
import os
from app import create_app
from models import db, StateInfo

def populate_last_states():
    # Data for the final 12 states
    last_states = [
        {
            "state_name": "Rhode Island",
            "license_types": "Master Electrician, Journeyperson Electrician, Limited Premises Electrician",
            "experience_reqs": "Journeyperson: 4 years (8,000 hours) as registered apprentice. Master: 2 years as journeyperson.",
            "application_info_link": "https://dbr.ri.gov/divisions/occupationalandprofessionallicensing/electricians",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Open-book exam on NEC and Rhode Island electrical code",
            "official_board_link": "https://dbr.ri.gov/divisions/occupationalandprofessionallicensing/electricians"
        },
        {
            "state_name": "South Carolina",
            "license_types": "Master Electrician, Journeyman Electrician, Residential Electrician",
            "experience_reqs": "Journeyman: 4 years experience. Master: 2 years as journeyman.",
            "application_info_link": "https://llr.sc.gov/res/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and South Carolina electrical regulations",
            "official_board_link": "https://llr.sc.gov/res/"
        },
        {
            "state_name": "South Dakota",
            "license_types": "Electrical Contractor, Class B Electrical Contractor, Journeyman Electrician, Class B Journeyman Electrician",
            "experience_reqs": "Journeyman: 4 years of qualified experience. Contractor: 1 year as journeyman.",
            "application_info_link": "https://dlr.sd.gov/electrical/default.aspx",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Open-book exam on NEC and South Dakota electrical code",
            "official_board_link": "https://dlr.sd.gov/electrical/default.aspx"
        },
        {
            "state_name": "Tennessee",
            "license_types": "Limited Licensed Electrician (LLE), Electrical Contractor",
            "experience_reqs": "LLE: 2 years experience. Contractor: 5 years experience.",
            "application_info_link": "https://www.tn.gov/commerce/regboards/contractors/licensee-applicant-resources/license-requirements.html",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Business and law exam, trade exam",
            "official_board_link": "https://www.tn.gov/commerce/regboards/contractors.html"
        },
        {
            "state_name": "Texas",
            "license_types": "Master Electrician, Journeyman Electrician, Residential Wireman, Electrical Apprentice, Electrical Contractor",
            "experience_reqs": "Journeyman: 8,000 hours experience. Master: 2 years as journeyman.",
            "application_info_link": "https://www.tdlr.texas.gov/electricians/elec.htm",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Open-book exam on NEC and Texas electrical statutes",
            "official_board_link": "https://www.tdlr.texas.gov/electricians/elec.htm"
        },
        {
            "state_name": "Utah",
            "license_types": "Master Electrician, Residential Master Electrician, Journeyman Electrician, Residential Journeyman Electrician",
            "experience_reqs": "Journeyman: 4 years (8,000 hours) as apprentice. Master: 2 years as journeyman.",
            "application_info_link": "https://dopl.utah.gov/elec/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Utah construction trades licensing act",
            "official_board_link": "https://dopl.utah.gov/elec/"
        },
        {
            "state_name": "Vermont",
            "license_types": "Master Electrician, Journeyman Electrician, Type-S Limited Specialty",
            "experience_reqs": "Journeyman: 4 years (8,000 hours) experience. Master: 2 years (4,000 hours) as journeyman.",
            "application_info_link": "https://sos.vermont.gov/electricians/",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Open-book exam on NEC and Vermont electrical safety rules",
            "official_board_link": "https://sos.vermont.gov/electricians/"
        },
        {
            "state_name": "Virginia",
            "license_types": "Master Electrician, Journeyman Electrician, Electrical Contractor (Class A, B, or C)",
            "experience_reqs": "Journeyman: 4 years experience. Master: 1 year as journeyman.",
            "application_info_link": "https://www.dpor.virginia.gov/boards/tradesmen",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Virginia electrical code",
            "official_board_link": "https://www.dpor.virginia.gov/boards/tradesmen"
        },
        {
            "state_name": "Washington",
            "license_types": "Master Electrician, Journeyman Electrician, Specialty Electrician, Electrical Contractor",
            "experience_reqs": "Journeyman: 8,000 hours experience. Master: 4 years as journeyman.",
            "application_info_link": "https://lni.wa.gov/licensing-permits/electrical/electrical-licensing-exams-education/electrician",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Open-book exam on NEC and Washington electrical laws",
            "official_board_link": "https://lni.wa.gov/licensing-permits/electrical/"
        },
        {
            "state_name": "West Virginia",
            "license_types": "Master Electrician, Journeyman Electrician, Apprentice Electrician",
            "experience_reqs": "Journeyman: 8,000 hours experience (4 years). Master: 2 years as journeyman.",
            "application_info_link": "https://firemarshal.wv.gov/divisions/fireservices/electricians/Pages/default.aspx",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and West Virginia electrical code",
            "official_board_link": "https://firemarshal.wv.gov/divisions/fireservices/electricians/Pages/default.aspx"
        },
        {
            "state_name": "Wisconsin",
            "license_types": "Master Electrician, Journeyman Electrician, Residential Master Electrician, Residential Journeyman Electrician, Industrial Journeyman Electrician",
            "experience_reqs": "Journeyman: 8,000 hours experience. Master: 1 year as journeyman.",
            "application_info_link": "https://dsps.wi.gov/Pages/Professions/ElectricalContractor/Default.aspx",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Wisconsin electrical code",
            "official_board_link": "https://dsps.wi.gov/Pages/Professions/ElectricalContractor/Default.aspx"
        },
        {
            "state_name": "Wyoming",
            "license_types": "Master Electrician, Journeyman Electrician, Low Voltage Technician, Apprentice Electrician",
            "experience_reqs": "Journeyman: 4 years (8,000 hours) experience. Master: 2 years as journeyman.",
            "application_info_link": "https://electrical.wyo.gov/",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Open-book exam on NEC and Wyoming electrical laws",
            "official_board_link": "https://electrical.wyo.gov/"
        }
    ]

    added_count = 0
    skipped_count = 0

    for state_data in last_states:
        # Check if state already exists
        existing_state = StateInfo.query.filter_by(state_name=state_data["state_name"]).first()
        
        if existing_state:
            print(f"State {state_data['state_name']} already exists. Skipping...")
            skipped_count += 1
        else:
            # Create new state
            new_state = StateInfo(
                state_name=state_data["state_name"],
                license_types=state_data["license_types"],
                experience_reqs=state_data["experience_reqs"],
                application_info_link=state_data["application_info_link"],
                tested_nec_version=state_data["tested_nec_version"],
                exam_details=state_data["exam_details"],
                official_board_link=state_data["official_board_link"]
            )
            
            db.session.add(new_state)
            print(f"Added state: {state_data['state_name']}")
            added_count += 1
    
    # Commit all changes
    db.session.commit()
    print(f"Completed. Added {added_count} states, skipped {skipped_count} states.")

def main():
    app = create_app()
    with app.app_context():
        try:
            populate_last_states()
        except Exception as e:
            print(f"Error populating states: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main() 
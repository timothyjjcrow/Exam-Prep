import sys
import os
from app import create_app
from models import db, StateInfo

def populate_final_states():
    # Data for remaining states
    final_states = [
        {
            "state_name": "Mississippi",
            "license_types": "Master Electrician, Journeyman Electrician, Residential Electrician",
            "experience_reqs": "Journeyman: 4 years experience. Master: 5 years experience with 2 as journeyman.",
            "application_info_link": "https://www.msboc.us/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Mississippi regulations",
            "official_board_link": "https://www.msboc.us/"
        },
        {
            "state_name": "Missouri",
            "license_types": "No statewide licensing. Local municipalities regulate licenses.",
            "experience_reqs": "Varies by municipality",
            "application_info_link": "N/A - check with local jurisdictions",
            "tested_nec_version": "Varies by municipality, usually 2017 or 2020 NEC",
            "exam_details": "Varies by municipality",
            "official_board_link": "N/A - check with local jurisdictions"
        },
        {
            "state_name": "Montana",
            "license_types": "Master Electrician, Journeyman Electrician, Residential Electrician",
            "experience_reqs": "Journeyman: 8,000 hours as apprentice. Master: 4 years as journeyman.",
            "application_info_link": "https://boards.bsd.dli.mt.gov/electricians/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Montana electrical code",
            "official_board_link": "https://boards.bsd.dli.mt.gov/electricians/"
        },
        {
            "state_name": "Nebraska",
            "license_types": "Electrical Contractor, Master Electrician, Journeyman Electrician",
            "experience_reqs": "Journeyman: 4 years of experience. Master: 1 year as journeyman.",
            "application_info_link": "https://electrical.nebraska.gov/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Nebraska electrical regulations",
            "official_board_link": "https://electrical.nebraska.gov/"
        },
        {
            "state_name": "Nevada",
            "license_types": "Master Electrician, Journeyman Electrician, Residential Electrician, Photovoltaic Installer",
            "experience_reqs": "Journeyman: 4 years experience. Master: 1 year as journeyman.",
            "application_info_link": "https://www.nvcontractorsboard.com/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Nevada regulations",
            "official_board_link": "https://www.nvcontractorsboard.com/"
        },
        {
            "state_name": "New Hampshire",
            "license_types": "Master Electrician, Journeyman Electrician",
            "experience_reqs": "Journeyman: 8,000 hours as apprentice. Master: 2,000 hours as journeyman.",
            "application_info_link": "https://www.oplc.nh.gov/electricians/",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Open-book exam on NEC and New Hampshire electrical code",
            "official_board_link": "https://www.oplc.nh.gov/electricians/"
        },
        {
            "state_name": "New Jersey",
            "license_types": "Electrical Contractor, Master Electrician",
            "experience_reqs": "Electrical Contractor: 5 years experience",
            "application_info_link": "https://www.njconsumeraffairs.gov/elec/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Business and law exam, electrical exam",
            "official_board_link": "https://www.njconsumeraffairs.gov/elec/"
        },
        {
            "state_name": "New Mexico",
            "license_types": "Electrical Contractor (EE-98), Journeyman Electrician (EE-98J), Residential Electrician",
            "experience_reqs": "Journeyman: 4 years experience. Contractor: 2 years as journeyman.",
            "application_info_link": "https://www.psiexams.com/nmcid",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and New Mexico electrical code",
            "official_board_link": "https://www.rld.nm.gov/construction-industries/electrical-bureau/"
        },
        {
            "state_name": "New York",
            "license_types": "No statewide licensing. Local municipalities regulate licenses.",
            "experience_reqs": "Varies by municipality",
            "application_info_link": "N/A - check with local jurisdictions",
            "tested_nec_version": "Varies by municipality, usually 2017 or 2020 NEC",
            "exam_details": "Varies by municipality",
            "official_board_link": "N/A - check with local jurisdictions"
        },
        {
            "state_name": "North Carolina",
            "license_types": "Limited, Intermediate, Unlimited Electrical Contractor",
            "experience_reqs": "Limited: 2 years experience. Intermediate: 4 years. Unlimited: 5 years.",
            "application_info_link": "https://www.ncbeec.org/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and North Carolina electrical code",
            "official_board_link": "https://www.ncbeec.org/"
        },
        {
            "state_name": "North Dakota",
            "license_types": "Master Electrician, Journeyman Electrician, Class B Electrician",
            "experience_reqs": "Journeyman: 8,000 hours as apprentice. Master: 2,000 hours as journeyman.",
            "application_info_link": "https://www.ndseb.com/",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Open-book exam on NEC and North Dakota electrical code",
            "official_board_link": "https://www.ndseb.com/"
        },
        {
            "state_name": "Ohio",
            "license_types": "Electrical Contractor",
            "experience_reqs": "5 years experience in electrical contracting or 3 years with electrical engineering degree",
            "application_info_link": "https://com.ohio.gov/divisions-and-programs/industrial-compliance/boards-and-commissions/ohio-construction-industry-licensing-board",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Business and law exam, technical exam",
            "official_board_link": "https://com.ohio.gov/divisions-and-programs/industrial-compliance/boards-and-commissions/ohio-construction-industry-licensing-board"
        },
        {
            "state_name": "Oklahoma",
            "license_types": "Electrical Contractor, Journeyman Electrician",
            "experience_reqs": "Journeyman: 8,000 hours as apprentice. Contractor: 2 years as journeyman.",
            "application_info_link": "https://cib.ok.gov/electrical-division",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Oklahoma electrical code",
            "official_board_link": "https://cib.ok.gov/electrical-division"
        },
        {
            "state_name": "Oregon",
            "license_types": "General Supervising Electrician, General Journeyman, Limited Journeyman, Limited Residential, Limited Renewable Energy",
            "experience_reqs": "General Journeyman: 8,000 hours as apprentice. General Supervisor: 4,000 hours as journeyman.",
            "application_info_link": "https://www.oregon.gov/bcd/licensing/Pages/index.aspx",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Oregon electrical code",
            "official_board_link": "https://www.oregon.gov/bcd/licensing/Pages/index.aspx"
        },
        {
            "state_name": "Pennsylvania",
            "license_types": "No statewide licensing. Local municipalities regulate licenses.",
            "experience_reqs": "Varies by municipality",
            "application_info_link": "N/A - check with local jurisdictions",
            "tested_nec_version": "Varies by municipality, usually 2017 or 2020 NEC",
            "exam_details": "Varies by municipality",
            "official_board_link": "N/A - check with local jurisdictions"
        }
    ]

    added_count = 0
    skipped_count = 0

    for state_data in final_states:
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
            populate_final_states()
        except Exception as e:
            print(f"Error populating states: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main() 
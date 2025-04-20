import sys
import os
from app import create_app
from models import db, StateInfo

def populate_more_states():
    # Data for more states
    more_states = [
        {
            "state_name": "Indiana",
            "license_types": "No statewide licensing. Local municipalities regulate licenses.",
            "experience_reqs": "Varies by municipality",
            "application_info_link": "N/A - check with local jurisdictions",
            "tested_nec_version": "Varies by municipality, usually 2017 or 2020 NEC",
            "exam_details": "Varies by municipality",
            "official_board_link": "N/A - check with local jurisdictions"
        },
        {
            "state_name": "Iowa",
            "license_types": "Master Electrician, Journeyman Electrician, Apprentice Electrician, Special Electrician, Residential Electrician",
            "experience_reqs": "Journeyman: 4 years as registered apprentice. Master: 2 years as journeyman.",
            "application_info_link": "https://iowaelectrical.gov/licensing/license-types",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Open-book exam on NEC and Iowa electrical code",
            "official_board_link": "https://iowaelectrical.gov/"
        },
        {
            "state_name": "Kansas",
            "license_types": "No statewide licensing. Local municipalities regulate licenses.",
            "experience_reqs": "Varies by municipality",
            "application_info_link": "N/A - check with local jurisdictions",
            "tested_nec_version": "Varies by municipality, usually 2017 or 2020 NEC",
            "exam_details": "Varies by municipality",
            "official_board_link": "N/A - check with local jurisdictions"
        },
        {
            "state_name": "Kentucky",
            "license_types": "Master Electrician, Electrician, Electrical Contractor",
            "experience_reqs": "Electrician: 4 years as apprentice. Master: 2 years as electrician.",
            "application_info_link": "https://ky.gov/licensing/Pages/Electrical-Licensing.aspx",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Kentucky electrical code",
            "official_board_link": "https://ky.gov/licensing/Pages/Electrical-Licensing.aspx"
        },
        {
            "state_name": "Louisiana",
            "license_types": "Electrical Contractor",
            "experience_reqs": "Minimum of 3 years of experience in electrical work",
            "application_info_link": "https://lslbc.louisiana.gov/contractor-licensing/",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Business and Law exam, Technical exam",
            "official_board_link": "https://lslbc.louisiana.gov/"
        },
        {
            "state_name": "Maine",
            "license_types": "Master Electrician, Journeyman Electrician, Limited Electrician, Helper Electrician, Apprentice Electrician",
            "experience_reqs": "Journeyman: 8,000 hours of experience. Master: 4,000 hours as journeyman.",
            "application_info_link": "https://www.maine.gov/pfr/professionallicensing/professions/electricians/",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Closed-book exam on NEC and Maine electrical statutes",
            "official_board_link": "https://www.maine.gov/pfr/professionallicensing/professions/electricians/"
        },
        {
            "state_name": "Maryland",
            "license_types": "Master Electrician, Journeyman Electrician, Apprentice Electrician",
            "experience_reqs": "Master: 7 years experience. Journeyman: 4 years experience.",
            "application_info_link": "https://www.dllr.state.md.us/license/elec/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Written examination on NEC and Maryland-specific requirements",
            "official_board_link": "https://www.dllr.state.md.us/license/elec/"
        },
        {
            "state_name": "Massachusetts",
            "license_types": "Master Electrician, Journeyman Electrician, Systems Contractor, Systems Technician",
            "experience_reqs": "Journeyman: 4 years as registered apprentice. Master: 1 year as journeyman.",
            "application_info_link": "https://www.mass.gov/orgs/board-of-state-examiners-of-electricians",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Open-book exam on NEC and Massachusetts electrical code",
            "official_board_link": "https://www.mass.gov/orgs/board-of-state-examiners-of-electricians"
        },
        {
            "state_name": "Michigan",
            "license_types": "Master Electrician, Journey Electrician, Apprentice Electrician, Fire Alarm Specialty Technician, Sign Specialist",
            "experience_reqs": "Journey: 8,000 hours as apprentice. Master: 2 years as journeyman.",
            "application_info_link": "https://www.michigan.gov/lara/bureau-list/bcc/divisions/licensing-division/electrical",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Michigan electrical code",
            "official_board_link": "https://www.michigan.gov/lara/bureau-list/bcc/about-electrical"
        },
        {
            "state_name": "Minnesota",
            "license_types": "Master Electrician, Journeyman Electrician, Maintenance Electrician, Power Limited Technician",
            "experience_reqs": "Journeyman: 4 years as registered apprentice. Master: 1 year as journeyman.",
            "application_info_link": "https://www.dli.mn.gov/business/electrical-contractors/licensing-information-electrical-contractors",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Open-book exam on NEC and Minnesota electrical code",
            "official_board_link": "https://www.dli.mn.gov/business/electrical-contractors"
        }
    ]

    added_count = 0
    skipped_count = 0

    for state_data in more_states:
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
            populate_more_states()
        except Exception as e:
            print(f"Error populating states: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main() 
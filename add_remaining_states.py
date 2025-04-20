import sys
import os
import json
from app import create_app
from models import db, StateInfo

def populate_remaining_states():
    # Data for remaining states
    remaining_states = [
        {
            "state_name": "Florida",
            "license_types": "Electrical Contractor, Alarm System Contractor",
            "experience_reqs": "At least 6 years of electrical experience, with at least 3 years at the supervisory level.",
            "application_info_link": "http://www.myfloridalicense.com/DBPR/electrical-contractors/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Business and Finance exam, Technical/Safety exam",
            "official_board_link": "http://www.myfloridalicense.com/DBPR/electrical-contractors/"
        },
        {
            "state_name": "Georgia",
            "license_types": "Class I Electrical Contractor (Unrestricted), Class II Electrical Contractor (Restricted)",
            "experience_reqs": "Class I: 4 years of experience. Class II: 3 years of experience.",
            "application_info_link": "https://sos.ga.gov/georgia-state-construction-industry-licensing-board-division-electrical-contractors",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Business and Law exam, Technical exam",
            "official_board_link": "https://sos.ga.gov/georgia-state-construction-industry-licensing-board-division-electrical-contractors"
        },
        {
            "state_name": "Hawaii",
            "license_types": "Electrician (EJ), Supervising Electrician (ES), Journey Worker Industrial Electrician (EJI), Supervising Industrial Electrician (ESI), Journey Worker Specialty Electrician (EJS), Supervising Specialty Electrician (ESS), Maintenance Electrician (EM)",
            "experience_reqs": "Journey Worker: 5 years experience. Supervising: 5 years as a journey worker.",
            "application_info_link": "http://cca.hawaii.gov/pvl/boards/electrician/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Written examination on NEC and Hawaii-specific requirements",
            "official_board_link": "http://cca.hawaii.gov/pvl/boards/electrician/"
        },
        {
            "state_name": "Idaho",
            "license_types": "Master Electrician, Journeyman Electrician, Apprentice Electrician, Limited Electrical Installer",
            "experience_reqs": "Journeyman: 4 years as registered apprentice. Master: 2 years as journeyman.",
            "application_info_link": "https://dbs.idaho.gov/licenses/electrical/",
            "tested_nec_version": "2017 NEC",
            "exam_details": "Open-book exam on NEC and Idaho statutes",
            "official_board_link": "https://dbs.idaho.gov/boards/electrical-board/"
        },
        {
            "state_name": "Illinois",
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

    for state_data in remaining_states:
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
            populate_remaining_states()
        except Exception as e:
            print(f"Error populating states: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main() 
import sys
import os
from app import create_app
from models import db, StateInfo

def populate_missing_states():
    # Data for the 8 missing states
    missing_states = [
        {
            "state_name": "Alabama",
            "license_types": "Journeyman Electrician; Electrical Contractor (unlimited); Electrical Contractor (Restricted)",
            "experience_reqs": "Journeyman license requires at least 8,000 hours of electrical work experience. The Electrical Contractor license requires 4 years experience.",
            "application_info_link": "https://aecb.alabama.gov/licensees/forms/",
            "tested_nec_version": "2023 NEC",
            "exam_details": "Journeyman exam: 80 questions, 4-hour time limit, open-book. Electrical contractor exam: 110 questions, 5-hour limit.",
            "official_board_link": "https://aecb.alabama.gov"
        },
        {
            "state_name": "Alaska",
            "license_types": "Electrical Trainee (Apprentice); Journeyman Electrician; Residential Electrician; Power Lineman (Journeyman); Power Lineman Trainee; Electrical Administrator",
            "experience_reqs": "Journeyman Electrician requires 8,000 hours of work experience. A Residential Electrician needs 4,000 hours of experience.",
            "application_info_link": "https://labor.alaska.gov/lss/plumbing_electrical.htm",
            "tested_nec_version": "2020 NEC",
            "exam_details": "The journeyman electrician exam is 100 questions with a 5-hour time limit. The exam is open-book.",
            "official_board_link": "https://commerce.alaska.gov/cbp/Main/Division?divisionID=8"
        },
        {
            "state_name": "Arizona",
            "license_types": "No state-issued electrician licenses (electricians are licensed at the city/municipal level). Electrical Contractors are licensed by the Arizona Registrar of Contractors (ROC).",
            "experience_reqs": "To become a licensed electrical contractor through the state ROC, one must have 4 years of trade experience.",
            "application_info_link": "https://roc.az.gov/licensing",
            "tested_nec_version": "N/A (no state electrical exam; varies by local jurisdiction)",
            "exam_details": "For a state contractor license, Arizona ROC requires a trade exam and business exam.",
            "official_board_link": "https://roc.az.gov"
        },
        {
            "state_name": "Arkansas",
            "license_types": "Journeyman Electrician; Residential Journeyman Electrician; Master Electrician; Residential Master Electrician",
            "experience_reqs": "Journeyman Electrician requires 8,000 hours of on-the-job electrical training, plus 800 hours of classroom instruction.",
            "application_info_link": "https://www.labor.arkansas.gov/licensing/electrical-examining-board/",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Journeyman exam has about 80 multiple-choice questions with a 4-hour time limit. The Master exam has around 100 questions in 5 hours.",
            "official_board_link": "https://www.labor.arkansas.gov/licensing/electrical-examining-board/"
        },
        {
            "state_name": "California",
            "license_types": "Electrical Trainee; Certified General Electrician; Certified Residential Electrician; Certified Fire/Life Safety Technician; Certified Voice Data Video Technician; C-10 Electrical Contractor",
            "experience_reqs": "Certified General Electrician requires 8,000 hours of on-the-job experience. Certified Residential Electrician requires 4,800 hours of residential electrical experience.",
            "application_info_link": "https://www.dir.ca.gov/dlse/ECU/ElectricalTrade.html",
            "tested_nec_version": "2020 NEC",
            "exam_details": "The California General Electrician certification exam consists of ~100 multiple-choice questions with a 4.5-hour time limit. The exam is closed-book.",
            "official_board_link": "https://www.cslb.ca.gov"
        },
        {
            "state_name": "Colorado",
            "license_types": "Residential Wireman; Journeyman Electrician; Master Electrician; Electrical Contractor",
            "experience_reqs": "Journeyman Electrician requires 8,000 hours of electrical work experience. Master Electrician requires at least one year as a licensed journeyman.",
            "application_info_link": "https://dpo.colorado.gov/Electrical/Applications",
            "tested_nec_version": "2023 NEC",
            "exam_details": "Residential Wireman exam has ~60 questions with a 3-hour limit. Journeyman exam has around 80 questions in 4 hours.",
            "official_board_link": "https://dpo.colorado.gov/Electrical"
        },
        {
            "state_name": "Connecticut",
            "license_types": "Apprentice (registration); Journeyperson Electrician (E-2 Unlimited); Master Electrician (E-1 Unlimited)",
            "experience_reqs": "Journeyperson (E-2) requires 8,000 hours of apprenticeship experience and 720 hours of classroom instruction. Master (E-1) requires an additional 4,000 hours as a licensed journeyperson.",
            "application_info_link": "https://portal.ct.gov/DCP/License-Services/All-License-Applications/Electrical-Licensing-Applications",
            "tested_nec_version": "2020 NEC",
            "exam_details": "The Unlimited Journeyperson (E-2) exam has about 90 questions covering the NEC with a time limit around 4 hours.",
            "official_board_link": "https://portal.ct.gov/DCP/License-Services/Divisions/Professional-Licensing/Electrical-Work-Examining-Board"
        },
        {
            "state_name": "Delaware",
            "license_types": "Apprentice (registration); Journeyperson Electrician; Master Electrician; Master Special Electrician; Limited Electrician; Limited Special Electrician; Residential Electrician",
            "experience_reqs": "Journeyperson requires 8,000 hours on-the-job and typically 576 hours classroom instruction. Master Electrician requires at least 2 years of experience as a licensed journeyperson.",
            "application_info_link": "https://dpr.delaware.gov/boards/electrician/",
            "tested_nec_version": "2020 NEC",
            "exam_details": "The Journeyperson exam consists of ~75 questions on the NEC and general electrical knowledge with a 3.5-hour limit.",
            "official_board_link": "https://dpr.delaware.gov/boards/electrician/"
        }
    ]

    added_count = 0
    skipped_count = 0

    for state_data in missing_states:
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
            populate_missing_states()
        except Exception as e:
            print(f"Error populating states: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main() 
#!/usr/bin/env python
import sys
import os
import json
from app import create_app, db
from models import StateInfo

def populate_state_requirements():
    """Add state licensing requirements to the database."""
    # Alabama to Delaware for first batch
    states_data = [
        {
            "state_name": "Alabama",
            "license_types": "Journeyman Electrician; Electrical Contractor (unlimited); Electrical Contractor (Restricted)",
            "experience_reqs": "Journeyman license requires at least 8,000 hours of electrical work experience (up to 2,000 hours may be substituted by approved education). The Electrical Contractor license requires a minimum of 8,000 hours (approx. 4 years) experience in the design, planning, layout, and direct supervision of electrical construction (often satisfied by four years as a journeyman in charge of jobs). Applicants must document experience and may substitute up to 2,000 hours with education. (Alabama no longer issues new Provisional licenses; those were temporary contractor licenses that expired in 2012.)",
            "application_info_link": "https://aecb.alabama.gov/licensees/forms/",
            "tested_nec_version": "2023 NEC",
            "exam_details": "Journeyman exam: 80 questions, 4-hour time limit, open-book (allowed NEC codebook); covers general electrical knowledge, wiring methods, motors, low voltage, lighting, etc. Electrical contractor exam: 110 questions, 5-hour limit, covering both technical electrical topics and business management (open-book). A score of 75% is required to pass each exam. No practical (hands-on) component is required.",
            "official_board_link": "https://aecb.alabama.gov"
        },
        {
            "state_name": "Alaska",
            "license_types": "Electrical Trainee (Apprentice); Journeyman Electrician; Residential Electrician; Power Lineman (Journeyman); Power Lineman Trainee; Electrical Administrator",
            "experience_reqs": "Journeyman Electrician requires 8,000 hours of work experience, with at least 6,000 hours in commercial or industrial electrical work (up to 1,000 hours of related technical training can substitute). A Residential Electrician needs 4,000 hours of electrical work experience (primarily on residential systems). A Power Lineman Journeyman must typically complete a recognized lineman apprenticeship (around 7,000 hours) or equivalent utility experience. All trainees must register before accumulating hours. To qualify as an Electrical Administrator (the license required to contract or supervise electrical work), one must have been a journeyman in Alaska for at least 4 of the last 6 years and provide letters of reference from three licensed electricians attesting to the applicant's experience and qualifications.",
            "application_info_link": "https://labor.alaska.gov/lss/plumbing_electrical.htm",
            "tested_nec_version": "2020 NEC (currently used for Alaska electrician exams)",
            "exam_details": "Alaska issues a state Certificate of Fitness exam for each category. The journeyman electrician exam is 100 questions (a mix of multiple-choice and true/false) based on the NEC, with a 5-hour time limit. The exam is open-book (candidates may use the NEC codebook). A 70% score is typically required. No practical skills test is required. (Electrical Administrators also have a separate exam focused on code and management.)",
            "official_board_link": "https://commerce.alaska.gov/cbp/Main/Division?divisionID=8"
        },
        {
            "state_name": "Arizona",
            "license_types": "No state-issued electrician licenses (electricians are licensed at the city/municipal level). Electrical Contractors are licensed by the Arizona Registrar of Contractors (ROC) under commercial or residential contracting categories.",
            "experience_reqs": "No state requirements for journeyman or master electrician licensing – requirements are set by local municipalities or unions. Typically, cities require around 4 years (8,000 hours) of apprenticeship under a licensed electrician to become a journeyman. To become a licensed electrical contractor through the state ROC, one must have 4 years of trade experience and pass business and trade exams.",
            "application_info_link": "https://roc.az.gov/licensing",
            "tested_nec_version": "N/A (no state electrical exam; NEC code adoption and exam standards vary by local jurisdiction)",
            "exam_details": "N/A. There is no state electrician exam. Local jurisdictions may administer journeyman exams (often open-book using the NEC). For a state contractor license, Arizona ROC requires a trade exam and business exam specific to the classification, both administered by a testing vendor (open-book with current NEC for the trade portion).",
            "official_board_link": "https://roc.az.gov"
        },
        {
            "state_name": "Arkansas",
            "license_types": "Journeyman Electrician; Residential Journeyman Electrician; Master Electrician; Residential Master Electrician",
            "experience_reqs": "Journeyman Electrician requires 8,000 hours of on-the-job electrical training (approximately 4 years), plus 800 hours of classroom instruction in electrical theory and code. Residential Journeyman requires 2 years of experience specifically in one- and two-family dwelling wiring, along with a letter from a trade school verifying completion of any required training. Master Electrician requires either: a degree in electrical engineering plus 2 years of construction experience, *or* at least 6 years of electrical construction experience including 2 years as a licensed journeyman. Residential Master requires at least 3 years of experience in residential wiring and at least 1 year as a licensed Residential Journeyman.",
            "application_info_link": "https://www.labor.arkansas.gov/licensing/electrical-examining-board/",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Arkansas's electrical exams are administered by Prometric. The Journeyman exam typically has about 80 multiple-choice questions (covering NEC rules, electrical theory, installation practices) with a 4-hour time limit. The Master exam has around 100 questions in 5 hours. All exams are open-book, and candidates may use the NEC Code book during testing. A score of 75% is generally needed to pass. No practical hands-on exam is required.",
            "official_board_link": "https://www.labor.arkansas.gov/licensing/electrical-examining-board/"
        },
        {
            "state_name": "California",
            "license_types": "Electrical Trainee; Certified General Electrician; Certified Residential Electrician; Certified Fire/Life Safety Technician; Certified Voice Data Video Technician; Certified Non-Residential Lighting Technician; C-10 Electrical Contractor",
            "experience_reqs": "California requires electrician certification for anyone performing work as an electrician for a C-10 contractor. To test for Certified General Electrician, one needs at least 8,000 hours (about 4 years) of on-the-job experience in electrical construction under appropriate supervision. Certified Residential Electrician requires 4,800 hours of residential electrical experience. Other specialty certifications (Voice Data Video, Fire/Life Safety, etc.) require around 4,000 hours in that specialty. All aspiring electricians must first register as an Electrical Trainee if they are not yet certified. To become a licensed Electrical Contractor (C-10) in California, an individual must either be a certified electrician or have managerial experience and must demonstrate at least 4 years of journey-level experience, then pass the state contractor's trade exam and business-law exam.",
            "application_info_link": "https://www.dir.ca.gov/dlse/ECU/ElectricalTrade.html",
            "tested_nec_version": "2020 NEC (California exams currently reference the 2017 NEC with state amendments, moving to 2020 NEC under the latest California Electrical Code)",
            "exam_details": "The California General Electrician certification exam is administered by PSI. It consists of ~100 multiple-choice questions with a 4.5-hour time limit. The exam is closed-book (California does **not** allow the NEC codebook during the electrician certification exam). It tests on the California Electrical Code (based on the NEC) and practical electrical knowledge. A passing score of 70% is required. The C-10 Electrical Contractor exam is separate, consisting of a 100-question trade exam (open-book with the NEC allowed) and a 120-question law/business exam. No practical performance test is required for either certification or contractor licensing.",
            "official_board_link": "https://www.cslb.ca.gov"
        },
        {
            "state_name": "Colorado",
            "license_types": "Residential Wireman; Journeyman Electrician; Master Electrician; Electrical Contractor",
            "experience_reqs": "Residential Wireman requires 4,000 hours (about 2 years) of electrical work experience restricted to residential (one- and two-family dwellings). Journeyman Electrician requires 8,000 hours (~4 years) of applicable electrical construction work experience; Colorado also accepts 6,000 hours if combined with an approved 2-year electrical school degree. Master Electrician requires at least one year as a licensed journeyman (Colorado specifies 2,000 hours of experience as a journeyman) in addition to the journeyman requirements, for a total of about 5 years of experience. An Electrical Contractor license in Colorado is an organizational license issued if the company employs a master electrician who takes responsibility for all work (the master must be either an owner or a supervising employee).",
            "application_info_link": "https://dpo.colorado.gov/Electrical/Applications",
            "tested_nec_version": "2023 NEC",
            "exam_details": "Colorado's exams are administered by PSI. The Residential Wireman exam has ~60 questions with a 3-hour limit, and the Journeyman exam around 80 questions in 4 hours; the Master exam may have ~90 questions in 5 hours. All are open-book exams using the NEC (current code is the 2023 NEC). A score of 70% is needed to pass. Exam topics include circuits, wiring methods, overcurrent protection, grounding, and Colorado electrical statutes. No practical test is required. The Electrical Contractor registration itself does not require an additional exam beyond the master electrician exam.",
            "official_board_link": "https://dpo.colorado.gov/Electrical"
        },
        {
            "state_name": "Connecticut",
            "license_types": "Apprentice (registration); Journeyperson Electrician (E-2 Unlimited Electrical Journeyperson and various limited journeyperson categories); Master Electrician (E-1 Unlimited Electrical Contractor and limited contractor categories)",
            "experience_reqs": "Connecticut requires a registered apprenticeship for electricians. To qualify for the Unlimited Journeyperson (E-2) exam, one must complete 8,000 hours (4 years) of apprenticeship experience and 720 hours of classroom instruction in electrical theory, code, and safety. There are also limited electrical journeyperson licenses (for specialties like low-voltage, alarm systems, etc.) with different hour requirements (generally 4,000 hours for limited categories). To become an Unlimited Electrical Contractor (E-1 Master), a candidate must first hold the E-2 journeyperson license and accumulate an additional two years (4,000 hours) as a licensed journeyperson. Limited electrical contractor licenses similarly require experience as a corresponding journeyperson. All experience must be verifiable and under the supervision of a licensed contractor.",
            "application_info_link": "https://portal.ct.gov/DCP/License-Services/All-License-Applications/Electrical-Licensing-Applications",
            "tested_nec_version": "2020 NEC (Connecticut has adopted the 2020 NEC effective October 1, 2022)",
            "exam_details": "Connecticut's electrician exams are administered by PSI. The Unlimited Journeyperson (E-2) exam typically has about 90 questions (multiple-choice) covering the NEC, Connecticut amendments, and electrical trade knowledge, with a time limit around 4 hours. The Unlimited Contractor (E-1) exam adds questions on business law and project supervision (often given in two parts: a technical part and a business part). All exams are open-book; candidates may use the NEC code book and other approved reference materials. A 70% score is required to pass. No practical component is included.",
            "official_board_link": "https://portal.ct.gov/DCP/License-Services/Divisions/Professional-Licensing/Electrical-Work-Examining-Board"
        },
        {
            "state_name": "Delaware",
            "license_types": "Apprentice (registration); Journeyperson Electrician; Master Electrician; Master Special Electrician; Limited Electrician; Limited Special Electrician; Residential Electrician",
            "experience_reqs": "Delaware requires all practicing electricians to be licensed. To qualify as a Journeyperson in Delaware, an applicant needs to complete an apprenticeship (8,000 hours on-the-job and typically 576 hours classroom) or have 6 years of supervised electrical experience. A Master Electrician requires at least 2 years of experience as a licensed journeyperson or 7 years of total experience in electrical work. "Master Special" licenses (for specialties like HVAC, signs, etc.) typically also require 7 years in the limited area. A Limited Electrician license (restricted scope) requires 3 years of experience in the limited area, and a Limited Special requires 3 years in that specialty. Residential Electrician requires 4,000 hours of residential-only experience. All experience must be documented and typically verified by a supervising Master or contractor. Delaware also allows substitute credit for technical school (e.g., 2 years of trade school may count as 2,000 hours).",
            "application_info_link": "https://dpr.delaware.gov/boards/electrician/",
            "tested_nec_version": "2020 NEC",
            "exam_details": "Delaware uses third-party testing (through PSI) for exams. The Journeyperson exam usually consists of ~75 questions on the NEC and general electrical knowledge, 3.5-hour limit, open-book (2020 NEC allowed). The Master Electrician exam is longer (~100 questions, 4-hour limit) and covers more complex calculations and Code provisions. A 75% score is needed to pass. Exams are open-book with the NEC and other permitted references (e.g. Ugly's Electrical References). There is no practical/hands-on exam. Additionally, Delaware requires candidates to pass a separate test on Delaware state law and code amendments as part of licensure.",
            "official_board_link": "https://dpr.delaware.gov/boards/electrician/"
        }
    ]
    
    added_count = 0
    existing_count = 0
    
    for state_data in states_data:
        # Check if this state already exists
        existing_state = StateInfo.query.filter_by(state_name=state_data["state_name"]).first()
        
        if existing_state:
            # Update existing state
            existing_state.license_types = state_data["license_types"]
            existing_state.experience_reqs = state_data["experience_reqs"]
            existing_state.application_info_link = state_data["application_info_link"]
            existing_state.tested_nec_version = state_data["tested_nec_version"]
            existing_state.exam_details = state_data["exam_details"]
            existing_state.official_board_link = state_data["official_board_link"]
            existing_count += 1
            print(f"Updated existing state: {state_data['state_name']}")
        else:
            # Create new state entry
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
            added_count += 1
            print(f"Added new state: {state_data['state_name']}")
    
    db.session.commit()
    print(f"States added: {added_count}")
    print(f"States updated: {existing_count}")
    return added_count, existing_count

def main():
    try:
        app = create_app()
        with app.app_context():
            added, updated = populate_state_requirements()
            print(f"Successfully added {added} states and updated {updated} states")
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main()) 
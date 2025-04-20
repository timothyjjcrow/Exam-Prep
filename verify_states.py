import sys
from app import create_app
from models import db, StateInfo

def verify_states():
    # Get all states from the database
    all_states = StateInfo.query.order_by(StateInfo.state_name).all()
    
    # Expected state count
    expected_count = 50
    
    # Print state count and name of each state
    print(f"Total states in database: {len(all_states)}")
    print(f"Expected states: {expected_count}")
    print("\nStates in database:")
    
    for i, state in enumerate(all_states, 1):
        print(f"{i}. {state.state_name}")
    
    # Check for missing states
    all_us_states = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", 
        "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", 
        "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", 
        "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", 
        "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", 
        "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", 
        "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", 
        "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", 
        "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", 
        "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ]
    
    db_state_names = [state.state_name for state in all_states]
    
    # Check for missing states
    missing_states = [state for state in all_us_states if state not in db_state_names]
    if missing_states:
        print("\nMissing states:")
        for state in missing_states:
            print(f"- {state}")
    else:
        print("\nAll 50 states are present in the database!")

def main():
    app = create_app()
    with app.app_context():
        try:
            verify_states()
        except Exception as e:
            print(f"Error verifying states: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main() 
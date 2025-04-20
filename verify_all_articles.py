import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import app factory and db
from app import create_app, db
from models import NECArticle

def verify_nec_articles():
    """Verifies all required NEC articles are in the database with proper content."""
    
    # List of articles we expect to find
    required_articles = [
        {"article_number": "90", "title": "Introduction"},
        {"article_number": "100", "title": "Definitions"},
        {"article_number": "110", "title": "Requirements for Electrical Installations"},
        {"article_number": "200", "title": "Use and Identification of Grounded Conductors"},
        {"article_number": "210", "title": "Branch Circuits"},
        {"article_number": "220", "title": "Branch-Circuit, Feeder, and Service Calculations"},
        {"article_number": "250", "title": "Grounding and Bonding"},
        {"article_number": "300", "title": "Wiring Methods and Materials"},
        {"article_number": "310", "title": "Conductors for General Wiring"},
        {"article_number": "334", "title": "Nonmetallic-Sheathed Cable: Types NM, NMC, and NMS"},
        {"article_number": "352", "title": "Rigid Polyvinyl Chloride Conduit: Type PVC"},
        {"article_number": "404", "title": "Switches"},
        {"article_number": "406", "title": "Receptacles, Cord Connectors, and Attachment Plugs (Caps)"},
        {"article_number": "422", "title": "Appliances"},
        {"article_number": "430", "title": "Motors, Motor Circuits, and Controllers"},
        {"article_number": "700", "title": "Emergency Systems"}
    ]
    
    print("=== NEC ARTICLES VERIFICATION ===")
    print(f"Checking for {len(required_articles)} required articles...\n")
    
    found_count = 0
    missing_count = 0
    incomplete_count = 0
    
    # Check each required article
    for article_info in required_articles:
        article_number = article_info["article_number"]
        expected_title = article_info["title"]
        
        # Look up the article in the database
        article = NECArticle.query.filter_by(article_number=article_number).first()
        
        if article:
            # Article exists, check content
            title_match = article.title == expected_title
            has_content = len(article.content) > 200  # Basic check for substantial content
            
            if title_match and has_content:
                print(f"✅ Article {article_number}: {article.title} - FOUND [Content: {len(article.content)} chars]")
                found_count += 1
            else:
                status = []
                if not title_match:
                    status.append(f"Title mismatch (expected: '{expected_title}', got: '{article.title}')")
                if not has_content:
                    status.append(f"Content may be incomplete ({len(article.content)} chars)")
                
                print(f"⚠️ Article {article_number}: {article.title} - INCOMPLETE [{', '.join(status)}]")
                incomplete_count += 1
        else:
            print(f"❌ Article {article_number}: {expected_title} - MISSING")
            missing_count += 1
    
    # Summarize results
    print("\n=== VERIFICATION SUMMARY ===")
    print(f"Total articles checked: {len(required_articles)}")
    print(f"Found complete: {found_count}")
    print(f"Found but incomplete: {incomplete_count}")
    print(f"Missing: {missing_count}")
    
    if missing_count > 0 or incomplete_count > 0:
        print("\nRecommendation: Run the appropriate update scripts to add or complete the missing articles.")
    else:
        print("\nAll required NEC articles are present and complete!")

def main():
    """Create app context and run the verification function."""
    try:
        app = create_app()
        with app.app_context():
            verify_nec_articles()
    except Exception as e:
        print(f"Error during verification: {str(e)}")

if __name__ == "__main__":
    main() 
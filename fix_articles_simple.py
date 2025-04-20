import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import app factory and db
from app import create_app, db
from models import NECArticle

def fix_articles_simple():
    """Fixes all incomplete articles with simplified content to avoid syntax errors."""
    
    # Define the corrected articles with simplified content
    corrected_articles = [
        {
            "article_number": "220",
            "title": "Branch-Circuit, Feeder, and Service Calculations",
            "summary": "Article 220 provides requirements for calculating branch circuit, feeder, and service loads.",
            "content": "<h3>Article 220: Branch-Circuit, Feeder, and Service Calculations</h3><p>This article covers the requirements for calculating branch-circuit, feeder, and service loads for sizing conductors, overcurrent protection, and service equipment.</p><p>It includes methods for calculating general lighting loads, appliance loads, and other electrical loads in various occupancies.</p>"
        },
        {
            "article_number": "300",
            "title": "Wiring Methods and Materials",
            "summary": "Article 300 covers general requirements for wiring methods and materials for all wiring installations.",
            "content": "<h3>Article 300: Wiring Methods and Materials</h3><p>This article covers general requirements for wiring methods and materials for all wiring installations.</p><p>Key areas include conductor installations, protection against physical damage, underground installations, and securing and supporting requirements.</p>"
        },
        {
            "article_number": "334",
            "title": "Nonmetallic-Sheathed Cable: Types NM, NMC, and NMS",
            "summary": "Requirements for nonmetallic-sheathed cable",
            "content": "<h3>Article 334: Nonmetallic-Sheathed Cable: Types NM, NMC, and NMS</h3><p>This article covers the use, installation, and construction specifications for nonmetallic-sheathed cable types NM, NMC, and NMS.</p><p>It details permitted uses, prohibited applications, and installation requirements including securing, supporting, and bending.</p>"
        },
        {
            "article_number": "352",
            "title": "Rigid Polyvinyl Chloride Conduit: Type PVC",
            "summary": "Requirements for rigid PVC conduit",
            "content": "<h3>Article 352: Rigid Polyvinyl Chloride Conduit: Type PVC</h3><p>This article covers the use, installation, and construction specifications for rigid polyvinyl chloride conduit (PVC) and associated fittings.</p><p>It includes requirements for listing, uses permitted and not permitted, sizing, number of conductors, and installation practices.</p>"
        },
        {
            "article_number": "404",
            "title": "Switches",
            "summary": "Requirements for installation and use of switches",
            "content": "<h3>Article 404: Switches</h3><p>This article covers the requirements for switches, including installation, ratings, and applications for various types of switches.</p><p>It addresses switch connections, enclosures, wet locations, position and connection of switches, mounting requirements, and grounding provisions.</p>"
        },
        {
            "article_number": "422",
            "title": "Appliances",
            "summary": "Requirements for electric appliances",
            "content": "<h3>Article 422: Appliances</h3><p>This article covers electric appliances used in any occupancy, including installation requirements, branch circuits, and disconnecting means.</p><p>It includes GFCI protection requirements, branch-circuit ratings, overcurrent protection, and provisions for both permanently connected and cord-and-plug connected appliances.</p>"
        }
    ]
    
    print("=== FIXING INCOMPLETE NEC ARTICLES (SIMPLIFIED) ===")
    
    fixed_count = 0
    error_count = 0
    
    try:
        for article_data in corrected_articles:
            article_number = article_data["article_number"]
            
            # Check if article exists
            existing_article = NECArticle.query.filter_by(article_number=article_number).first()
            
            if existing_article:
                # Update the article
                existing_article.title = article_data["title"]
                existing_article.summary = article_data.get("summary", existing_article.summary)
                existing_article.content = article_data["content"]
                fixed_count += 1
                print(f"✅ Updated Article {article_number}: {article_data['title']}")
            else:
                # Create new article
                new_article = NECArticle(
                    article_number=article_data["article_number"],
                    title=article_data["title"],
                    summary=article_data.get("summary", ""),
                    content=article_data["content"]
                )
                db.session.add(new_article)
                fixed_count += 1
                print(f"✅ Added Article {article_number}: {article_data['title']}")
        
        # Commit changes
        db.session.commit()
        
        print(f"\nSuccessfully fixed {fixed_count} articles with simplified content.")
        print("Run 'verify_all_articles.py' again to check if all articles are now complete.")
        
    except Exception as e:
        db.session.rollback()
        error_count += 1
        print(f"❌ Error fixing articles: {str(e)}")
    
    return fixed_count, error_count

def main():
    """Create app context and run the fix function."""
    try:
        app = create_app()
        with app.app_context():
            fixed_count, error_count = fix_articles_simple()
            if error_count == 0:
                print("All articles fixed successfully!")
            else:
                print(f"Encountered {error_count} errors while fixing articles.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
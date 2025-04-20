import sys
import os
from flask import Flask

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import app factory and db
from app import create_app, db
from models import NECArticle

def update_nec_articles_batch3():
    """Update or add NEC articles to the database (third batch)."""
    # List of updated NEC articles
    updated_articles = [
        {
            "article_number": "334",
            "title": "Nonmetallic-Sheathed Cable: Types NM, NMC, and NMS",
            "summary": "Requirements for nonmetallic-sheathed cable",
            "content": "<h3>Article 334: Nonmetallic-Sheathed Cable</h3><p>This article covers the use, installation, and construction specifications for nonmetallic-sheathed cable.</p>"
        },
        {
            "article_number": "352",
            "title": "Rigid Polyvinyl Chloride Conduit: Type PVC",
            "summary": "Requirements for rigid PVC conduit",
            "content": "<h3>Article 352: Rigid PVC Conduit</h3><p>This article covers the use, installation, and construction specifications for rigid polyvinyl chloride conduit.</p>"
        },
        {
            "article_number": "404",
            "title": "Switches",
            "summary": "Requirements for installation and use of switches",
            "content": "<h3>Article 404: Switches</h3><p>This article covers the requirements for switches, including installation, ratings, and applications for various types of switches.</p>"
        },
        {
            "article_number": "406",
            "title": "Receptacles, Cord Connectors, and Attachment Plugs (Caps)",
            "summary": "Requirements for receptacles, cord connectors, and attachment plugs",
            "content": "<h3>Article 406: Receptacles, Cord Connectors, and Attachment Plugs (Caps)</h3><p>This article covers the installation and use of all receptacles, cord connectors, and attachment plugs (cord caps).</p>"
        },
        {
            "article_number": "422",
            "title": "Appliances",
            "summary": "Requirements for electric appliances",
            "content": "<h3>Article 422: Appliances</h3><p>This article covers electric appliances used in any occupancy, including installation requirements, branch circuits, and disconnecting means.</p>"
        },
        {
            "article_number": "430",
            "title": "Motors, Motor Circuits, and Controllers",
            "summary": "Requirements for motors, motor branch-circuit and feeder conductors and their protection",
            "content": "<h3>Article 430: Motors, Motor Circuits, and Controllers</h3><p>This article covers motors, motor branch-circuit and feeder conductors and their protection, motor overload protection, motor control circuits, motor controllers, and motor control centers.</p>"
        },
        {
            "article_number": "700",
            "title": "Emergency Systems",
            "summary": "Requirements for emergency systems that provide illumination or power upon loss of normal power supply",
            "content": "<h3>Article 700: Emergency Systems</h3><p>This article applies to the electrical safety of the installation, operation, and maintenance of emergency systems consisting of circuits and equipment intended to supply, distribute, and control electricity for illumination or power, or both, to required facilities when the normal electrical supply or system is interrupted.</p>"
        }
    ]
    
    # Track statistics
    added_count = 0
    updated_count = 0
    skipped_count = 0
    
    try:
        # Process each article
        for article_data in updated_articles:
            # Check if article exists
            existing_article = NECArticle.query.filter_by(
                article_number=article_data["article_number"]
            ).first()
            
            if existing_article:
                # Update existing article
                existing_article.title = article_data["title"]
                existing_article.summary = article_data["summary"]
                existing_article.content = article_data["content"]
                updated_count += 1
                print(f"Updated Article {article_data['article_number']}: {article_data['title']}")
            else:
                # Create new article
                new_article = NECArticle(
                    article_number=article_data["article_number"],
                    title=article_data["title"],
                    summary=article_data["summary"],
                    content=article_data["content"]
                )
                db.session.add(new_article)
                added_count += 1
                print(f"Added Article {article_data['article_number']}: {article_data['title']}")
        
        # Commit changes
        db.session.commit()
        
        print(f"\nNEC Article Update Summary (Batch 3):")
        print(f"Articles added: {added_count}")
        print(f"Articles updated: {updated_count}")
        print(f"Articles skipped: {skipped_count}")
        print(f"Total processed: {added_count + updated_count + skipped_count}")
        
        return True
        
    except Exception as e:
        db.session.rollback()
        print(f"Error updating NEC articles: {str(e)}")
        return False

def main():
    """Create app context and run the update function."""
    try:
        app = create_app()
        with app.app_context():
            success = update_nec_articles_batch3()
            if success:
                print("NEC article update (batch 3) completed successfully.")
            else:
                print("NEC article update (batch 3) failed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

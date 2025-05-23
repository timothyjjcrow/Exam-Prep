from vercel_app import create_app
import os
from api.init_db import initialize_db

# Create the Flask application
app = create_app()

# Initialize the database with sample data if running on Vercel
if os.environ.get('VERCEL'):
    try:
        with app.app_context():
            initialize_db(app)
    except Exception as e:
        print(f"Error initializing database: {str(e)}")

# This is required for Vercel serverless deployment - properly formatted WSGI handler
def handler(event, context):
    return app(event, context) 
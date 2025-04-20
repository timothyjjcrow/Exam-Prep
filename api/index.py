from vercel_app import create_app
import os
from api.init_db import initialize_db

# Create the Flask application
app = create_app()

# Initialize the database with sample data if running on Vercel
if os.environ.get('VERCEL'):
    with app.app_context():
        initialize_db(app)

# This is required for Vercel serverless deployment
handler = app 
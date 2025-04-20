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
            print("Database initialized successfully")
    except Exception as e:
        print(f"Error initializing database: {str(e)}")

# Standard WSGI handler format
def app_handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

# Vercel handler
handler = app 
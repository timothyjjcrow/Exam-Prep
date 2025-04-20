import os

# Secret key for session management and form security
SECRET_KEY = 'development_secret_key_change_in_production'

# Database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False 
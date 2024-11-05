import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# REMOVED PERSAONAL LOGIN DETAILS
# Connect to the database
db_name = "postgres"
db_pword = "Alona1996l!"

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = f'postgresql://{db_name}:{db_pword}@localhost:5432/fyyurapp'
SQLALCHEMY_TRACK_MODIFICATIONS = False

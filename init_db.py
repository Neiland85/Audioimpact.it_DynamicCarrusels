# init_db.py
from app import db

# Initialize the database
db.create_all()
print("Database initialized.")


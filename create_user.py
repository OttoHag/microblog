#!/usr/bin/env python
"""Create a test user for development."""

from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    # Check if user already exists
    existing_user = db.session.query(User).filter_by(username='Geir Otto').first()
    if existing_user:
        print("User 'Geir Otto' already exists!")
    else:
        # Create new user
        user = User(username='Geir Otto', email='geirolar@hotmail.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        print("User 'Geir Otto' created successfully with password: password123")

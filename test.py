from datetime import datetime, timedelta, timezone
import unittest
from app import create_app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_follow(self):
        u = User(username='john', email='john@example.com')
        self.assertEqual(u.avatar(128),
                         'https://www.gravatar.com/avatar/527bd5b5d689e25c3d3c8d0f1f5f6e46?d=identicon&s=128')
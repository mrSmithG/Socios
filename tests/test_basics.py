import unittest
from flask import current_app
from project import create_app, db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing') or current_app
        if not self.app.testing:
            self.app.app_context().push()
            db.create_all()

    def tearDrown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertFalse(current_app.config['TESTING'])

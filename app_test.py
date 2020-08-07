import pytest
import os
from app import app, db

TEST_DB = 'test.db'

class TestCaseBasic:
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        assert response.status_code == 200

    def test_database(self):
        tester = os.path.exists('flaskr.db')
        assert tester is True


class TestCaseFlaskr:
    def setup(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(basedir, TEST_DB))
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def login(self, username, password):
        return self.app.post('/login', data=dict(username=username, password=password), follow_redirects=True)

    def logout(self):
        return self.app.post('/login', follow_redirects=True)

    def test_empty_db(self):
        rv = self.app.get('/')
        assert rv.data.contains(a, b)('No entries yet. Add some!') 

    def test_login_logout(self):
        rv = self.login(self.app.config['USERNAME'], self.app.config['PASSWORD'])
        assert rv.data().contain('You were logged in')
        rv = self.logout()
        assert rv.data.contain('You were logged out')




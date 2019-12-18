from auth.app import create_app
from unittest.mock import patch, Mock
import pytest
from auth.app import create_app


@pytest.fixture
def app():
    '''
    Builds and configures a new app instance for each test
    Automatically manages the temporary files.
    '''

    app = create_app(config='tests/config_test.py')
    yield app


@pytest.fixture()
def client_factory(app):

    class ClientFactory:

        def __init__(self, app):
            self._app = app

        def get(self):
            return self._app.test_client()

    return ClientFactory(app)


@pytest.fixture()
def client(app, client_factory):
    return client_factory.get()


@pytest.fixture
def client(app, client_factory):
    '''
    Builds a new test client instance.
    '''
    return client_factory.get()


@pytest.fixture()
def jwt_token(app):

    class JWTActions():

        def create_token(self, identity, refresh=False, max_age=None):
            with app.app_context():
                if refresh:
                    return jwt.create_refresh_token(identity,
                                                    expires_delta=max_age)
                return jwt.create_access_token(identity,
                                               expires_delta=max_age)

        def set_token(self, response, token, refresh=False):
            with app.app_context():
                if refresh:
                    jwt.set_refresh_cookies(response, token)
                else:
                    jwt.set_access_cookies(response, token)

        def token_headers(self, identity, refresh=False, max_age=None):
            with app.app_context():
                token = self.create_token(identity, max_age=max_age)
                res = jsonify({})
                self.set_token(res, token)
                if refresh:
                    token = self.create_token(
                        identity, refresh=True, max_age=max_age)
                    self.set_token(res, token, refresh=True)
                return res.headers['Set-Cookie']

    return JWTActions()

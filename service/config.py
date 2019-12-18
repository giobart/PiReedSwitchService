# -*- coding: utf-8 -*-
import os

SECRET_KEY = 'change me please'

# Upstream requests timeout in seconds
REQUESTS_TIMEOUT = 0.33

# Microservices endpoints
AUTH_ENDPOINT = os.getenv('AUTH_API', 'localhost:5005')
NOTIFICATION_ENDPOINT = os.getenv('NOTIFICATION_ENDPOINT', 'localhost:5005')

# JWT
SECRET_KEY = 'some-secret-string-CHANGE-ME'
JWT_SECRET_KEY = 'jwt-secret-string-CHANGE-ME'
JWT_TOKEN_LOCATION = ['cookies']
JWT_ACCESS_COOKIE_PATH = '/'
JWT_REFRESH_COOKIE_PATH = '/auth/token_refresh'
JWT_COOKIE_CSRF_PROTECT = False  # False for debug purpose
JWT_COOKIE_SECURE = False  # True for only https

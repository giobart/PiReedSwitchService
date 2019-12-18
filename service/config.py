# -*- coding: utf-8 -*-
import os
from service.api_key import MY_KEY

SECRET_KEY = 'change me please'

# Upstream requests timeout in seconds
REQUESTS_TIMEOUT = 0.33

# Microservices endpoints
AUTH_ENDPOINT = os.getenv('AUTH_API', 'localhost:5005')
NOTIFICATION_ENDPOINT = os.getenv('NOTIFICATION_ENDPOINT', 'https://maker.ifttt.com/trigger/reed_switch_triggered/with/key/'+MY_KEY)

# JWT
SECRET_KEY = 'some-secret-string-CHANGE-ME'
JWT_SECRET_KEY = 'jwt-secret-string-CHANGE-ME'
JWT_TOKEN_LOCATION = ['cookies']
JWT_ACCESS_COOKIE_PATH = '/'
JWT_REFRESH_COOKIE_PATH = '/auth/token_refresh'
JWT_COOKIE_CSRF_PROTECT = False  # False for debug purpose
JWT_COOKIE_SECURE = False  # True for only https

# GPIO Sensors
REED_OUT = os.getenv('REED_OUT', 16)
REED_1_IN = os.getenv('REED_1_IN', 21)

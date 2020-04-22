import os

from flask import Flask
from service.views import blueprints
from service.extensions import jwt
from flask_cors import CORS
from service.tasks.web_page_test import time_loop

__all__ = ('create_app',)


def create_app(config=None, app_name='service'):
    """
    Prepares initializes the application and its utilities.
    """

    app = Flask(app_name)
    CORS(app)

    if config:
        app.config.from_pyfile(config)

    jwt.init_app(app)

    for bp in blueprints:
        app.register_blueprint(bp)
        bp.app = app

    time_loop.start(block=False)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)

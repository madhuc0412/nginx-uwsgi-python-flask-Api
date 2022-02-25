from flask import Flask
from app import settings
from flask import has_request_context, request
import logging


def create_app():

    application = Flask(__name__)

    if settings.SECRET_KEY is not None:
        application.config['SECRET_KEY'] = settings.SECRET_KEY

    register_blueprints(application)

    # configure_logging(application)

    return application



def register_blueprints(application):
    from app.routes import Routes
    application.register_blueprint(Routes, url_prefix=f'/api/v{int(float(settings.VERSION))}', cli_group=None)


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


def configure_logging(application):
    from flask.logging import default_handler
    from logging.handlers import RotatingFileHandler

    formatter = RequestFormatter(
        '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
        '%(levelname)s in %(module)s: %(message)s'
    )

    file_handler = RotatingFileHandler('flaskapp.log', maxBytes=16384, backupCount=20)
    file_handler.setFormatter(formatter)

    application.logger.removeHandler(default_handler)
    application.logger.addHandler(file_handler)




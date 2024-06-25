"""Configure env variables."""
from os import environ


class Config:
    """Set Flask configuration variables from .env file."""

    # General Flask Config
    TEMPLATES_AUTO_RELOAD = environ.get('TEMPLATES_AUTO_RELOAD')
    DEBUG = environ.get('DEBUG')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')

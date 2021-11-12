"""Configure env variables."""
from os import environ, path
from dotenv import load_dotenv


class Config:
    """Set Flask configuration variables from .env file."""

    if path.exists(".env"):
        load_dotenv('.env', verbose=True)

    # General Flask Config
    TEMPLATES_AUTO_RELOAD = environ.get('TEMPLATES_AUTO_RELOAD')
    DEBUG = environ.get('DEBUG')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')

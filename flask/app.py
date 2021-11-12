"""Run the jewels."""
from application import app
from dotenv import load_dotenv
from os import path

if __name__ == "__main__":
    if path.exists(".env"):
        load_dotenv('.env', verbose=True)

    app.run()

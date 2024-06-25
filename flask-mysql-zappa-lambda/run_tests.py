"""Run the unit tests."""
from tests.test_basic import BasicTests
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    if os.path.exists("tests/.env"):
        load_dotenv('tests/.env', verbose=True)
    BasicTests().run_tests()

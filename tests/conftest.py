import pytest
from os import getenv
from pathlib import Path
from dotenv import load_dotenv


@pytest.fixture(scope="module")
def app():
    # Configure enviroments
    env_path = Path('/home/rodrigo/app/personal/flask-study') / '.env'
    load_dotenv(dotenv_path=env_path)

    # Create instance of app
    from app import create_app
    return create_app('testing')

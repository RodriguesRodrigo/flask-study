from os import getenv
from dotenv import load_dotenv

load_dotenv()

from app import create_app

app = create_app(getenv('FLASK_ENV'))

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=app.config['APP_PORT'],
        debug=app.config['DEBUG'],
    )

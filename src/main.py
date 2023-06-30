from cli import app
from simplelogin import settings
import os

if __name__ == "__main__":
    token = os.getenv(settings.TOKEN_ENV_VARIABLE_NAME)
    if token:
        settings.TOKEN = token
    app()


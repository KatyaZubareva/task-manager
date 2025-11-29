# Authentication routes (login, signup, logout)
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta

import secrets

from models import User

secure_key = secrets.token_hex(32)

SECRET_KEY = secure_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_sheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token():
    pass


def get_current_user():
    pass
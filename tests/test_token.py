import pytest
from datetime import datetime, timedelta
from FastAuth.token import Token, SECRET_KEY, ALGORITHM
import jwt

# Sample User data
user_data = {
    "id": 1,
    "username": "test_user",
    "email": "test_user@example.com"
}

# Mock User model
class MockUser:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

@pytest.fixture
def user():
    return MockUser(**user_data)

def test_create_token(user):
    token = Token.create(user)
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert decoded_token["username"] == user.username
    assert decoded_token["email"] == user.email
    assert "exp" in decoded_token
    assert "iat" in decoded_token
    assert "nbf" in decoded_token

def test_create_token_with_expiry(user):
    expires_delta = timedelta(minutes=10)
    token = Token.create(user, expires_delta)
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    exp = decoded_token["exp"]
    expected_exp = datetime.now() + expires_delta
    assert exp == int(expected_exp.timestamp())

def test_validate_token(user):
    token = Token.create(user)
    assert Token.validate(token) == True

def test_validate_invalid_token():
    invalid_token = "invalid.token.string"
    assert Token.validate(invalid_token) == False

def test_expired_token(user):
    expires_delta = timedelta(seconds=1)
    token = Token.create(user, expires_delta)
    assert Token.validate(token) == True

    # Wait for the token to expire
    import time
    time.sleep(2)
    
    assert Token.validate(token) == False
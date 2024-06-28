from .models import JWTToken, User
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "key" # TODO: Find a solution for the secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token:

    def create(user: User, expires_delta: timedelta | None = None) -> str:
        NOW = datetime.now()
        nbf = NOW
        iat = NOW
        user_dict = user.dict()

        # Set JWT Expire Time
        if expires_delta:
            exp = datetime.now() + expires_delta
        else:
            exp = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        # Create Encodable JWT Object
        jwt_token = JWTToken(nbf=nbf,exp=exp,iat=iat).dict()
        jwt_token.update(user_dict)

        # Dynamically clears out any data that is None
        for key in jwt_token.copy():
            if not jwt_token[key]:
                jwt_token.pop(key)

        encoded_jwt = jwt.encode(jwt_token, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
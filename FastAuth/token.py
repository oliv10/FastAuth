from .models import JWTToken, User
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "key" # TODO: Find a solution for the secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token:

    @staticmethod
    def create(user: User, expires_delta: timedelta | None = None, jwt_token: JWTToken = None) -> str:
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
        if jwt_token:
            jwt_token_dict = jwt_token.dict()
            jwt_token_dict.update(user_dict)
        else:
            jwt_token_dict = JWTToken(nbf=nbf,exp=exp,iat=iat).dict()
            jwt_token_dict.update(user_dict)

        # Dynamically clears out any data that is None
        for key in jwt_token_dict.copy():
            if not jwt_token_dict[key]:
                jwt_token_dict.pop(key)

        encoded_jwt = jwt.encode(jwt_token_dict, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def validate(token) -> bool:
        try:
            jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return True
        except:
            return False
from fastapi import Depends
from fastauth.models import User
from fastapi.security import HTTPBearer, APIKeyHeader
from fastapi.security.http import HTTPAuthorizationCredentials


bearer_header = HTTPBearer(auto_error=False)
api_header = APIKeyHeader(name="x-api-key", auto_error=False)


class Authentication:

    @staticmethod
    def user(
        encoded_token: HTTPAuthorizationCredentials = Depends(bearer_header),
    ) -> User:
        pass

    @staticmethod
    def admin(
        encoded_token: HTTPAuthorizationCredentials = Depends(bearer_header),
    ) -> User:
        pass

    @staticmethod
    def api(api_key: str = Depends(api_header)) -> User:
        pass

    @staticmethod
    def authenticate(
        api_key: str | None = Depends(api_header),
        encoded_token: HTTPAuthorizationCredentials | None = Depends(bearer_header),
    ) -> User:
        pass

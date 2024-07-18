from fastapi import APIRouter
from redis import Redis
from .routes import AuthRoutes


class FastAuth:

    def __init__(
        self,
        database: Redis = Redis(),
        router: APIRouter = APIRouter(prefix="/auth", tags=["authentication"]),
        enable_signup: bool = True,
    ):
        self._DATABASE = database
        self._ROUTER = router
        self._ENABLE_SIGNUP = enable_signup

        AuthRoutes(self._DATABASE, self._ROUTER, self._ENABLE_SIGNUP)

    def getDatabase(self) -> Redis:
        return self._DATABASE

    def getRouter(self) -> APIRouter:
        return self._ROUTER

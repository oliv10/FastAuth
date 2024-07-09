from fastapi import APIRouter
from redis import Redis
from .routes import AuthRoutes


class FastAuth:

    def __init__(
        self,
        database=Redis(),
        router=APIRouter(prefix="/auth", tags=["authentication"]),
    ):
        self._DATABASE = database
        self._ROUTER = router

        AuthRoutes(self._DATABASE, self._ROUTER)

    def getDatabase(self) -> Redis:
        return self._DATABASE

    def getRouter(self) -> APIRouter:
        return self._ROUTER

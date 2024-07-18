import fastauth
from uuid import UUID
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, Body
from fastauth.models import User, PasswordReset
from typing import List
from fastapi.exceptions import HTTPException

from fastauth.authentication import Authentication


def AuthRoutes(database: fastauth._Redis, router: fastauth._APIRouter):

    @router.get("/user/{userID}", response_model=UUID)
    async def get_user(userID: UUID):
        return userID

    @router.post("/login")
    async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
        pass

    @router.get("/validate", response_model=bool)
    async def validate_token():
        return True

    @router.get("/me", response_model=User)
    async def get_me():
        return None

    @router.post("/signup", response_model=User)
    async def signup(username: str = Body(), password: str = Body()):
        pass

    @router.get("/users", response_model=List[User])
    async def get_users():
        pass

    @router.delete("/user/{username}", response_model=User)
    async def delete_user(username: str):
        pass

    @router.post("/user/{username}", response_model=User)
    async def update_user(username: str):
        pass

    @router.post("/reset/me", response_model=User)
    async def reset_current_user_password(reset_form: PasswordReset):
        if reset_form.new_password != reset_form.new_password_confirm:
            raise HTTPException(500, "New passwords do not match.")
        pass

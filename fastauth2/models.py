from dataclasses import dataclass
from typing import Literal, List


@dataclass
class BASE_USER_ROLES:
    ADMIN: str = "admin"
    USER: str = "user"


# TODO: buildout model with greater typcasting controls
@dataclass
class User:
    # OpenID Connect Core 1.0, Section 5.1
    sub: str
    name: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    middle_name: str | None = None
    nickname: str | None = None
    preferred_username: str | None = None
    profile: str | None = None
    picture: str | None = None
    website: str | None = None
    email: str | None = None
    email_verified: bool | None = None
    gender: Literal["male", "female"] | None = None
    birthdate: str | None = None
    zoneinfo: str | None = None
    locale: str | None = None
    phone_number: str | None = None
    phone_number_verified: bool | None = None
    address: str | None = None
    update_at: int | None = None

    # RFC7643, Section 4.1.2
    groups: List[str] | None = None
    roles: List[str] | None = None
    entitlement: List[str] | None = None

    def dict(self):
        return self.__dict__


@dataclass
class DatabaseUser(User):
    password_hash: str = None

    def User(self) -> User:
        userDict = self.dict()
        UserKeys = set(User.__dataclass_fields__.keys())
        DatabaseUserKeys = set(DatabaseUser.__dataclass_fields__.keys())
        uniqueKeys = DatabaseUserKeys.difference(UserKeys)
        for key in uniqueKeys:
            userDict.pop(key, None)
        return User(**userDict)


@dataclass
class JWTToken:
    # RFC7519, Section 4.1
    iss: str | None = None
    sub: str | None = None
    aud: str | None = None
    exp: int | None = None
    nbf: int | None = None
    iat: int | None = None
    jti: str | None = None

    def dict(self):
        return self.__dict__


@dataclass
class PasswordReset:
    current_password: str
    new_password: str
    new_password_confirm: str

from pydantic import BaseModel, EmailStr, ConfigDict

class UserBase(BaseModel):
    email:EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class AccountBase(BaseModel):
    account_number: str


class AccountCreate(AccountBase):
    balance: float = 0.0


class AccountResponse(AccountBase):
    id: int
    balance: float

    owner_id: int

    model_config = ConfigDict(from_attributes=True)

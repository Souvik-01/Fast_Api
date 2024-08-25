from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    # Optional fields with default values
    id: int
    created_at: date
    photo: str
    updated_at: date

class Credentials(BaseModel):
    email:EmailStr
    password:str
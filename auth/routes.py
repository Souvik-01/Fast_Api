from fastapi import APIRouter, status, Depends, Header
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from users.schemas import Credentials
from core.database import get_db
from auth.services import get_token, get_refresh_token

router = APIRouter(
    prefix="/login",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)

@router.post("", status_code=status.HTTP_200_OK)
async def authenticate_user(data: Credentials, db: Session = Depends(get_db)):
    print(data,"prinnghte data")
    return await get_token(data=data, db=db)

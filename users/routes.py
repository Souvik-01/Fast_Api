from fastapi import APIRouter, status, Depends, Request,UploadFile,File
from sqlalchemy.orm import Session
from core.database import get_db
from users.schemas import CreateUserRequest
from users.services import create_user_account, get_user_details,upload_photo
from fastapi.responses import JSONResponse

ImageDir="images/"


router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequest, db: Session = Depends(get_db)):
    await create_user_account(data=data, db=db)
    payload = {"message": "User account has been succesfully created."}
    return JSONResponse(content=payload)
    
@router.get('/get-user', status_code=status.HTTP_200_OK)
async def fetch_user(email:str, db: Session = Depends(get_db)):
   return await get_user_details(email, db=db)

@router.post('/upload-profile-pic', status_code=status.HTTP_200_OK)
async def create_user(email:str,file:UploadFile=File(...), db: Session = Depends(get_db)):
   
   return  await upload_photo(email,file,db)
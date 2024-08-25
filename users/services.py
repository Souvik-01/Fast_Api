from users.model import UserModel
from fastapi.exceptions import HTTPException
from core.security import get_password_hash
from datetime import datetime
import os



async def create_user_account(data, db):
    user = db.query(UserModel).filter(UserModel.email == data.email).first()
    if user:
        raise HTTPException(status_code=422, detail="Email is already registered with us.")

    new_user = UserModel(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        password=get_password_hash(data.password),
        created_at=datetime.now(),

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def get_user_details(email,db):
    user = db.query(UserModel).filter(UserModel.email == email).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="No user found with this email")
    
    return {user}



async def upload_photo(email: str, file, db):
    ImageDir = "images/"
    user = db.query(UserModel).filter(UserModel.email == email).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="No user found with this email")
    if not os.path.exists(ImageDir):
        os.makedirs(ImageDir)
    file_path = os.path.join(ImageDir, file.filename)
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)
    user.photo = file_path
    
    db.commit() 
    db.refresh(user) 
    
    return {"message": "Photo uploaded successfully", "photo_path": file_path}
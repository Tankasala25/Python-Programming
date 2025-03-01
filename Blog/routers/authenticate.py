from fastapi import APIRouter,Depends,HTTPException,status
from .. import models,schemas,database
from sqlalchemy.orm import Session
from .. hashing import Hash

router = APIRouter(
    tags=['Authentication']
)

@router.post("/login")
def login(request:schemas.login,db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="Invalid Username")
    print(f"Plain password: {request.password}")
    print(f"Stored hashed password: {user.password}")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Password")
    #we are going to generate JWT token if everything was correct  
    return user
from fastapi import APIRouter,HTTPException,status,Depends,Response
from typing import List
from .. import models,schemas
from .. database import get_db
from .. hashing import Hash
from sqlalchemy.orm import Session
from ..repository import user

router=APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post("/",status_code = status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create(request:schemas.User,db:Session=Depends(get_db)):
    return user.create(request,db)


@router.get("/{id}",response_model=schemas.ShowUser)
def showUser(id,db:Session=Depends(get_db)):
    return user.get_userby_id(id,db)

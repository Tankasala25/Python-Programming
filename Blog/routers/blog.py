from fastapi import APIRouter,HTTPException,status,Depends,Response
from typing import List
from .. import models,schemas
from .. database import get_db
from sqlalchemy.orm import Session
from ..repository import blog

router=APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.ShowBlog])
def get_blog(db:Session=Depends(get_db)):
    return blog.get_all(db)


@router.post("/",status_code = status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(get_db)):
    return blog.create(request,db)

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def getblogby_id(id,response:Response,db:Session=Depends(get_db)):
    return blog.get_blogby_id(id,db)

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def updateblog(id,request:schemas.Blog,db:Session=Depends(get_db)):
    return blog.update(id,request,db)

@router.delete("/{id}")
def deleteblog(id,db:Session=Depends(get_db)):
    return blog.delete(id,db)
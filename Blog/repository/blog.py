from .. import models,schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException,status


def get_all(db:Session):
    all=db.query(models.Blog).all()
    return all

def create(request:schemas.Blog,db:Session):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blogby_id(id,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} is not available'}
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    return blog


def update(id,request:schemas.Blog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.update(request.model_dump())
    db.commit()
    return "Blog updated Sucessfully"

def delete(id,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    db.delete(blog)
    db.commit()
    return 'Blog Deleted Successfully'
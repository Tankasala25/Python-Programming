from fastapi import FastAPI,Depends,HTTPException,status,Response
from . import schemas,models
from .database import engine,Base,SessionLocal
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash


app=FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/blog",status_code = status.HTTP_201_CREATED,tags=['Blogs'])
def create(request:schemas.Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog",status_code=status.HTTP_200_OK,response_model=List[schemas.ShowBlog],tags=['Blogs'])
def get_blog(db:Session=Depends(get_db)):
    all=db.query(models.Blog).all()
    return all

@app.get("/blog/{id}",status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog,tags=['Blogs'])
def getblogby_id(id,response:Response,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} is not available'}
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    return blog

@app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED,tags=['Blogs'])
def updateblog(id,request:schemas.Blog,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.update(request.model_dump())
    db.commit()
    return "Blog updated Sucessfully"

@app.delete("/blog/{id}",tags=['Blogs'])
def deleteblog(id,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    db.delete(blog)
    db.commit()
    return 'Blog Deleted Successfully'


@app.post("/user",status_code = status.HTTP_201_CREATED,tags=['Users'],response_model=schemas.ShowUser)
def create(request:schemas.User,db:Session=Depends(get_db)):
    new_user=models.User(name=request.name,email=request.email,password=Hash.bycrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/user/{id}",tags=['Users'],response_model=schemas.ShowUser)
def showUser(id,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"User with id {id} was not found.")
    return user

from fastapi import FastAPI,Depends,HTTPException,status,Response
from . import schemas,models
from .database import engine,Base,get_db
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash
from .routers import blog,user,authenticate

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authenticate.router)
app.include_router(blog.router)
app.include_router(user.router)



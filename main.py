from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()

@app.get("/blog")
def index(limit=10,published:bool=True,sort:Optional[str]=None):

    if published:
        return {"data":f"{limit} blogs from published list"}
    else:
        return {"data":f"{limit} blogs from list"}

class Blog(BaseModel):
        title:str
        body:str
        published:Optional[bool]

    


@app.post("/create/blog")
def create(request:Blog):
    return f"Blog Created with {request.title}"


@app.get("/blog/unpublished")
def unpublished():
    return {"data":"Unpublished Data"}

@app.get("/blog/{id}")
def showBlog(id:int):
    return {"data":id}




@app.get("/about")
def about():
    return {"about:about page"}



# if __name__=="__main__":
#      uvicorn.run(app,host="127.0.0.1",port=9000)
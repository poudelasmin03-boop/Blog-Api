from fastapi import FastAPI,APIRouter,Form,HTTPException,File,Depends,UploadFile
from models.blog import Blog
from database.db import engine,get_db
import os
from fastapi.staticfiles import StaticFiles 
import shutil

from sqlalchemy.orm import Session

folder =  "blog/"
os.makedirs(folder,exist_ok=True)



router = APIRouter(
  prefix="/blog",
  tags=["blog"]
)


@router.get("/")
async def get_all(db:Session=Depends(get_db)):
    blog = db.query(Blog).all()
    return{
        "blog":blog
    }




@router.post("/")
async def create_blog(
    title:str=Form(...),
    description:str=Form(...),
    content:UploadFile=File(...),
    db:Session=Depends(get_db)
):

    file_path = os.path.join(folder,content.filename)

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(content.file,buffer)


    new_post = Blog(
        title = title,
        description = description,
        content = file_path
    )    

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return{
        "message":"Successfully added"
    }






 ####3 DDELETE BLOG
@router.delete("/delete/{blog_id}")
async def delete(
    blog_id:int,
    db:Session=Depends(get_db)
) :
    blog  =  db.query(Blog).filter(Blog.blog_id==blog_id).first()
    if not blog:
        raise HTTPException(
            status_code=401,
            detail = "Not found"
        )  


    db.delete(blog)
    db.commit()

    return{
        "message":"Successfully deleted.."
    }




######Update the status...
@router.put("/update/{blog_id}")
async def update_post(
    blog_id:int,
    title:str=Form(...),
    content:UploadFile=File(...),
    description:str=Form(...),
    db:Session=Depends(get_db)
  ):
      blog  =  db.query(Blog).filter(Blog.blog_id==blog_id).first()
      if not blog:
          raise HTTPException(
              status_code=401,
              detail = "Not found"
          )    

      blog.title = title
      blog.description = description

      file_path = os.path.join(folder,content.filename)
      
      with open(file_path,"wb") as buffer:
              shutil.copyfileobj(content.file,buffer)

      blog.content = file_path 

      db.commit()
      db.refresh(blog)      


      return{
           "message":"Update succesfully post"
      } 
      

    
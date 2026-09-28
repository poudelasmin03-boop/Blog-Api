from fastapi import FastAPI,APIRouter
from fastapi.staticfiles import StaticFiles
from router.blog import router as  blogrouter


app = FastAPI()



app.include_router(blogrouter)


@app.get("/")
async def home_views():
  return{
    "message":"Welcome to our views..."
  }

folder = "blog"
app.mount("/files",StaticFiles(directory="blog"),name="file")



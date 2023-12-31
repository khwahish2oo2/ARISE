
from fastapi import FastAPI, Request, Form, HTTPException,UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from long_format import output
from tabular import output_table
from utils import extract_text_func

from firebase_admin import auth, db, initialize_app, credentials


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")
# cred = credentials.Certificate("login-database-a039a-firebase-adminsdk-nl21h-077c59e4c6.json")
# firebase_app = initialize_app(cred, {"databaseURL": "https://login-database-a039a-default-rtdb.firebaseio.com"})


@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
   return templates.TemplateResponse("index.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
   return templates.TemplateResponse("login.html", {"request": request})


@app.get("/reset_password", response_class=HTMLResponse)
async def reset_password(request: Request):
   return templates.TemplateResponse("reset_password.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
   return templates.TemplateResponse("register.html", {"request": request})

@app.get("/OurServices", response_class=HTMLResponse)
async def OurServices(request: Request):
   return templates.TemplateResponse("home-entrepreneur.html", {"request": request})

@app.get("/YourProfile", response_class=HTMLResponse)
async def YourProfile(request: Request):
   return templates.TemplateResponse("profile.html", {"request": request})

@app.get("/Upload", response_class=HTMLResponse)
async def Upload(request: Request):
   return templates.TemplateResponse("Upload_doc.html", {"request": request})

@app.get("/Upload_Table", response_class=HTMLResponse)
async def Upload_Table(request: Request):
   return templates.TemplateResponse("Upload_doc_table.html",{"request":request})

@app.get("/question", response_class=HTMLResponse)
async def question(request: Request):
   return templates.TemplateResponse("question.html", {"request": request})

@app.post("/uploadfile")
async def uploadFile(file: UploadFile = File(...), question: str = Form(...)):
   document = extract_text_func(file)
   value = await output(document,question)
   return {"output": value}

@app.post("/uploadfiletable")
async def uploadFileTable(file: UploadFile = File(...), question: str = Form(...)):
   answer = output_table()
   return {"output": answer}
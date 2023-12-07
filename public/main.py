
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from firebase_admin import auth, db, initialize_app, credentials


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")
cred = credentials.Certificate("login-database-a039a-firebase-adminsdk-nl21h-077c59e4c6.json")
firebase_app = initialize_app(cred, {"databaseURL": "https://login-database-a039a-default-rtdb.firebaseio.com"})

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


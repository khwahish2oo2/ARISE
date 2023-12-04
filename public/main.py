# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def index():
#    return {"message": "Hello World"}

# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi import FastAPI, Request
# app = FastAPI()
# templates = Jinja2Templates(directory="Templates")
# @app.get("/", response_class=HTMLResponse)
# async def hello(request: Request):
#    return templates.TemplateResponse("index.html", {"request": request})

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

@app.post("/login")
async def login(
    email: str = Form(...),
    password: str = Form(...),
):
    try:
        
        user = auth.get_user_by_email(email)

        # Verify the password (optional, Firebase does this by default)
        # If you want additional password verification, you can use:
        # auth.verify_password_hash(password, user.password_hash)

        return JSONResponse(content={"message": "Login successful"}, status_code=200)

    except auth.AuthError as e:
        raise HTTPException(status_code=401, detail=f"Login failed: {e}")

@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
   return templates.TemplateResponse("register.html", {"request": request})

# @app.post("/submit/")
# async def submit(
#     request: Request,
#     Email: str = Form(...),
#     Password: str = Form(...),
#     full_name: str = Form(...),
#     first_school: str = Form(...),
# ):
#     try:
#         # Create user in Firebase Authentication
#         user = auth.create_user(
#             email=Email,
#             password=Password,
#         )

#         # Store additional user information in Firebase Realtime Database
#         user_data = {
#             "fullName": full_name,
#             "firstSchool": first_school,
#         }
#         db.reference(f"UsersAuthList/{user.uid}").set(user_data)

#         return templates.TemplateResponse("login.html", {"request": request})

#     except auth.AuthError as e:
#         raise HTTPException(status_code=400, detail=f"Registration failed: {e}")
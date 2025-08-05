from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.spotify_utils import get_auth_url, get_token

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/authorize")
def authorize(client_id: str = Form(...), client_secret: str = Form(...)):
    response = RedirectResponse(url=get_auth_url(client_id), status_code=302)
    response.set_cookie("client_id", client_id)
    response.set_cookie("client_secret", client_secret)
    return response

@app.get("/callback")
def callback(request: Request, code: str):
    client_id = request.cookies.get("client_id")
    client_secret = request.cookies.get("client_secret")
    token_data = get_token(code, client_id, client_secret)
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "token": token_data

from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

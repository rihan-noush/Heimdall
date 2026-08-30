import ageCheck
import analyzer
import databaseCrossCheck
import qrcodeReader
import textExtractor
import textSplitter

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 1. Mount the 'static' folder for your CSS, JS, and Images
app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. Point FastAPI to your 'templates' folder for HTML
templates = Jinja2Templates(directory="templates")

# 3. Serve your index.html file at the home URL
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
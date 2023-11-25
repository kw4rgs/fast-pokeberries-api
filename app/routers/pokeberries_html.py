from fastapi import FastAPI, Request, APIRouter, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="app/templates")

router = APIRouter(tags=["Get all berry stats"], responses={404: {"description": "Not found"}})

@router.get("/berry-histogram", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
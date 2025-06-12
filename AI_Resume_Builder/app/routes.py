from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .models import ResumeRequest
from .llm_chain import chain

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Welcome to the FastAPI App!</h1>"
    
@router.post("/generate_resume/", response_class=HTMLResponse)
async def generate_resume(req: ResumeRequest, request: Request):
    output = chain.invoke({
        "name": req.name,
        "role": req.role,
        "skills": ", ".join(req.skills),
        "experience": req.experience
    })

    # Simple splitting logic
    summary, *bullets = output.strip().split("\n")
    bullet_points = [b.lstrip("-• ") for b in bullets if b.strip()]

    return templates.TemplateResponse("resume.html", {
        "request": request,
        "name": req.name,
        "role": req.role,
        "summary": summary,
        "experience": bullet_points
    })

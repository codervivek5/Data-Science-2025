from fastapi import FastAPI
from .routes import router

app = FastAPI(title="GenAI Resume Generator")
app.include_router(router)

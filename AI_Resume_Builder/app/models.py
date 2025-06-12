from pydantic import BaseModel
from typing import List

class ResumeRequest(BaseModel):
    name: str
    role: str
    skills: List[str]
    experience: int

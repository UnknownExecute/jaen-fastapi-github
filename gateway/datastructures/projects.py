from pydantic import BaseModel


class ProjectForm(BaseModel):
    pat: str
    remote: str


class ProjectResponse(BaseModel):
    id: int
    pat: str
    remote: str
    created_by: int
    created_at: str
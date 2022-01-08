from typing import List

from fastapi import FastAPI, Header, status, APIRouter
from tortoise.contrib.fastapi import register_tortoise

from models import Project_Pydantic, ProjectIn_Pydantic, Projects


app = FastAPI()

router = APIRouter(prefix="/api/jaen")


@router.get('/projects', response_model=List[Project_Pydantic])
async def get_projects(request_user_id: str = Header(None)):
    return await Project_Pydantic.from_queryset(
        Projects.filter(created_by=request_user_id)
    )

app.include_router(router)


register_tortoise(
    app,
    db_url='sqlite://:memory:',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

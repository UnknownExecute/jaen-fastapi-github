from pydantic import BaseModel

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Projects(models.Model):
    id = fields.IntField(pk=True)
    pat = fields.TextField()
    remote = fields.TextField()
    created_by = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)


Project_Pydantic = pydantic_model_creator(Projects, name='Project')


class ProjectIn_Pydantic(BaseModel):
    pat: str
    remote: str
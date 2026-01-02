from typing import Optional
from pydantic import BaseModel


class ModulesIn(BaseModel):
    target_modules: list[str]


class SkillOut(BaseModel):
    id: str
    name: str


class ModuleOut(BaseModel):
    id: str
    name: str
    skills: Optional[list[SkillOut]]


class ModulePath(BaseModel):
    path: list[ModuleOut]

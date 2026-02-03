from typing import Optional
from pydantic import BaseModel, Field


class ModulesIn(BaseModel):
    target_modules: list[str]


class UserPromt(BaseModel):
    message: str


class CreateRoadmapSchema(BaseModel):
    target_skills: list[Optional[str]]
    known_skills: list[Optional[str]] = Field([])


class SkillOut(BaseModel):
    id: str
    name: str


class ModuleOut(BaseModel):
    id: str
    name: str
    skills: Optional[list[SkillOut]]


class Link(BaseModel):
    url: str
    title: str


class ModuleDetails(ModuleOut):
    level: str | None
    description: str | None
    links: list[Link | None]


class ModulePath(BaseModel):
    path: list[ModuleOut]


class UserPath(BaseModel):
    complited: int
    lenght: int
    current_module: str
    path: list[ModuleOut]

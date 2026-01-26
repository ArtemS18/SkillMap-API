from httpx import AsyncClient
from unittest.mock import AsyncMock, MagicMock
import pytest

from app.schemas import skill_schema
from app.server.server import app


@pytest.mark.asyncio
async def test_create_path_ok(async_client: AsyncClient, monkeypatch):
    from tortoise.queryset import QuerySet
    from app.service import roadmap
    from app.depends import get_current_user_id
    from app.service.progress import create_user_path
    from tests.test_server.utils import get_fake_roadmap

    app.dependency_overrides[get_current_user_id] = lambda: 123
    fake_target_skills = {
        "target_skills": ["functions_basics"],
        "known_skills": ["python_syntax_types"],
    }
    monkeypatch.setattr(roadmap, "get_roadmap", get_fake_roadmap)

    async def fake_get_or_none(*args, **kwargs):
        return MagicMock(have_active_path=False, id=123, name="test")

    monkeypatch.setattr(QuerySet, "get_or_none", fake_get_or_none)
    await create_user_path(
        1, skill_schema.CreateRoadmapSchema.model_validate(fake_target_skills)
    )

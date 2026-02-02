from app.pydantic_schemas import skill_schema, user_schema
from unittest.mock import MagicMock, Mock, AsyncMock


def create_user():
    return user_schema.CreateUser(
        email="test_user@email.com",
        password="test",
        firstname="test_firstname",
        lastname="test_lastname",
    )


async def get_fake_roadmap():
    return skill_schema.ModulePath(
        path=[
            skill_schema.ModuleOut(id="test_module1", name="Test Module", skills=[]),
            skill_schema.ModuleOut(
                id="test_module2",
                name="Test Module",
                skills=[skill_schema.SkillOut(id="sk1", name="Test Skill")],
            ),
        ]
    )


def get_fake_redis(val):
    redis_mock = Mock()
    redis_mock.get = AsyncMock(return_value=val)
    return redis_mock

from app.schemas import skill_schema, user_schema


def create_user():
    return user_schema.CreateUser(
        email="test",
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

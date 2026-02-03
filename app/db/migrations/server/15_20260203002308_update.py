from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "resources" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "url" VARCHAR(256) NOT NULL,
    "title" VARCHAR(128) NOT NULL
);
        CREATE TABLE "resources_modules_info" (
    "resource_id" INT NOT NULL REFERENCES "resources" ("id") ON DELETE CASCADE,
    "module_code" VARCHAR(128) NOT NULL REFERENCES "modules_info" ("code") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "resources_modules_info";
        DROP TABLE IF EXISTS "resources_modules_info";
        DROP TABLE IF EXISTS "resources";"""


MODELS_STATE = (
    "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"
    "k7St5R8o6Sd6qzTGss7zz/AVvHwnM="
)

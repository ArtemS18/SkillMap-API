from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "modules_info" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "code" VARCHAR(128) NOT NULL UNIQUE,
    "description" TEXT NOT NULL,
    "level" VARCHAR(32) NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "modules_info";"""


MODELS_STATE = (
    "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"
)

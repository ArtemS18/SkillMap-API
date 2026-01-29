from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "refresh_tokens" (
    "id" VARCHAR(257) NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "is_banned" BOOL NOT NULL DEFAULT False,
    "expire_at" TIMESTAMPTZ,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_refresh_tok_user_id_4c0a06" UNIQUE ("user_id", "id")
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "refresh_tokens";"""


MODELS_STATE = (
    "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"
)

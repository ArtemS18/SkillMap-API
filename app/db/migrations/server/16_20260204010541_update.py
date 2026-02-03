from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "resources_modules_info";
        CREATE TABLE IF NOT EXISTS "resources_modules_info" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "module_code" VARCHAR(64) NOT NULL,
    "resource_id" INT NOT NULL REFERENCES "resources" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_resources_m_resourc_cc9938" UNIQUE ("resource_id", "module_code")
);
        ALTER TABLE "user" ADD "external_id" VARCHAR(255) UNIQUE;
        ALTER TABLE "user" RENAME COLUMN "lastname" TO "name";
        ALTER TABLE "user" DROP COLUMN "firstname";
        ALTER TABLE "user" ALTER COLUMN "provider" SET DEFAULT 1;
        ALTER TABLE "user" ALTER COLUMN "provider" TYPE SMALLINT USING "provider"::SMALLINT;
        COMMENT ON COLUMN "user"."provider" IS 'email: 1
google: 2';
        ALTER TABLE "user" ALTER COLUMN "hashed_password" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "uid_user_externa_2a025a";
        ALTER TABLE "user" RENAME COLUMN "name" TO "lastname";
        ALTER TABLE "user" ADD "firstname" VARCHAR(128) NOT NULL;
        ALTER TABLE "user" DROP COLUMN "external_id";
        ALTER TABLE "user" ALTER COLUMN "provider" TYPE VARCHAR(128) USING "provider"::VARCHAR(128);
        ALTER TABLE "user" ALTER COLUMN "provider" DROP DEFAULT;
        COMMENT ON COLUMN "user"."provider" IS NULL;
        ALTER TABLE "user" ALTER COLUMN "hashed_password" SET NOT NULL;
        DROP TABLE IF EXISTS "resources_modules_info";
        CREATE TABLE "resources_modules_info" (
    "resource_id" INT NOT NULL REFERENCES "resources" ("id") ON DELETE CASCADE,
    "module_id" INT NOT NULL REFERENCES "modules_info" ("id") ON DELETE CASCADE
);"""


MODELS_STATE = (
    "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"
    "o7Ut6R8o6Ud8ozTSss7yz+B7lg9A8="
)

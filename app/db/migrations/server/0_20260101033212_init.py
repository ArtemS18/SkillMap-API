from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "progress" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "current_module" VARCHAR(128),
    "module_skill_learned" SMALLINT NOT NULL,
    "module_progress" DOUBLE PRECISION NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "provider" VARCHAR(128),
    "email" VARCHAR(128) NOT NULL UNIQUE,
    "firstname" VARCHAR(128) NOT NULL,
    "lastname" VARCHAR(128) NOT NULL,
    "hashed_password" VARCHAR(128) NOT NULL,
    "email_verified" BOOL NOT NULL DEFAULT False,
    "progress_id" INT NOT NULL UNIQUE REFERENCES "progress" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmetP2zAQwP+Vqp9A2ibIeIlvaem0Ti1FbdkmEIrcxG0tHDvYzgCh/u+znfdzLaNbkf"
    "IFkfOdfffz487uS5tD9guyTyZkyF62z1svbQJcKP/JtXxotYHnJXIlEGCGtSpIdGZcMGAL"
    "KZ0DzKEUOZDbDHkCUSKlxMdYCaktFRFZJCKfoAcfWoIuoFjKAc5bt3dSjIgDnyCPPr17a4"
    "4gdjKuIkeNreWWePa0rE/EF62oRptZNsW+SxJl71ksKYm1ERFKuoAEMiCg6l4wX7mvvAvj"
    "jCIKPE1UAhdTNg6cAx+LVLhrMrApUfykN1wHuFCjfDQOj06Pzj6fHJ1JFe1JLDldBeElsQ"
    "eGmsDltL3S7UCAQENjTLjJeeTKpQK87hKwcnopkxxC6XgeYQSsjmEkSCAmC+eNKLrgycKQ"
    "LIRa4MbxcQ2z7+a4+9Uc70mtfRUNlYs5WOOXYZMRtCmwCUi1NTaAGKq/T4CHBwdrAJRalQ"
    "B1WxagHFHAYA9mIX6bjC7LIaZMciCviQzw1kG2+NDCiIu73cRaQ1FFrZx2OX/AaXh7Q/Nn"
    "nmt3MOpoCpSLBdO96A46krE6Muf3qc2vBDNg3z8C5liFFmrQKt1ik2u4eQkgYKFZqYhVfG"
    "ESuWJUecbLEkzcVptivLRWk2TeUZKxGVTBWqBkd1/IFoFcWLHDM5Y5mE5o+in6Z41NHpL7"
    "l0enDMEZEfwcjl5Dctof9iZTc3iV2fgX5rSnWgwtfc5J905yh0HcSetHf/q1pT5bN6PLXv"
    "58iPWmN23lE/AFtQh9tICTWmKRNAKTObJ9z3nlvGYtm3n9n/MaOp/arj5jMq1aLnV8DDep"
    "aoqWrypw/sNkZusb42yd+sY4q65vVFu2vgmYWPweYSyHAozAknQycQHGlTmlqo8/Z5ndqH"
    "fCRPPZOD2Jc4z6qEsvk6E5GEQ5poAzXRRkSX7BFNRjTNvmCM6V8W4yrEF1MbruDHqtq3Gv"
    "25/0w/oxPlh0oxJJARI6zHHPHGyxRExlCh4Uc9kp6oRmIwKnVP4ZQwxExdUyqBSvw3527g"
    "BZRWsskkYH64Zlsg6wpESOAq8ujyPETWnclMZNCdWUxs28bqE0liXDL+SU5bLqojht05TD"
    "EUnoAoQ3wRgbvM2b6dYTx/YRzhHjQn9sgDFj9E6fn7cBE4PNWaZtGpQxyiXgS5nAPMD5I2"
    "UlhWE10RLTBmz2zLRk4Y9kpyVcO5RiCEjN+ZkxzpGdSettod30JrL+nbczGg0ytUOnP80h"
    "vR52epL1fvbuW3xSiN4DrI0uMzmrt3mKeQ/Xmr96NShSLyKPngU09770HxC79Kwt/oq0a7"
    "yrngekmIHH+D6dX0wySAdiGCzYrjnpmhe99upvf5Rb/QZHYOfP"
)

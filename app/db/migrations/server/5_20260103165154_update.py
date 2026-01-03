from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user_module_progress" ADD "complite_percent" DOUBLE PRECISION NOT NULL DEFAULT 0;
        ALTER TABLE "userpath" ADD "current_module_path_id" INT;
        ALTER TABLE "userpath" ALTER COLUMN "status_id" SET DEFAULT 2;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "userpath" DROP COLUMN "current_module_path_id";
        ALTER TABLE "userpath" ALTER COLUMN "status_id" SET DEFAULT 1;
        ALTER TABLE "user_module_progress" DROP COLUMN "complite_percent";"""


MODELS_STATE = (
    "eJztm1tv4jgUgP8KylNHmh216YVq3sKlO+xAqbjsrKaqIpMYiJrEmcRpQVX/+9rO1bkNoa"
    "TANE+UYx/H/myfG+mL4ED7CdpfJGhrylL42ngRTGBA8kei5XNDAJYVyakAg5nOuoKoz8zB"
    "NlAwkc6B7kAiUqGj2JqFNWQSqenqOhUihXTUzEUkck3tlwtljBYQL8kDvjbuH4hYM1W4gk"
    "7w1XqU5xrUVW6qmkqfzeQyXltM1jPxDetInzaTFaS7hhl1ttZ4icywt2ZiKl1AE9oAQzo8"
    "tl06fTo7f53BiryZRl28KcZ0VDgHro5jy92QgYJMyo/MxmELXNCn/CWeXTQvrs+vLq5JFz"
    "aTUNJ89ZYXrd1TZARuJ8IrawcYeD0Yxogb2UeHTikFr70Edja9mEoCIZl4EmEArIhhIIgg"
    "RgdnRxQNsJJ1aC4wPeDi5WUBs3+lUfubNDohvT7R1SBymL0zfus3iV4bBRuBpFejBES/+3"
    "ECPDs93QAg6ZULkLXxAMkTMfTuIA/xn/HwNhtiTCUBcmqSBd6rmoI/N3TNwQ+HibWAIl01"
    "nbThOL/0OLyTgfRfkmu7P2wxCsjBC5uNwgZoEcbUZM4fY5efCmZAeXwGtiqnWpCI8vqmmw"
    "zRSEqACRaMFV0xXZ/vRMYYYNfJci9+S6F7caI+B+NexgbQ9T/Ix5yLzavQvdAvRZ5lPJD6"
    "/d+7F/ZZwiwG/Y/TLp6LG5jFczHXKtKmUhc2Au2SSyMbSHV1KFs2okbAcdLkW/4wN99HUA"
    "c4x41793JKPgdsxDt/wMPcg9fgEAVS/4Zw3oXysQBe7oDJHRnmyEhUadgpkiyzzuSFRt0N"
    "ehyMSf+DrHllGYNiQ7pYGWSEah3SgjUD5oRrnGYCpuqrfgn+2OCK+eTe096TJahDU19HNi"
    "aP5KQ36I4n0uCOi+I60qRLW0QmXSekJ1cJ3xAO0vjRm3xr0K+Nn8PbbjLYC/tNfgp0TsDF"
    "SDbRswzU2BELpAEY3kJa6pb7ymvW+7rPfU05PhIMPGmqZ2g3jcLiOltFYnvYQD5BFa83SV"
    "DF6/wElbbxCSo0gKaXwRgq7CaardxxVI9wrtkOLpsTcErHmRhUAlMH5VnGdWqUIcolcJbE"
    "gVnAcZ6RnREY5hPNUK3B8jZTJoG/RgbN4NpCSIfALLCfnHKC7IxoV4W2bCayeWWvNRz2ud"
    "ih1ZskkE4HrS5hzUiTThr2shM/No+f2ycok8xJIx+Wn5aWAJylXiPesgLjFV/qmkss9Kzr"
    "LRXVWxJHJKf6kj5IxbWYZP1w97WZ+7Dm4z9KQSoUHuqSTV2yqVP7umTzMfc15TfjtjG1r/"
    "mZSEKtqizk+KoOCjIsGuDJFrSVzFcMbnQEctxIlnIC7ZxqVxWhnFYSIHeG01a/27gbddu9"
    "cc9/0yC8AqyRD4xHXamfwOr9Ji+X/2mcU/y9g94VybM3O+jtfyFP/FBbKpCJabwfrP0HNK"
    "kkjGeYcYmRDbWF+R2uGccemREwlUxbyP9CeXj88hILIrbBcxgZx48GWZ4Kdejd1rY0bkud"
    "rpBxX3fALXph58Cu6abYOAPEgRt3J41O90aa9skR3M+LUmHKm5PVBelwcS4XlHOqyN8CY0"
    "QeIdPyZyqBexGitbJuAu0AVxbNKsljQwhRYreS2chszIXGKgLBqfu7x9wTXJGF0O/extQJ"
    "Yp0g1olEnSB+gH3NLKymNzT/Pemc2n79knT4knSSrufXUogLXpmIKx1l6i1eFvmQ6L8img"
    "X/FdFMpd6ubZOkWd6ypJGjXtE7KUdY2eD5sENYKgbKH2CrVHMPRn4nkdHxFjXEN6Orixp1"
    "UeM9/fiHLGq84ZoecVHj9X+f23a9"
)

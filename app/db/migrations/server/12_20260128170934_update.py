from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "uid_userpath_user_id_6037cd";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE UNIQUE INDEX IF NOT EXISTS "uid_userpath_user_id_6037cd" ON "userpath" ("user_id", "path_hash");"""


MODELS_STATE = (
    "eJztW1tv4jgU/iuIp640O2rTq+YtULrDDpSq0N3VVFVkEgNWEycTOy2o6n8f27k6tyEsaW"
    "GaJ5rjcxyfz8fnFvelTaD7BN3PKnSRvmh/ab20MbAg+yM18qnVBo4T0zmBgqkpWEHMMyXU"
    "BTpl1BkwCWQkAxLdRQ5FNmZU7JkmJ9o6Y0R4HpM8jH54UKP2HNIFe8GX1v0DIyNswCUk4a"
    "PzqM0QNA1pqcjg7xZ0ja4cQetjeiUY+dummm6bnoVjZmdFFzaOuBGmnDqHGLqAQj49dT2+"
    "fL66QM9QI3+lMYu/xISMAWfAM2lC3TUx0G3M8WOrIULBOX/Ln8rRyfnJxfHZyQVjESuJKO"
    "evvnqx7r6gQOB60n4V44ACn0PAGOPG9pHwJWXA6y6Am49eQiQFIVt4GsIQsDIMQ0IMYmw4"
    "W0LRAkvNhHhOuYErp6clmP2j3na/qrcHjOsPro3NjNm38etgSPHHOLAxkPxoVAAxYN9PAI"
    "8OD9cAkHEVAijGZADZGyn0z6AM4t/j0XU+iAmRFJB3mCl4byCdfmqZiNCH3YS1BEWuNV+0"
    "RcgPMwnewVD9L41rdzDqCBRsQueumEVM0GEYc5c5e0wcfk6YAv3xGbiGlhmxFbuINztkKV"
    "aaAjCYC6y4xly/IIiMKaAeyQsvwUhpeCExz86El7EFTPM3ijHHyvlZFF74Q1lkGQ/VweDX"
    "4UX8VnCLIf9++sVjZQ23eKwUekU+VOnAxkB77NBolm14JtQc1+ZOgJAs8p1gmqtvt9AEtC"
    "CM++fyjv0OxYw3wYS7uQevoRGF1OCESNGF4+MAutgCJjdsmj1Dok7HziHJc+uCXurUvZBj"
    "Z1z6b+TNa6sYdBdyZTWQk6pdshGKLFiQrkmSKTCNQPRz+McaRyxA7i39PVPBGGFzFfuYIi"
    "Qn/WFvPFGHN1IWd6lOenxEEdRVinpwlooN0SStf/uTry3+2Po+uu6lk72Ib/K9zdcEPGpr"
    "2H7WgJEwsZAaAiN7SMfYcF9lyWZf33NfM4GPJQNPyPAd7bpZWFJmo0zsHTZQLlCVi3UKVO"
    "WiuEDlY3KBCi2AzCowRgLbyWZrDxz1QzhDLqFVawJJaD8Lg1rANEF1LJMyDZQRlAtAFiyA"
    "OYCQZ9vNSQyLEc0RbYCVfabGEn/EJs3BtWPbJgS4xH9Kwilkp0y6LmirViLrd/Y6o9FAyh"
    "06/UkK0rthp8ewFkgzJkT96iTIzZN2+wQ1Vjkh9uMEZWkFgPPEG4g37MD4zZem55JIPZt+"
    "S039lpSJFHRfsoZU3otJ9w+335u5j3o+wat024Dth6Zl07RsmtK+adl8zH3NxM2kb8zsa3"
    "ElkhKrqwrZv66D//FYq/4NVxL8dSTZVlJy9L8jyeafclNfFCtF3ITE24H1/pE3Uy3IGGYB"
    "vLJdiOb4G1wJHPtsRQDruYdW/pS2e/gVZcCM7ILnKIVLmgZTz4Am9Outrjruqpe9ds553Q"
    "Ju8c2SHTum68ImOSAJuHFv0rrsXal3A2aC73OjJ6rNCsqPsG4rLzrCvkOtH4Ff2rFOoixt"
    "cwa4dHiZw6aPlI0rjaUmbJYza3MkStTQuv7qi5tZcMkWzJ/9DWgqlqZiaTLbpmL5APua2+"
    "nLbmjxxd2CZnNzaze6tZtGV+PfmSp9w08K7WUtqJyWxZD4mv55yTX983QtKGBhr6gQlpMi"
    "H6mukS7ne64LMdU2bE0UiO+lWdbSoggBIhTm/BtJoWmmxd7OPA93xzab9k7T3mnaO017Z3"
    "eO6R63d15/Ak6ZWJw="
)

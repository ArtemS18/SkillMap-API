from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "userpath" RENAME COLUMN "current_module_path_id" TO "current_step";
        ALTER TABLE "userpath" ALTER COLUMN "path_len" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "userpath" RENAME COLUMN "current_step" TO "current_module_path_id";
        ALTER TABLE "userpath" ALTER COLUMN "path_len" SET NOT NULL;"""


MODELS_STATE = (
    "eJztm1tz2joQgP8K46ecmbbTOBcyfTOEnNJCyATSnmkm4xG2AE1s2bXkBCaT/15Jvl+LOb"
    "hA4yfCaleWPkm72sV5kQh0nqDzQYEO0hbSp9aLhIEJ2R+plnctCdh2JOcCCqaGUAWRzpRQ"
    "B2iUSWfAIJCJdEg0B9kUWZhJsWsYXGhpTBHheSRyMfrpQpVac0gX7AGfWvcPTIywDpeQBF"
    "/tR3WGoKEnhop0/mwhV+nKFrI+pldCkT9tqmqW4Zo4UrZXdGHhUBthyqVziKEDKOTdU8fl"
    "w+ej8+cZzMgbaaTiDTFmo8MZcA0am+6aDDQLc35sNERMcM6f8l4+Pm2fXpycn14wFTGSUN"
    "J+9aYXzd0zFASuJ9KraAcUeBoCY8SNrSPhQ8rA6y6Ak08vZpJCyAaeRhgAK2MYCCKI0cbZ"
    "EkUTLFUD4jnlG1w+Oyth9k257X5Wbo+Y1j98NhbbzN4ev/abZK+Ng41A8qNRAaKvfpgAjz"
    "9+XAMg0yoEKNqSANkTKfTOYBLil/HoOh9izCQF8g6zCd7rSKPvWgYi9GE/sZZQ5LPmgzYJ"
    "+WnE4R0Nlf/SXLuDUUdQsAidO6IX0UGHMeYuc/YYO/xcMAXa4zNwdDXTYslWkW62yZTNtA"
    "RgMBes+Iz5/PwgMqaAuiQvvPgtpeGFRDp7E17GJjCMvyjGnMjt8zC88C9lkWU8VAaD34cX"
    "8VnBLQb6h+kXT+Q13OKJXOgVeVOlAxuBdtmhUU1Ldw2o2o7FnQAhWfIdv5urr7fQALQgjH"
    "vn8o59DkWPN36H+7kGr8EmCqT+CUlEF87HBnSxBSY3rJsDI1GnY+dI8ty6kJc6dTfQ2BuX"
    "/hd589oyBs2BfLIqyLmqXbIWikxYcF1LWKZg6r7ph+CPNY6YT+5P+ns2BX2EjVXkY4pITv"
    "rD3niiDG8St7hLZdLjLbKQrlLSo/NUbAg7aX3vTz63+NfWj9F1L33ZC/UmPyQ+JuBSS8XW"
    "swr02BYLpAGYpIe09Q3XNWnZrOsu1zUT+Nhl4AnpnqNd9xYWt9noJraDBUwmqPLFOgmqfF"
    "GcoPK2ZIIKTYCMKhhDg+3cZmsPHPUjnCGH0Ko5QcLoMBODWmAaoDrLuE2DMkS5AGTBApgN"
    "CHm2nJyLYTHRHNMGbNJnquzij1inOVw7lmVAgEv8Z8I4RXbKrOtCWzUTWb+y1xmNBom7Q6"
    "c/SSG9G3Z6jLUgzZQQ9bIT/24e37dPUGWZE2Iftp+WVgCcZ94g3rAC4xVfmppL7OrZ1Ftq"
    "qrektkhB9SW7kcprMen64fZrM/dhzcd/lGbpUHpoSjZNyaZJ7ZuSzdtc10zcjPvGzLoWZy"
    "Ips7qykMOrOng/HqvVf8NNGP4+kmzrUnL8vyPJ5j/lpn5RrBRxYxZ/DtbuI28mW0gyzAK8"
    "shyI5vgrXAmOfTYigLXcQ5v8KW3/+BXdgJnYAc/hFS6+Ndj0dGhAL9/qKuOuctmTcs7rFr"
    "hFb5bs2TFdF1vCASXAjXuT1mXvSrkbsC24mzd6wtysIP0I8rbypCOoO9SRaATOiD1C5XW6"
    "TKbxIkVzFWoSV4BLm6c/7LEhhCgDWaqiZ9HnHInUNdh1//bFG1twySbCv3sL02QyTSbT3H"
    "ibTOYNrGtuBTC7oMUv9BYUoZu3ecO3edN0vbiWQVzy237c6CBzRPmsLIZEr++3S17fb6dz"
    "RIGFPaJCWI6bbJTv7MDTbCU8x8Kx6zgQU3XDikWBeU2vnBxe4SLgQyjM+eeSwo2ZNnujm7"
    "Mp+zRln6bs05R99ueYHnDZ5/UXGJJhbQ=="
)

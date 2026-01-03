from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "userpath" ALTER COLUMN "current_step" SET DEFAULT 0;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "userpath" ALTER COLUMN "current_step" DROP DEFAULT;"""


MODELS_STATE = (
    "eJztm1tz2joQgP8K46d0pqeTOBcyfTOEnHIKIRPIOZ1mMh5hC9DEll1LTmAy+e+V5Pu1mI"
    "MDtH4irHZl6ZO0q12cV4lA5xk6nxToIG0hfW69ShiYkP2RavnYkoBtR3IuoGBqCFUQ6UwJ"
    "dYBGmXQGDAKZSIdEc5BNkYWZFLuGwYWWxhQRnkciF6MfLlSpNYd0wR7wufXwyMQI63AJSf"
    "DVflJnCBp6YqhI588WcpWubCHrY3otFPnTpqpmGa6JI2V7RRcWDrURplw6hxg6gELePXVc"
    "Pnw+On+ewYy8kUYq3hBjNjqcAdegsemuyUCzMOfHRkPEBOf8KX/JJ2fts8vTi7NLpiJGEk"
    "rab970orl7hoLAzUR6E+2AAk9DYIy4sXUkfEgZeN0FcPLpxUxSCNnA0wgDYGUMA0EEMdo4"
    "W6JogqVqQDynfIPL5+clzP5V7rpflLsjpvWBz8Zim9nb4zd+k+y1cbARSH40KkD01Q8T4M"
    "nx8RoAmVYhQNGWBMieSKF3BpMQ/xmPbvIhxkxSIO8xm+CDjjT6sWUgQh/3E2sJRT5rPmiT"
    "kB9GHN7RUPmW5todjDqCgkXo3BG9iA46jDF3mbOn2OHnginQnl6Ao6uZFku2inSzTaZspi"
    "UAg7lgxWfM5+cHkTEF1CV54cVvKQ0vJNLZm/AyNoFh/EYx5lRuX4ThhX8piyzjoTIY/Dq8"
    "iM8KbjHQP0y/eCqv4RZP5UKvyJsqHdgItMsOjWpaumtA1XYs7gQIyZLv+N1cf72DBqAFYd"
    "w7l/fscyh6vPU73M81eAs2USD1T0giunA+NqCLLTC5Zd0cGIk6HTtHkufWhbzUqbuBxt64"
    "9N/Im9eWMWgO5JNVQc5V7Yq1UGTCgutawjIFU/dNPwV/rHHEfHLv6e/ZFPQRNlaRjykiOe"
    "kPe+OJMrxN3OKulEmPt8hCukpJjy5SsSHspPVff/Klxb+2vo9ueunLXqg3+S7xMQGXWiq2"
    "XlSgx7ZYIA3AJD2krW+4rknLZl13ua6ZwMcuA89I9xzturewuM1GN7EdLGAyQZUv10lQ5c"
    "viBJW3JRNUaAJkVMEYGmznNlt74Kgf4Qw5hFbNCRJGh5kY1ALTANVZxm0alCHKBSALFsBs"
    "QMiL5eRcDIuJ5pg2YJM+U2UXf8Q6zeHasSwDAlziPxPGKbJTZl0X2qqZyPqVvc5oNEjcHT"
    "r9SQrp/bDTY6wFaaaEqJed+Hfz+L59hirLnBD7sP20tALgPPMG8YYVGK/40tRcYlfPpt5S"
    "U70ltUUKqi/ZjVRei0nXD7dfm3kIaz7+ozRLh9JjU7JpSjZNat+UbP7Mdc3EzbhvzKxrcS"
    "aSMqsrCzm8qoP347Fa/TfchOGvI8m2LiUn/zuSbP5TbuoXxUoRN2bxfrB2H3kz2UKSYRbg"
    "teVANMdf4Upw7LMRAazlHtrkT2n7x6/oBszEDngJr3DxrcGmp0MDevlWVxl3lauelHNet8"
    "AterNkz47putgSDigBbtybtK5618r9gG3B3bzRE+ZmBelHkLeVJx1B3aGORCNwRuwRKq/T"
    "ZTKNVymaq1CTuAJc2jz9YY8NIUQZyFIVPYs+50ikrsGu+7sv3tiCSzYR/t1bmCaTaTKZ5s"
    "bbZDJ/wLrmVgCzC1r8Qm9BEbp5mzd8mzdN14trGcQlv+3HjQ4yR5TPy2JI9Pp+u+T1/XY6"
    "RxRY2CMqhOW4yUb5zg48zVbCcywcu44DMVU3rFgUmNf0ysnhFS4CPoTCnH8uKdyYabN325"
    "zH+7Mzm5pPU/Npaj5NzWd/jukB13zefgKZBF/i"
)

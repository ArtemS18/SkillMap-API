from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "userpath" ALTER COLUMN "path_len" SET NOT NULL;
        ALTER TABLE "userpath" ALTER COLUMN "current_module_code" SET NOT NULL;
        ALTER TABLE "userpath" ALTER COLUMN "current_step" SET NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "userpath" ALTER COLUMN "path_len" DROP NOT NULL;
        ALTER TABLE "userpath" ALTER COLUMN "current_module_code" DROP NOT NULL;
        ALTER TABLE "userpath" ALTER COLUMN "current_step" DROP NOT NULL;"""


MODELS_STATE = (
    "eJztm21v4jgQgP8K4lNP2lu16av2W6D0llsoVaF3p62qyCQGrCZONnZaUNX/vrbz6rwt4U"
    "gL23yijGcc+7E94xnSlzaB7hN0P6vQRfqi/aX10sbAguyPVMunVhs4TiznAgqmplAFsc6U"
    "UBfolElnwCSQiQxIdBc5FNmYSbFnmlxo60wR4Xks8jD64UGN2nNIF+wBX1r3D0yMsAGXkI"
    "RfnUdthqBpSENFBn+2kGt05QhZH9MrocifNtV02/QsHCs7K7qwcaSNMOXSOcTQBRTy7qnr"
    "8eHz0QXzDGfkjzRW8YeYsDHgDHgmTUx3TQa6jTk/NhoiJjjnT/lTOTo5P7k4Pju5YCpiJJ"
    "Hk/NWfXjx331AQuJ60X0U7oMDXEBhjbmwdCR9SBl53Adx8egmTFEI28DTCEFgZw1AQQ4w3"
    "zpYoWmCpmRDPKd/gyulpCbN/1NvuV/X2gGn9wWdjs83s7/HroEnx2zjYGCQ/GhUgBur7Cf"
    "Do8HANgEyrEKBokwGyJ1Lon0EZ4t/j0XU+xIRJCuQdZhO8N5BOP7VMROjDbmItochnzQdt"
    "EfLDTMI7GKr/pbl2B6OOoGATOndFL6KDDmPMXebsMXH4uWAK9Mdn4BpapsVW7CLdbJOlWG"
    "kJwGAuWPEZ8/kFQWRMAfVIXngJWkrDC4l1dia8jC1gmr9RjDlWzs+i8MK/lEWW8VAdDH4d"
    "XsRnBbcY6u+nXzxW1nCLx0qhV+RNlQ5sDNpjh0azbMMzoea4NncChGTJd4Jurr7dQhPQgj"
    "Dun8s79jkUPd4EHe7mGryGmyiUBidEii6cjwPoYgtMblg3e0aiTsfOkeS5dSEvdepeqLEz"
    "Lv038ua1ZQy6C/lkNZBzVbtkLRRZsOC6JlmmYBqB6efwjzWOWEDuLf09m4IxwuYq9jFFJC"
    "f9YW88UYc30i3uUp30eIsipKuU9OAsFRuiTlr/9idfW/xr6/voupe+7EV6k+9tPibgUVvD"
    "9rMGjMQWC6UhGNlDOsaG6ypbNuv6nuuaCXzsMvCEDN/RrnsLS9psdBN7hwWUE1TlYp0EVb"
    "koTlB5m5ygQgsgswrGyGA7t9naA0f9CGfIJbRqTiAZ7WdiUAtME1RnmbRpUEYoF4AsWABz"
    "ACHPtptzMSwmmmPagJV9psYu/oh1msO1Y9smBLjEf0rGKbJTZl0X2qqZyPqVvc5oNJDuDp"
    "3+JIX0btjpMdaCNFNC1M9Ogrt5ct8+QY1lToh9OEFaWgFwnnmDeMMKjF98aWouiatnU2+p"
    "qd6S2iIF1ZfsRiqvxaTrh9uvzdxHNZ/gUbptwPZDU7JpSjZNat+UbD7mumbiZtI3Zta1OB"
    "NJmdWVhexf1cH/8Vir/huuZPjrSLKtS8nR/44km/+Um/pFsVLETVi8Haz3j7yZbEFmmAV4"
    "ZbsQzfE3uBIc+2xEAOu5h1b+KW33+BXdgJnYBc/RFS65Ndj0DGhCP9/qquOuetlr55zXLX"
    "CL3yzZsWO6LjbJAUngxr1J67J3pd4N2BZ8nzd6otysIP0I87bypCOsO9SRaITOiD1C43W6"
    "TKbx0o7nKtTaXAEuHZ7+sMdGEOIMZKmJnkWfcyRS13DX/dUXb2zBJZsI/+4vTJPJNJlMc+"
    "NtMpkPsK65FcDsgha/0FtQhG7e5o3e5k3T9eNaBnHJb/tJo73MEZXTshgSv75/XvL6/nk6"
    "RxRY2CMqhOWkyUfKd6SX9j3XhZhqG5YsCsz3clvWUroIAREKc/69pHBrps3ebnse7s7ebM"
    "o+TdmnKfs0ZZ/dOaZ7XPZ5/QkT+WDD"
)

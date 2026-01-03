from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user_module_progress" DROP COLUMN "complite_percent";
        ALTER TABLE "userpath" ADD "path_len" INT;
        ALTER TABLE "userpath" ALTER COLUMN "status_id" SET DEFAULT 1;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "userpath" DROP COLUMN "path_len";
        ALTER TABLE "userpath" ALTER COLUMN "status_id" SET DEFAULT 2;
        ALTER TABLE "user_module_progress" ADD "complite_percent" DOUBLE PRECISION DEFAULT 0;"""


MODELS_STATE = (
    "eJztmltz2joQgP8K46ecmbbTOBcyfTOEnNJCyATSnmkm4xG2AE1s2bXlBCaT/15Jvsq3Yg"
    "4u0PgpYbUrS5+kXe3aL5ILnSfofFCgg7SF9Kn1ImFgQvpPquVdSwK2HcuZgICpwVVBrDN1"
    "iQM0QqUzYLiQinToag6yCbIwlWLPMJjQ0qgiwvNY5GH004MqseaQLOgDPrXuH6gYYR0uoR"
    "v+tB/VGYKGLgwV6ezZXK6Slc1lfUyuuCJ72lTVLMMzcaxsr8jCwpE2woRJ5xBDBxDIuieO"
    "x4bPRhfMM5yRP9JYxR9iwkaHM+AZJDHdNRloFmb86GhcPsE5e8p7+fi0fXpxcn56QVX4SC"
    "JJ+9WfXjx335ATuJ5Ir7wdEOBrcIwxN7qOLhtSBl53AZx8egmTFEI68DTCEFgZw1AQQ4w3"
    "zpYommCpGhDPCdvg8tlZCbNvym33s3J7RLX+YbOx6Gb29/h10CT7bQxsDJIdjQoQA/XDBH"
    "j88eMaAKlWIUDeJgKkTyTQP4MixC/j0XU+xIRJCuQdphO815FG3rUM5JKH/cRaQpHNmg3a"
    "dN2fRhLe0VD5L821Oxh1OAXLJXOH98I76FDGzGXOHhOHnwmmQHt8Bo6uZlos2SrSzTaZsp"
    "mWAAzmnBWbMZtfEETGBBDPzQsvQUtpeHFjnb0JL2MTGMZfFGNO5PZ5FF7Yj7LIMh4qg8Hv"
    "wwv/W8EthvqH6RdP5DXc4olc6BVZU6UDG4P26KFRTUv3DKjajsWcgOtmyXeCbq6+3kIDkI"
    "Iw7p/LO/p3yHu8CTrczzV4DTdRKA1OiBBdGB8bkMUWmNzQbg6MRJ2OnSHJc+tcXurUvVBj"
    "b1z6X+TNa8sYNAeyyaog56p2SVsIMmHBdU2wTMHUA9MP4T9rHLGA3J/093QK+ggbq9jHFJ"
    "Gc9Ie98UQZ3gi3uEtl0mMtMpeuUtKj81RsiDppfe9PPrfYz9aP0XUvfdmL9CY/JDYm4BFL"
    "xdazCvTEFgulIRjRQ9r6husqWjbrust1zQQ+ehl4QrrvaNe9hSVtNrqJ7WABxQRVvlgnQZ"
    "UvihNU1iYmqNAEyKiCMTLYzm229sBRP8IZclxSNScQjA4zMagFpgGqs0zaNCgjlAvgLmgA"
    "s4HrPltOzsWwmGiOaQNW9Jkqvfgj2mkO145lGRDgEv8pGKfITql1XWirZiLrV/Y6o9FAuD"
    "t0+pMU0rthp0dZc9JUCRE/Ownu5sl9+wRVmjkh+scO0tIKgPPMG8QbVmD84ktTc0lcPZt6"
    "S031ltQWKai+ZDdSeS0mXT/cfm3mPqr5BI/SLB1KD03JpinZNKl9U7J5m+uaiZtJ35hZ1+"
    "JMJGVWVxZyeFUH/+WxWv0drmD4+0iyrUvJ8f+OJJu/yk29UawUcRMWfw7W7iNvJlsQGWYB"
    "XlkORHP8Fa44xz4dEcBa7qEVX6XtH7+iGzAVO+A5usIltwadng4N6OdbXWXcVS57Us553Q"
    "K3+MuSPTum62ITHJAAbtybtC57V8rdgG7B3XzRE+VmBelHmLeVJx1h3aGORCN0RvQRKqvT"
    "ZTKNFymeK1eTmAJc2iz9oY+NIMQZyFLlPfM+54inruGu+7fPv9iCSzoR9ttfmCaTaTKZ5s"
    "bbZDJvYF1zK4DZBS3+oLegCN18zRt9zZum68e1DOKSd/tJo4PMEeWzshgSf77fLvl8v53O"
    "ETkW+ogKYTlp8pbyHeGjfc9xICbqhiWLAvOavjk5vMpFig/fcZWujsUdbLRjdxAbt7xhm1"
    "pQUwtqakFNLWh/jukB14JefwEcYmm8"
)

import logging
from config import settings

LOG_LOVELS = {"INFO": logging.INFO, "DEBUG": logging.DEBUG}
LOG_FORMAT = "[%(asctime)s.%(msecs)03d] %(levelname)s %(module)10s:%(funcName)s:%(lineno)-3d %(message)s"
LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"


def _init_logger():
    logging.basicConfig(
        format=LOG_FORMAT, datefmt=LOG_DATEFMT, level=LOG_LOVELS["INFO"]
    )

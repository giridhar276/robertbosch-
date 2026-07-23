import logging
from logging.handlers import RotatingFileHandler
logger = logging.getLogger("rotating_logger")
handler = RotatingFileHandler("rotating.log", maxBytes=2000, backupCount=3)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
for i in range(5):
    logger.info(f"Log entry {i}")

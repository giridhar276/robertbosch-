import logging
logging.basicConfig(level=logging.ERROR)
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("An error occurred")

import logging
logger = logging.getLogger("my_module")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.debug("Debug from named logger")

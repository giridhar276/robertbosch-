import logging
logging.basicConfig(level=logging.DEBUG)
logging.info("This will show")
logging.disable(logging.CRITICAL)
logging.error("This will NOT show because logging is disabled")

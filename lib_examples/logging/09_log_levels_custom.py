import logging
logger = logging.getLogger("level_check")
logger.setLevel(logging.WARNING)
logger.info("This won't print (below WARNING)")
logger.warning("This will print")
print("Effective level:", logger.getEffectiveLevel())

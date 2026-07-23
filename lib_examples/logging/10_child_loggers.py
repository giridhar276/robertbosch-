import logging
logging.basicConfig(level=logging.INFO)
parent = logging.getLogger("app")
child = logging.getLogger("app.module1")
parent.info("Message from parent logger")
child.info("Message from child logger (inherits parent config)")

import logging
logging.basicConfig(filename="app.log", level=logging.INFO,
                     format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("This message goes to app.log")

import logging
from pathlib import Path

def configure_logging():
    Path("logs").mkdir(exist_ok=True)
    logging.basicConfig(
        filename="logs/automation.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

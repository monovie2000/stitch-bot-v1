# logger

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger("Stitch")

def log_error(e):
    logger.error(str(e))
'''
    constructor file
'''

import os
import sys
import logging

logging_str = "[ %(asctime)s: %(levelname)s: %(module)s:  %(message)s]"

LOG_DIR = "logs"
log_filepath = os.path.join(LOG_DIR, "runningLogs.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnclassifierLogger")

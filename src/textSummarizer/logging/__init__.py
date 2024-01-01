import os
import logging
import sys

log_str = '[%(asctime)s : %(levelname)s : %(module)s : %(message)s]'
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'running_logs.log')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    format = log_str,
    level = logging.INFO,

    handlers=[
        logging.FileHandler(filename= log_filepath),
        logging.StreamHandler(sys.stdout)
    ]

)

logger = logging.getLogger('textSummarizerLogger')

if __name__ == '__main__':
    logger.info('welcome to custom logs')

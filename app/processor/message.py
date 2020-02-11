from time import sleep
from app.utils.logger import get_logger


LOG = get_logger(__name__)


# process message
def process(message):
    # execution time of process
    LOG.info('Processing Message', {'message': message})
    sleep(0.2)
    if ('error' in message):
        raise Exception('Process Custom Error')

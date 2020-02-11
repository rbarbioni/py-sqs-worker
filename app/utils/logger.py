import logging
from time import time
from json import dumps
from socket import gethostname
from sys import stdout
from app.utils.config import get_config


class GraylogFormatter(logging.Formatter):

    def __init__(self):
        logging.Formatter.__init__(self)

    def format(self, record):
        log = {
            'timestamp': time(),
            '_app_version': get_config('APPLICATION_VERSION'),
            '_product': 'namespace',
            '_application': get_config('APPLICATION_NAME'),
            '_environment': get_config('ENV', 'dev'),
            '_log_type': 'application',
            'host': gethostname(),
            'level': self.__get_log_level(record.levelno),
            'Severity': record.levelname,
            'message': record.msg,
        }

        extra = record.args
        if isinstance(extra, dict):
            fields = {}
            # convert all logs custom fields to Gelf pattern
            for k, v in extra.items():
                fields[f'_{k}'] = str(v)
            log.update(fields)

        return dumps(log)

    @staticmethod
    def __get_log_level(levelno):
        return {
            logging.INFO: 6,
            logging.DEBUG: 7,
            logging.ERROR: 3,
            logging.WARN: 4,
            logging.WARNING: 4,
            logging.CRITICAL: 2
        }.get(levelno, 6)


def get_logger(application_name, log_level=1):
    handler_stream = logging.StreamHandler(stdout)
    handler_stream.formatter = GraylogFormatter()

    logger = logging.getLogger(application_name)
    logger.setLevel(level=log_level)
    logger.addHandler(handler_stream)
    logger.propagate = False

    return logger

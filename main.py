from concurrent.futures import ThreadPoolExecutor
from prometheus_client import start_http_server
from sentry_sdk import init as sentry_init
from app.utils.config import get_config
from app.consumer import consume
from app.utils.logger import get_logger
from app.aws.sqs import receive


LOG = get_logger(__name__)
ENV = get_config('ENV')
SENTRY_URL = get_config('SENTRY_DSN')
MAX_WORKERS = get_config('COMSUMER_MAX_WORKERS', default=10, cast='@int')


def start():
    message_first = False

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while(True):
            try:
                messages = receive().get('Messages')

                if message_first is False:
                    LOG.info('Worker Started')
                    message_first = True

                if not messages:
                    continue

                for message in messages:
                    executor.submit(consume, (message))
            except Exception as ex:
                LOG.error(f'Error: {str(ex)}')


if __name__ == '__main__':
    LOG.info(f'Starting Worker env:{ENV}')

    # initialize sentry if exists url
    if SENTRY_URL:
        sentry_init()

    # initialize prometheus server
    start_http_server(5000)

    # initialize application
    start()

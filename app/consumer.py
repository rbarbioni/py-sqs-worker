from prometheus_client import Counter
from json import loads
from app.utils.logger import get_logger
from app.processor.message import process
from app.aws.sqs import delete
from app.utils.config import get_config


LOG = get_logger(__name__)
ENV = get_config('ENV')
COUNTER_SUCCESS = Counter('success', 'success message')
COUNTER_FAIL = Counter('fail', 'fail message')


def consume(message_raw):
    message = loads(message_raw['Body'])
    LOG.info(f'Consuming Message', {'message': message})

    try:
        # process message
        process(message)

        # delete message sqs queue
        delete(message_raw['ReceiptHandle'])

        # Prometheus success counter inc
        COUNTER_SUCCESS.inc()

        # Log success
        LOG.info(f'Message Processed', {'message': message})

    except Exception as ex:
        # Prometheus fail counter inc
        COUNTER_FAIL.inc()
        LOG.error(f'Message Error: {str(ex)}', {'message': message})

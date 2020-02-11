from boto3 import client
from app.utils.config import get_config


QUEUE_URL = get_config('AWS_SQS_QUEUE_URL')
SQS = client('sqs', endpoint_url=get_config('AWS_SQS_ENDPOINT_URL'))


def receive():
    return SQS.receive_message(QueueUrl=QUEUE_URL,
                               MaxNumberOfMessages=get_config('AWS_SQS_MAX_NUMBER_OF_MESSAGES', 1, cast='@int'))


def send(body):
    return SQS.send_message(QueueUrl=QUEUE_URL, MessageBody=body)


def send_batch(entries):
    return SQS.send_message_batch(QueueUrl=QUEUE_URL, Entries=entries)


def delete(receipt_handle):
    return SQS.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=receipt_handle)

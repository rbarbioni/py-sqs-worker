from .base import TestBase
from unittest import TestCase
from unittest.mock import patch
from json import loads, dumps
from app.aws.sqs import receive, send, delete, send_batch


endpoint_url = 'http://localhost:4576'
queue_url = f'{endpoint_url}/123456789012/dev-sqs-test'


class TestSQSClient(TestBase, TestCase):

    def mock_sqs_messages(self, operation_name, kwarg):
        return dumps({'Messages': [loads(self.get_sqs_message())]})

    def test_sqs_receive(self):
        with patch('botocore.client.BaseClient._make_api_call', new=self.mock_sqs_messages):
            resp = receive()
            resp_json = loads(resp)
            messages = resp_json['Messages']
            self.assertEqual(messages[0]['Body'], self.get_message())

    def test_sqs_send(self):
        with patch('botocore.client.BaseClient._make_api_call') as mock:
            test_message = self.get_message()
            send(test_message)
            mock.assert_called_once_with('SendMessage', {
                'QueueUrl': queue_url,
                'MessageBody': test_message
                })

    def test_sqs_send_batch(self):
        with patch('botocore.client.BaseClient._make_api_call') as mock:
            test_message = self.get_message()
            entries = [{'Id': '123', 'MessageBody': test_message}]
            send_batch(entries)
            mock.assert_called_once_with('SendMessageBatch', {
                'QueueUrl': queue_url,
                'Entries': entries
                })

    def test_sqs_delete(self):
        with patch('botocore.client.BaseClient._make_api_call') as mock:
            receipt_handle = 'receipt_handle'
            delete(receipt_handle)
            mock.assert_called_once_with('DeleteMessage', {
                'QueueUrl': queue_url,
                'ReceiptHandle': receipt_handle,
                })

from .base import TestBase
from unittest import TestCase
from json import loads, dumps
from app.consumer import consume


class TestConsumer(TestBase, TestCase):

    def test_consume_success(self):
        message_raw = loads(self.get_sqs_message())
        try:
            consume(message_raw)
            self.assertTrue(True)
        except Exception as ex:
            self.assertIsNone(ex)

    def test_consume_fail(self):
        message_raw = loads(self.get_sqs_message())
        message = loads(message_raw['Body'])
        message.update({'error': 'error message'})
        message_raw['Body'] = dumps(message)
        try:
            consume(message_raw)
        except Exception as ex:
            self.assertEqual(ex.args[0], 'Process Custom Error')

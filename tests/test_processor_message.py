from .base import TestBase
from unittest import TestCase
from app.processor.message import process


class TestProcessorMessage(TestBase, TestCase):

    def test_message_success(self):
        try:
            process({'data': 'message'})
            self.assertTrue(True)
        except Exception as ex:
            self.assertIsNone(ex)

    def test_message_error(self):
        try:
            process({'error': 'error message'})
        except Exception as ex:
            self.assertEqual(ex.args[0], 'Process Custom Error')

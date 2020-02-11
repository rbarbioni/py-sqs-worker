class TestBase:

    def get_message(self):
        return """{"data":"message data"}"""

    def get_sqs_message(self):
        return """
            {
                "MessageId": "43d5f3f4-ed29-4cf4-3ed4-f726dd7cccf0",
                "ReceiptHandle": "honmahrckapfhlezqkbnwcdyninjjcsnzhxdhrzggnwbabsmxfkotohwwuqpzbihloexpdqcn\n
                conejftptqtaqhncwkurbjjuoylazsltryyvsaazxusxwuajiqshesmdbgyccrovwdhdwxcqfagsduusdtyuvbvcqcp\n
                jdmvlbkterdzucmgstdiw",
                "MD5OfBody": "7c7f38596140293023cb9ac8d42791c2",
                "Body": "{\\"data\\":\\"message data\\"}",
                "Attributes": {
                    "SenderId": "AIDAIT2UOQQY3AUEKVGXU",
                    "SentTimestamp": "1581202625235",
                    "ApproximateReceiveCount": "8",
                    "ApproximateFirstReceiveTimestamp": "1581202625242"
                }
            }
            """.replace('\n', '')

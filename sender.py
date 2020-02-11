from json import dumps, loads
from uuid import uuid1
from app.aws.sqs import send_batch
from app.utils.config import get_config


MESSAGES_COUNT = get_config('MESSAGES_COUNT', default=10, cast='@int')
PAYLOAD = loads(get_config('PAYLOAD', default="{\"data\": \"text message\"}"))


def body(i):
    body = PAYLOAD.copy()
    body.update({'idx': i})
    body = dumps(body)
    return body


def part_list(alist, max):
    for i in range(0, len(alist), max):
        yield alist[i:i + max]


if __name__ == "__main__":
    i = 1
    arr = []

    while i <= MESSAGES_COUNT:
        arr.append({
            'Id': str(uuid1()),
            'MessageBody': body(i),
            })
        i += 1

    entries_parts = part_list(arr, 10)

    amount = 0
    for entries in entries_parts:
        amount += len(entries)
        print(f'{amount}')
        send_batch(entries)

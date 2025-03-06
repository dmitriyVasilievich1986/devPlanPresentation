from datetime import datetime
from random import randint
import json


data = [
    {
        "Name": "kjkjbadsda",
        "Age": randint(20, 100),
    },
    {
        "Name": "cvvnzlknxv",
        "Age": randint(20, 100),
    },
]


def handler(event, context):
    return {
        "statusCode": 201,
        "body": json.dumps(
            {"message": "ok", "data": data, "timestamp": datetime.now().isoformat()}
        ),
    }

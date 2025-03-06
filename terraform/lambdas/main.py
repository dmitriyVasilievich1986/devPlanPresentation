from random import randint
import json


data = [
    {
        "name": "kjkjbadsda",
        "age": randint(20, 100),
    }
    {
        "name": "cvvnzlknxv",
        "age": randint(20, 100),
    },
]


def handler(event, context):
    return {"statusCode": 200, "body": json.dumps({"message": "ok", "data": data})}

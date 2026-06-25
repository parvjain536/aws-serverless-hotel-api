import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):

    hotel_id = event["pathParameters"]["id"]

    body = json.loads(event["body"])

    response = table.update_item(
        Key={
            "hotelId": hotel_id
        },
        UpdateExpression="SET #n=:n, city=:c, price=:p",
        ExpressionAttributeNames={
            "#n": "name"
        },
        ExpressionAttributeValues={
            ":n": body["name"],
            ":c": body["city"],
            ":p": Decimal(str(body["price"]))
        },
        ReturnValues="ALL_NEW"
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response["Attributes"], default=int)
    }
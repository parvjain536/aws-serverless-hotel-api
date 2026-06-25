import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):

    hotel_id = event["pathParameters"]["id"]

    response = table.get_item(
        Key={
            "hotelId": hotel_id
        }
    )

    if "Item" not in response:
        return {
            "statusCode": 404,
            "body": json.dumps({
                "message": "Hotel not found"
            })
        }

    return {
    "statusCode": 200,
    "body": json.dumps(response["Item"], default=int)
}
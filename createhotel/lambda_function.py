import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):

    body = json.loads(event["body"])

    hotel = {
        "hotelId": body["hotelId"],
        "name": body["name"],
        "city": body["city"],
        "price": body["price"]
    }

    table.put_item(Item=hotel)

    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Hotel created successfully",
            "hotel": hotel
        })
    }
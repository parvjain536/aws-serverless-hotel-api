import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):

    hotel_id = event["pathParameters"]["id"]

    table.delete_item(
        Key={
            "hotelId": hotel_id
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hotel {hotel_id} deleted successfully"
        })
    }
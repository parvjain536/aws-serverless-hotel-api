AWS Serverless Hotel API
A CRUD REST API built using AWS Serverless services.

A production-style REST API built using AWS Serverless services.

Tech Stack
AWS Lambda
API Gateway
DynamoDB
IAM
Python 3.11
Postman

Features

✔ Create Hotel

✔ Get Hotel

✔ List Hotels

✔ Update Hotel

✔ Delete Hotel


Architecture

             Client
                │
                ▼
         API Gateway
                │
                ▼
          AWS Lambda
                │
                ▼
          DynamoDB


API Endpoints
Method	Endpoint
POST	/hotels
GET	/hotels
GET	/hotels/{id}
PUT	/hotels/{id}
DELETE	/hotels/{id}


Sample Request
{
  "hotelId":"H101",
  "name":"Taj Hotel",
  "city":"Mumbai",
  "price":6000
}


Sample Response
{
  "message":"Hotel created successfully"
}

Services Used
AWS Lambda
API Gateway
DynamoDB
IAM Roles


Tested With
AWS Console
Postman


Author:
Parv Jain







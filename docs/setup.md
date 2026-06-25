# Setup Guide

## Clone Repository

```bash
git clone https://github.com/USERNAME/aws-serverless-hotel-api.git
```

## Create DynamoDB Table

Table Name

Hotels

Partition Key

hotelId (String)

## Create Lambda Functions

- createHotel
- getHotel
- listHotels
- updateHotel
- deleteHotel

## Create API Gateway

POST /hotels

GET /hotels

GET /hotels/{id}

PUT /hotels/{id}

DELETE /hotels/{id}

Attach every route to its corresponding Lambda.

Deploy API.

Done.
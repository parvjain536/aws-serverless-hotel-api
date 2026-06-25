# Architecture

```
             Internet
                 │
                 ▼
          API Gateway
                 │
                 ▼
            AWS Lambda
                 │
                 ▼
            DynamoDB
```

The API Gateway receives requests.

Lambda contains business logic.

DynamoDB stores hotel data.

IAM controls permissions.
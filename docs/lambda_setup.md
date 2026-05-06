# AWS Lambda Setup (Data Ingestion)

## 1. Create Lambda Function
- Go to AWS Console → Lambda → Create Function
- Choose:
    - Runtime: Python 3.x
    - Architecture: x86_64
    - Name: vehicle_telemetry_ingestion

## 2. Configure Permissions
- Attach IAM Role with:
    - AmazonS3FullAccess (or restricted S3 write policy)

## 3. Add Environment Variables
    - BUCKET_NAME = your-bucket-name

## 4. Add Lambda Code
    - Code given in src/aws/lambda_function.py

## 5. Configure Trigger (API Gateway)
    - Create REST API in API Gateway
    - Add route (POST)
    - Integrate with Lambda
    - Deploy API

## 6. Test Ingestion
    - Send sample JSON using:
        - Postman / curl
    - Verify data in S3 /raw/ folder
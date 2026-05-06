# Amazon Redshift Serverless Setup

## 1. Create Redshift   - Serverless
- Go to AWS Console → Redshift → Serverless
- Click Create Workgroup
- Configure:
    - Workgroup name: vehicle-workgroup
    - Namespace name: vehicle-namespace
    - Database name: dev
    - Admin username & password

## 2. Configure Access
- Enable Public access (for development)
- Update Security Group:
    - Allow inbound port 5439
- Note:
    - Workgroup endpoint (used for connection)

## 3. Create IAM Role for S3 Access
- Go to IAM → Create Role
- Select: Redshift
- Attach policy:
    - AmazonS3ReadOnlyAccess
- Copy Role ARN

## 4. Attach Role to Redshift
- Go to Redshift Serverless → Namespace
- Add IAM Role
- Paste Role ARN
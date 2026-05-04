import os
import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_REGION=os.getenv("AWS_REGION")

redshift_client = None
def get_redshift_client():
    global redshift_client
    if redshift_client is None:
        redshift_client = boto3.client("redshift-data", region_name=AWS_REGION)
    return redshift_client
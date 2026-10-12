import os
import boto3
from uuid import uuid4

# Note: When running as a Lambda function, set these as Lambda environment variables.
# When running locally, you can use python-dotenv.
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "")
DYNAMODB_TABLE_NAME = os.environ.get("DYNAMODB_TABLE_NAME", "newtable")

def lambda_handler(event, context):
   
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DYNAMODB_TABLE_NAME)

    
    for record in event['Records']:
        try:
           
            bucket_name = record['s3']['bucket']['name']
            object_key = record['s3']['object']['key']
            size = record['s3']['object'].get('size', -1)
            event_name = record['eventName']
            event_time = record['eventTime']

           
            if bucket_name != S3_BUCKET_NAME:
                continue

           
            table.put_item(
                Item={
                    'unique': str(uuid4()),
                    'Bucket': bucket_name,
                    'Object': object_key,
                    'Size': size,
                    'Event': event_name,
                    'EventTime': event_time
                }
            )

        except Exception as e:
            print("Error processing record:", e)

    return {
        'statusCode': 200,
        'body': 'Data stored successfully in DynamoDB'
    }
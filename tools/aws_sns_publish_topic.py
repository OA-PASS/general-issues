import json
import boto3
import os

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
TOPIC_ARN = os.getenv('AWS_TOPIC_ARN')
DEPLOYMENT_ENVIRONMENT = os.getenv('DEPLOYMENT_ENVIRONMENT')
REGION=os.getenv('AWS_REGION')
COMMIT_REF = os.getenv('TARGET_COMMIT_REF')

MESSAGE = {"action": "DeployStart", "commitRef": COMMIT_REF, "deployEnv": DEPLOYMENT_ENVIRONMENT}

client = boto3.client('sns',
    region_name=REGION,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
    )
response = client.publish(
    TopicArn=TOPIC_ARN,
    Message=json.dumps({'default': json.dumps(MESSAGE)}),
    MessageStructure='json'
)

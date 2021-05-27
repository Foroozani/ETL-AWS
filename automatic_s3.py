import boto3
from secret_key import access_key_DG, secret_access_key_DG
import os
from pprint import pprint

## create bucket

"""resource(self, service_name, region_name=None, api_version=None,
         use_ssl=True, verify=None, endpoint_url=None,
         aws_access_key_id=None, aws_secret_access_key=None,
         aws_session_token=None, config=None)"""
aws_resource = boto3.resource('s3',aws_access_key_id = access_key_DG,
                              aws_secret_access_key = secret_access_key_DG)
bucket = aws_resource.Bucket('foroozani-demoboto3')
response = bucket.create(
    ACL='private',
#    Bucket='string',
    CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'}
)

print(response)

## list the bucket names
resource = boto3.resource("s3")
print(resource)
pprint(list(resource.buckets.all()))    # resource has many attributes, one is called main

# or loop through it
for bucket in resource.buckets.all():
    print(bucket.name)

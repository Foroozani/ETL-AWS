##
from webbrowser import get
from pprint import pprint
import boto3

session = boto3.session.Session(profile_name='DG-dwh')
s3_client = session.client('s3')

for each_bucket in s3_client.list_buckets().get('Buckets'):
    print(each_bucket)

##
for each_bucket in s3_client.list_buckets()['Buckets']:
    print(each_bucket['Name'])

##
session_dev = boto3.session.Session(profile_name='DG-dev', region_name = 'eu-central-1')
# list object in bucket using paginator
s3_client = session_dev.client('s3')

pprint(s3_client.list_buckets().get('Buckets'))
bucket_name = 'degruyter-live-cdnlogging'
# list the object in this bucket

cnt = 1
for each_object in s3_client.list_objects(Bucket= bucket_name)['Contents']:
    print(cnt, each_object['Key'])
    cnt = cnt + 1
# it givesonly 1000 objects in the bucket, therefore we need to use PAGINATOR

## --------------------------------------------------

"""
The available paginators are:
    S3.Paginator.ListMultipartUploads
    S3.Paginator.ListObjectVersions
    S3.Paginator.ListObjects
    S3.Paginator.ListObjectsV2
    S3.Paginator.ListParts
"""
paginator = s3_client.get_paginator('list_objects')
response_iterator = paginator.paginate(Bucket= bucket_name)

count = 1
for each_page in response_iterator:
    for each_object in each_page['Contents']:
        print(count, each_object['Key'])
        count = count + 1
# so far, 115827 cf-logs/E21HP2BQB03VPN.2021-02-02-14.be6ea222.gz


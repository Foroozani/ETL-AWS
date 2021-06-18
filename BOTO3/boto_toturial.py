##
import boto3
from pprint import pprint

session = boto3.Session(profile_name= 'aws-root')
s3 = session.resource('s3')
for each_bucket in s3.buckets.all():
    print(each_bucket.name)
##
#----------------------------------------------------
# a short example to see the difference between 'resource' and 'client' interface
# first validate your credentials
session = boto3.Session(profile_name = 'degruyter')
#----------------------------------------------------
ec2 = session.resource(service_name="ec2")
##
print('Instance information with resource')
for each_ec2 in ec2.instances.all():
    #print(each_ec2.id)
    print(each_ec2.state, each_ec2.id)

## using client 
ec2_cli = session.client(service_name= 'ec2')
pprint(ec2_cli.describe_instances()) # you see the output is in dictionary
##
print('Instance information with client')
for each in ec2_cli.describe_instances()['Reservations']:
    for each_in in each['Instances']:
        print(each_in['InstanceId'], each_in['State']['Name'])

##

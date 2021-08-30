# a simple script to list objects using CLIENT
##
import boto3
from pprint import pprint
# first log in
aws_mag_con = boto3.session.Session(profile_name='DG-dwh')

# now get console for each service iam, ec2, s3
iam_con_client = aws_mag_con.client(service_name='iam', region_name='eu-central-1')
ec2_con_client = aws_mag_con.client(service_name='ec2', region_name='eu-central-1')
s3_con_client = aws_mag_con.client(service_name='s3', region_name='eu-central-1')

##
"""
Lists the IAM users that have the specified path prefix. If no path prefix is specified, 
the operation returns all users in the account"""

response = iam_con_client.list_users()
pprint(response)

for each_item in response['Users']:
    print(each_item['UserName'])

## List all EC2 instance id
responce_ec2 = ec2_con_client.describe_instances()
pprint(responce_ec2)

for each_item in responce_ec2['Reservations']:
    for each_instance in each_item['Instances']:
        print(each_instance['InstanceId'])


#****************************************************************
aws_mag_con=boto3.session.Session(profile_name="DG-dev")
iam_con_re=aws_mag_con.resource(service_name="iam",region_name="eu-central-1")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="eu-central-1")
s3_con_re=aws_mag_con.resource(service_name="s3",region_name="eu-central-1")


#List all iam users
for each_item in iam_con_re.users.all():
	print(each_item.user_name)


for each_item in s3_con_re.buckets.limit(10):
    print(each_item.name)

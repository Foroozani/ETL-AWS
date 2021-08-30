# manuall steps to list all iam users
# step1: get AWS managent consule
# step2: get IAM console
#       options: user, group,...

import boto3

session = boto3.session.Session(profile_name="DG-dwh")
service = aws_man_colsole.resource("iam")

for  user in service.users.all():
    print(user.name)


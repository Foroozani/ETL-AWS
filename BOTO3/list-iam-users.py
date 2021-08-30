# manuall steps to list all iam users
# step1: get AWS managent consule
# step2: get IAM console
#       options: user, group,...

import boto3

aws_man_colsole = boto3.session.Session(profile_name="DG-dwh")
iam_console = aws_man_colsole.resource("iam")

for  user in iam_console.users.all():
    print(user.name)


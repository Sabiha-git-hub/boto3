# I want to implement a simple Python Boto3 script to list all my IAM users.
# Get AWS console
# Then enter any service
# We want to work with IAM, so I will get Iam console
# Then we select, users, roles, policies etc
# To use python boto3 scripts, I will import boto3


import boto3
#we configured our programatic access keys on our local server with some profile names.
#We will start a session with the root profile
#this is the step to get the aws mgt console
aws_mag_con=boto3.session.Session(profile_name="root")
#then we get into the iam console using resource or client options, we are using resource here
iam_con=aws_mag_con.resource('iam')
#now in the iam console, I want to access the users
for each_user in iam_con.users.all():
    print(each_user.name)





#using IAM roles instead of programmatic profiles
#just use default session
#Attach an IAM role to the EC2 enabling it to do things
import boto3

ec2_con=boto3.resource("ec2")

for each in ec2_con.instances.all():
    print(each.id,each.state)
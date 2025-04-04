# Custom Session:

# import boto3
# aws_mag_con=boto3.session.Session(profile_name="root")

# iam_con_re=aws_mag_con.resource(service_name='iam',region_name="us-east-2")
# iam_con_client=aws_mag_con.client(service_name='iam',region_name="us-east-2")

# ===============================================================================
# Default:
# Boto 3 can create a default session and create the aws console
# you have to do 
# aws configure command and give your credentials first
# then we need to create the iam console directly like shown below
import boto3
iam_con_re=boto3.resource(service_name="iam",region_name="us-east-1")
for each_user in iam_con_re.users.all():
    print(each_user.name)


# ===============================================================================



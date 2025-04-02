# what is session?
# it is  management console in our terms.
# We use the profile name to pass the profiles credential
# aws_mag_con=boto3.session.Session(profile_name="root")
# using this session we can create either resource or client objects or services.

# Resource and Client
# we use this to create a service console like, s3 or IAM etc,
# I can use both resource and client object to do this
# iam_con=aws_mag_con.resource('iam')
# iam_con=aws_mag_con.client('iam')
import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
print(dir(aws_mag_con))

#when you do this we can see a lot of operations available
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_loader', '_register_default_handlers', '_session', '_setup_loader', 'available_profiles', 'client', 'events', 'get_available_partitions', 'get_available_regions', 'get_available_resources', 'get_available_services', 'get_credentials', 'get_partition_for_region', 'profile_name', 'region_name', 'resource', 'resource_factory']
print(aws_mag_con.get_available_resources())
# If I do the Print for available resources, only a few resources are supported
# ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']
# The other services sre client supported
# When I use client the output is not a list but a dictionary and a bit difficult to use
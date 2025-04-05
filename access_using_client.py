#We will display all iam users, all s3 buckets and all ec2 instances in the region.
import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
iam_con=aws_mag_con.client('iam')
s3_con=aws_mag_con.client('s3')
ec2_con=aws_mag_con.client('ec2')
#list all iam users using client
print(iam_con.list_users())
# When I do this I get output as a dictionary:
# {'Users': [{'Path': '/', 'UserName': 'AdminOrgMaster', 'UserId': 'AIDAXN6H2HRXKWKGBWTPP', 'Arn': 'arn:aws:iam::510983289966:user/AdminOrgMaster', 'CreateDate': datetime.datetime(2022, 1, 8, 8, 10, 57, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 28, 14, 43, 19, tzinfo=tzutc())}, {'Path': '/', 'UserName': 'EC2_developer', 'UserId': 'AIDAXN6H2HRXL7GMNR4OL', 'Arn': 'arn:aws:iam::510983289966:user/EC2_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 10, 54, 45, tzinfo=tzutc())}, {'Path': '/', 'UserName': 's3_developer', 'UserId': 'AIDAXN6H2HRXIDK2BW5UC', 'Arn': 'arn:aws:iam::510983289966:user/s3_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 11, 2, 1, tzinfo=tzutc())}], 'IsTruncated': False, 'ResponseMetadata': {'RequestId': '284a09b0-83e5-43d4-99a4-e15c69cf7086', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Sat, 05 Apr 2025 10:04:22 GMT', 'x-amzn-requestid': '284a09b0-83e5-43d4-99a4-e15c69cf7086', 'content-type': 'text/xml', 'content-length': '1153'}, 'RetryAttempts': 0}}
#from this I wil only tale users
print(iam_con.list_users()['Users'])
# This is a list output:
# [{'Path': '/', 'UserName': 'AdminOrgMaster', 'UserId': 'AIDAXN6H2HRXKWKGBWTPP', 'Arn': 'arn:aws:iam::510983289966:user/AdminOrgMaster', 'CreateDate': datetime.datetime(2022, 1, 8, 8, 10, 57, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 28, 14, 43, 19, tzinfo=tzutc())}, {'Path': '/', 'UserName': 'EC2_developer', 'UserId': 'AIDAXN6H2HRXL7GMNR4OL', 'Arn': 'arn:aws:iam::510983289966:user/EC2_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 10, 54, 45, tzinfo=tzutc())}, {'Path': '/', 'UserName': 's3_developer', 'UserId': 'AIDAXN6H2HRXIDK2BW5UC', 'Arn': 'arn:aws:iam::510983289966:user/s3_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 11, 2, 1, tzinfo=tzutc())}]
# so we use for loop
for each_user in iam_con.list_users()['Users']:
    print (each_user)
# I get the 3 users as 3 dictionaries output:
# {'Path': '/', 'UserName': 'AdminOrgMaster', 'UserId': 'AIDAXN6H2HRXKWKGBWTPP', 'Arn': 'arn:aws:iam::510983289966:user/AdminOrgMaster', 'CreateDate': datetime.datetime(2022, 1, 8, 8, 10, 57, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 28, 14, 43, 19, tzinfo=tzutc())}
# {'Path': '/', 'UserName': 'EC2_developer', 'UserId': 'AIDAXN6H2HRXL7GMNR4OL', 'Arn': 'arn:aws:iam::510983289966:user/EC2_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 10, 54, 45, tzinfo=tzutc())}
# {'Path': '/', 'UserName': 's3_developer', 'UserId': 'AIDAXN6H2HRXIDK2BW5UC', 'Arn': 'arn:aws:iam::510983289966:user/s3_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 11, 2, 1, tzinfo=tzutc())}
for each_user in iam_con.list_users()['Users']:
    print (each_user['UserName'])

# Now I get the usernames output:
# AdminOrgMaster
# EC2_developer
# s3_developer

# ======================================
#list s3 buckets
#Go to boto3 documentation for s3 clients, we have already created the client s3_con
print(s3_con.list_buckets())
#output is a dictionary
#{'ResponseMetadata': {'RequestId': 'D0BTEM1X3Z8S88YS', 'HostId': 'BXCfgMDnru6YzvxFthVpberEEvqf+XBFCEBpeboS31PbfhVkVqPbeIZcNl+2mVW9RLm5NqESAr6IIokb6Ek7Qq5ZA0usHDFg9/OITOy5ftM=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'BXCfgMDnru6YzvxFthVpberEEvqf+XBFCEBpeboS31PbfhVkVqPbeIZcNl+2mVW9RLm5NqESAr6IIokb6Ek7Qq5ZA0usHDFg9/OITOy5ftM=', 'x-amz-request-id': 'D0BTEM1X3Z8S88YS', 'date': 'Sat, 05 Apr 2025 10:20:35 GMT', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Buckets': [{'Name': 'mybismillahbucket2025', 'CreationDate': datetime.datetime(2025, 3, 28, 9, 3, 33, tzinfo=tzutc())}], 'Owner': {'DisplayName': 'sabihaali1+orgmaster', 'ID': '1bfc93d3ae6c256123bd1bef3be5e66cca7bf5695922467275d4f5ec7816c379'}}
print(s3_con.list_buckets()['Buckets'])
#We get a list output:
#[{'Name': 'mybismillahbucket2025', 'CreationDate': datetime.datetime(2025, 3, 28, 9, 3, 33, tzinfo=tzutc())}]
# so we will use for loop
for each_bucket in s3_con.list_buckets()['Buckets']:
    print (each_bucket)

#We get a dictionary output:
#{'Name': 'mybismillahbucket2025', 'CreationDate': datetime.datetime(2025, 3, 28, 9, 3, 33, tzinfo=tzutc())}
for each_bucket in s3_con.list_buckets()['Buckets']:
    print (each_bucket['Name'])

#Now I get the bucket name
#mybismillahbucket2025

# =====================================
# List the EC2 instances
# Go to boto3 __doc
# We have already created the client ec2_con

 print(ec2_con.describe_instances())
# #We get a dictionary output:
# #{'Reservations': [{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-00a929b66ed6e0de6', 'InstanceId': 'i-0646e0bc2ba9e007b', 'InstanceType': 't2.micro', 'LaunchTime': datetime.datetime(2025, 4, 5, 10, 30, 57, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1c', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-172-31-85-244.ec2.internal', 'PrivateIpAddress': '172.31.85.244', 'ProductCodes': [], 'PublicDnsName': 'ec2-184-72-202-118.compute-1.amazonaws.com', 'PublicIpAddress': '184.72.202.118', 'State': {'Code': 16, 'Name': 'running'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-063bbb710539309c2', 'VpcId': 'vpc-09fbf9965bdbc6a27', 'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'AttachTime': datetime.datetime(2025, 4, 5, 10, 30, 58, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-094a862a456d5fae7'}}], 'ClientToken': 'e32d593e-b812-4f2e-8a12-0ef8a14d5d3c', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-184-72-202-118.compute-1.amazonaws.com', 'PublicIp': '184.72.202.118'}, 'Attachment': {'AttachTime': datetime.datetime(2025, 4, 5, 10, 30, 57, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-0e084523839435f95', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupName': 'launch-wizard-4', 'GroupId': 'sg-04fc78a9ab17837a0'}], 'Ipv6Addresses': [], 'MacAddress': '12:e7:66:2d:ce:5f', 'NetworkInterfaceId': 'eni-09f6c18afec85da9c', 'OwnerId': '510983289966', 'PrivateDnsName': 'ip-172-31-85-244.ec2.internal', 'PrivateIpAddress': '172.31.85.244', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-184-72-202-118.compute-1.amazonaws.com', 'PublicIp': '184.72.202.118'}, 'Primary': True, 'PrivateDnsName': 'ip-172-31-85-244.ec2.internal', 'PrivateIpAddress': '172.31.85.244'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-063bbb710539309c2', 'VpcId': 'vpc-09fbf9965bdbc6a27', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'launch-wizard-4', 'GroupId': 'sg-04fc78a9ab17837a0'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'Name', 'Value': 'Sabiha_instance1'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'required', 'HttpPutResponseHopLimit': 2, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled', 'InstanceMetadataTags': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'BootMode': 'uefi-preferred', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'UsageOperationUpdateTime': datetime.datetime(2025, 4, 5, 10, 30, 57, tzinfo=tzutc()), 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': True, 'EnableResourceNameDnsAAAARecord': False}, 'MaintenanceOptions': {'AutoRecovery': 'default'}}], 'OwnerId': '510983289966', 'ReservationId': 'r-01828c536402d61b1'}], 'ResponseMetadata': {'RequestId': 'a9b1dbec-7690-4abf-aa41-a7ec522a4fcd', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'a9b1dbec-7690-4abf-aa41-a7ec522a4fcd', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'accept-encoding', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '4807', 'date': 'Sat, 05 Apr 2025 10:34:15 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
 print(ec2_con.describe_instances()['Reservations'])
# #Now I get a list output:
#[{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-00a929b66ed6e0de6', 'InstanceId': 'i-0646e0bc2ba9e007b', 'InstanceType': 't2.micro', 'LaunchTime': datetime.datetime(2025, 4, 5, 10, 30, 57, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1c', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-172-31-85-244.ec2.internal', 'PrivateIpAddress': '172.31.85.244', 'ProductCodes': [], 'PublicDnsName': 'ec2-184-72-202-118.compute-1.amazonaws.com', 'PublicIpAddress': '184.72.202.118', 'State': {'Code': 16, 'Name': 'running'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-063bbb710539309c2', 'VpcId': 'vpc-09fbf9965bdbc6a27', 'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'AttachTime': datetime.datetime(2025, 4, 5, 10, 30, 58, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-094a862a456d5fae7'}}], 'ClientToken': 'e32d593e-b812-4f2e-8a12-0ef8a14d5d3c', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-184-72-202-118.compute-1.amazonaws.com', 'PublicIp': '184.72.202.118'}, 'Attachment': {'AttachTime': datetime.datetime(2025, 4, 5, 10, 30, 57, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-0e084523839435f95', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupName': 'launch-wizard-4', 'GroupId': 'sg-04fc78a9ab17837a0'}], 'Ipv6Addresses': [], 'MacAddress': '12:e7:66:2d:ce:5f', 'NetworkInterfaceId': 'eni-09f6c18afec85da9c', 'OwnerId': '510983289966', 'PrivateDnsName': 'ip-172-31-85-244.ec2.internal', 'PrivateIpAddress': '172.31.85.244', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-184-72-202-118.compute-1.amazonaws.com', 'PublicIp': '184.72.202.118'}, 'Primary': True, 'PrivateDnsName': 'ip-172-31-85-244.ec2.internal', 'PrivateIpAddress': '172.31.85.244'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-063bbb710539309c2', 'VpcId': 'vpc-09fbf9965bdbc6a27', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'launch-wizard-4', 'GroupId': 'sg-04fc78a9ab17837a0'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'Name', 'Value': 'Sabiha_instance1'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'required', 'HttpPutResponseHopLimit': 2, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled', 'InstanceMetadataTags': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'BootMode': 'uefi-preferred', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'UsageOperationUpdateTime': datetime.datetime(2025, 4, 5, 10, 30, 57, tzinfo=tzutc()), 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': True, 'EnableResourceNameDnsAAAARecord': False}, 'MaintenanceOptions': {'AutoRecovery': 'default'}}], 'OwnerId': '510983289966', 'ReservationId': 'r-01828c536402d61b1'}]
 for each_ec2 in ec2_con.describe_instances()['Reservations']:
   
   print (each_ec2)
#We get a dictionary  output again
#{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-00a929b66ed6e0de6', 'InstanceId': 'i-0646e0bc2ba9e007b', 'InstanceType': 't2.micro', 'LaunchTime': datetime.datetime(2025, 4, 5, 10, 30, 57, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1c', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-172-31-85-244.ec2.internal', 'PrivateIpAddress': '172.31.85.244', 'ProductCodes': [], 'PublicDnsName': 'ec2-184-72-202-118.compute-1.amazonaws.com', 'PublicIpAddress': '184.72.202.118', 'State': {'Code': 16, 'Name': 'running'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-063bbb710539309c2', 'VpcId': 'vpc-09fbf9965bdbc6a27', 'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'AttachTime': datetime.datetime(2025, 4, 5, 10, 30, 58, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-094a862a456d5fae7'}}], 'ClientToken': 'e32d593e-b812-4f2e-8a12-0ef8a14d5d3c', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-184-72-202-118.compute-1.amazonaws.com', 'PublicIp': '184.72.202.118'}, 'Attachment': {'AttachTime': datetime.datetime(2025, 4, 5, 10, 30, 57, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-0e084523839435f95', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupName': 'launch-wizard-4', 'GroupId': 'sg-04fc78a9ab17837a0'}], 'Ipv6Addresses': [], 'MacAddress': '12:e7:66:2d:ce:5f', 'NetworkInterfaceId': 'eni-09f6c18afec85da9c', 'OwnerId': '510983289966', 'PrivateDnsName': 'ip-172-31-85-244.ec2.internal', 'PrivateIpAddress': '172.31.85.244', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-184-72-202-118.compute-1.amazonaws.com', 'PublicIp': '184.72.202.118'}, 'Primary': True, 'PrivateDnsName': 'ip-172-31-85-244.ec2.internal', 'PrivateIpAddress': '172.31.85.244'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-063bbb710539309c2', 'VpcId': 'vpc-09fbf9965bdbc6a27', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'launch-wizard-4', 'GroupId': 'sg-04fc78a9ab17837a0'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'Name', 'Value': 'Sabiha_instance1'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'required', 'HttpPutResponseHopLimit': 2, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled', 'InstanceMetadataTags': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'BootMode': 'uefi-preferred', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'UsageOperationUpdateTime': datetime.datetime(2025, 4, 5, 10, 30, 57, tzinfo=tzutc()), 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': True, 'EnableResourceNameDnsAAAARecord': False}, 'MaintenanceOptions': {'AutoRecovery': 'default'}}], 'OwnerId': '510983289966', 'ReservationId': 'r-01828c536402d61b1'}

for each_ec2 in ec2_con.describe_instances()['Reservations']:
    print (each_ec2['Instances'])

# This is again a list, so we do nested for loop

for each_ec2 in ec2_con.describe_instances()['Reservations']:
    for each_name in each_ec2['Instances']:
      for each in(each_name['Tags']):
          print(each['Value'])
 
# Now I get the out put:

# Sabiha_instance1
 



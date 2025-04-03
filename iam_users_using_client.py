#list IAM users using client object
import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
iam_con=aws_mag_con.client('iam')
#if I  print the below , I get a dictionary, users is there.
print(iam_con.list_users())
#output={'Users': [{'Path': '/', 'UserName': 'AdminOrgMaster', 'UserId': 'AIDAXN6H2HRXKWKGBWTPP', 'Arn': 'arn:aws:iam::510983289966:user/AdminOrgMaster', 'CreateDate': datetime.datetime(2022, 1, 8, 8, 10, 57, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 28, 14, 43, 19, tzinfo=tzutc())}, {'Path': '/', 'UserName': 'EC2_developer', 'UserId': 'AIDAXN6H2HRXL7GMNR4OL', 'Arn': 'arn:aws:iam::510983289966:user/EC2_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 10, 54, 45, tzinfo=tzutc())}, {'Path': '/', 'UserName': 's3_developer', 'UserId': 'AIDAXN6H2HRXIDK2BW5UC', 'Arn': 'arn:aws:iam::510983289966:user/s3_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 11, 2, 1, tzinfo=tzutc())}], 'IsTruncated': False, 'ResponseMetadata': {'RequestId': '9f9a0635-32cc-4cee-af22-1a1169bf554e', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Thu, 03 Apr 2025 16:15:01 GMT', 'x-amzn-requestid': '9f9a0635-32cc-4cee-af22-1a1169bf554e', 'content-type': 'text/xml', 'content-length': '1153'}, 'RetryAttempts': 0}}

#Now I will take the users key
print(iam_con.list_users()['Users'])
#This output gives me a list, so I can use a for loop      
#output=aws:iam::510983289966:user/AdminOrgMaster', 'CreateDate': datetime.datetime(2022, 1, 8, 8, 10, 57, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 28, 14, 43, 19, tzinfo=tzutc())}, {'Path': '/', 'UserName': 'EC2_developer', 'UserId': 'AIDAXN6H2HRXL7GMNR4OL', 'Arn': 'arn:aws:iam::510983289966:user/EC2_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 10, 54, 45, tzinfo=tzutc())}, {'Path': '/', 'UserName': 's3_developer', 'UserId': 'AIDAXN6H2HRXIDK2BW5UC', 'Arn': 'arn:aws:iam::510983289966:user/s3_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 11, 2, 1, tzinfo=tzutc())}]
for each_user in iam_con.list_users()['Users']:
    print (each_user)
#output= 3 separate dictionaries, so let us tale the 'UserName' key
# {'Path': '/', 'UserName': 'AdminOrgMaster', 'UserId': 'AIDAXN6H2HRXKWKGBWTPP', 'Arn': 'arn:aws:iam::510983289966:user/AdminOrgMaster', 'CreateDate': datetime.datetime(2022, 1, 8, 8, 10, 57, tzinfo=tzutc()), 'PasswordLastUsed': datetime.datetime(2022, 5, 28, 14, 43, 19, tzinfo=tzutc())}
# {'Path': '/', 'UserName': 'EC2_developer', 'UserId': 'AIDAXN6H2HRXL7GMNR4OL', 'Arn': 'arn:aws:iam::510983289966:user/EC2_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 10, 54, 45, tzinfo=tzutc())}
# {'Path': '/', 'UserName': 's3_developer', 'UserId': 'AIDAXN6H2HRXIDK2BW5UC', 'Arn': 'arn:aws:iam::510983289966:user/s3_developer', 'CreateDate': datetime.datetime(2022, 5, 8, 11, 2, 1, tzinfo=tzutc())}
for each_user in iam_con.list_users()['Users']:
    print (each_user['UserName'])

# output=
# AdminOrgMaster
# EC2_developer
# s3_developer
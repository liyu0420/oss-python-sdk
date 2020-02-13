from ossConfig import ossConfig
import Oss

access_key = 'XXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://XXXXXXXXXXXXXXXXX.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'
object_name = 'mytestput'
response = Oss.get_object_acl(config, bucket_name,object_name)
print(response)

ACL = 'public-read'
if Oss.put_object_acl(config,bucket_name,object_name,ACL):
    print("put object acl sucess!")
else:
    print("put object acl fail!")

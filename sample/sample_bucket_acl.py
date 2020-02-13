from ossConfig import ossConfig
import Oss

access_key = 'XXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://XXXXXXXXXXXXXXXXX.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'
response = Oss.get_bucket_acl(config, bucket_name)
print(response)

ACL = 'public-read'
if Oss.put_bucket_acl(config,bucket_name,ACL):
    print("put bucket acl sucess!")
else:
    print("put bucket acl fail!")

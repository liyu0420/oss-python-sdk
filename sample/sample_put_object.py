from ossConfig import ossConfig
import Oss

access_key = 'XXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://XXXXXXXXXXXXXXXXX.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'
object_name = 'mytestput0212'
filename = 'D:\\test\\1084.iso'

if Oss.put_object(config, bucket_name, object_name, filename):
    print("put object sucess!")
else:
    print("put object failed!")

# 指定对象权限
if Oss.put_object(config, bucket_name, object_name, filename, ACL='public-read'):
    print("put object sucess!")
else:
    print("put object failed!")
from ossConfig import ossConfig
import Oss

access_key = 'XXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://XXXXXXXXXXXXXXXXX.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'd11111111'
object_name = 'mytestcopy'
source_bucket = 'test1'
source_object = 'mytestput'

if Oss.copy_object(config, source_bucket,source_object,bucket_name,object_name):
    print("copy object sucess!")
else:
    print("copy object failed!")
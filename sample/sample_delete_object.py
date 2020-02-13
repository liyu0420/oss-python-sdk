from ossConfig import ossConfig
import Oss

access_key = 'XXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://XXXXXXXXXXXXXXXXX.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'
object_name = 'mytestput'

if Oss.delete_object(config, bucket_name, object_name):
    print("delete sucess!")
else:
    print("delete failed!")
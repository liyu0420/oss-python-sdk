from ossConfig import ossConfig
import Oss

access_key = 'XXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://XXXXXXXXXXXXXXXXX.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'
object_name = 'mytestput1'
filename = 'D:\\test\\aaa.py'

if Oss.download_object(config, bucket_name, object_name, filename):
    print("download object sucess!")
else:
    print("download object failed!")
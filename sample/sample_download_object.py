from ossConfig import ossConfig
import Oss

access_key = 'zAlESzJWnKzQPLMW'
secret_key = 'e76HUKfiJs7BDJM0lGnixkZw5gvMz1'
endpoint_url = 'http://oss-cn-north-2.unicloudsrv.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'
object_name = 'mytestput1'
filename = 'D:\\test\\aaa.py'

if Oss.download_object(config, bucket_name, object_name, filename):
    print("download object sucess!")
else:
    print("download object failed!")
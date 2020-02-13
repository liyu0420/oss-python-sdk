from ossConfig import ossConfig
import Oss

access_key = 'zAlESzJWnKzQPLMW'
secret_key = 'e76HUKfiJs7BDJM0lGnixkZw5gvMz1'
endpoint_url = 'http://oss-cn-north-2.unicloudsrv.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'
if Oss.create_bucket(config, bucket_name):
    print("creat bucket sucess!")
else:
    print("create bucket failed!")

if Oss.bucket_exists(config, bucket_name):
    print("bucket exists!")
else:
    print("no bucket")

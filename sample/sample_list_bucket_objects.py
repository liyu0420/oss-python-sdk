from ossConfig import ossConfig
import Oss

access_key = 'zAlESzJWnKzQPLMW'
secret_key = 'e76HUKfiJs7BDJM0lGnixkZw5gvMz1'
endpoint_url = 'http://oss-cn-north-2.unicloudsrv.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'

objects = Oss.list_objects(config, bucket_name)
if objects is not None:
    # List the object names
    for obj in objects:
        print(obj["Key"])
else:
    print("ERROR!")

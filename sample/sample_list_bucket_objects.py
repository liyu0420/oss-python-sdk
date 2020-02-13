from ossConfig import ossConfig
import Oss

access_key = 'XXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://XXXXXXXXXXXXXXXXX.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'

objects = Oss.list_objects(config, bucket_name)
if objects is not None:
    # List the object names
    for obj in objects:
        print(obj["Key"])
else:
    print("ERROR!")

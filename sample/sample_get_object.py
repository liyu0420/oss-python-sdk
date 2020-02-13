from ossConfig import ossConfig
import Oss
import logging

access_key = 'XXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://XXXXXXXXXXXXXXXXX.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'
object_name = 'mytestput'

stream = Oss.get_object(config, bucket_name, object_name)
if stream is not None:
        # Read first chunk of the object's contents into memory as bytes
        data = stream.read(amt=1024)

        # Output object's beginning characters
        logging.info(f'{object_name}: {data[:60]}...')
else:
    print("get_object faild!")
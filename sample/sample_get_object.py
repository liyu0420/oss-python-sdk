from ossConfig import ossConfig
import Oss
import logging

access_key = 'zAlESzJWnKzQPLMW'
secret_key = 'e76HUKfiJs7BDJM0lGnixkZw5gvMz1'
endpoint_url = 'http://oss-cn-north-2.unicloudsrv.com'
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
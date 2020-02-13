from ossConfig import ossConfig
import Oss

access_key = 'zAlESzJWnKzQPLMW'
secret_key = 'e76HUKfiJs7BDJM0lGnixkZw5gvMz1'
endpoint_url = 'http://oss-cn-north-2.unicloudsrv.com'
config = ossConfig(access_key,secret_key,endpoint_url)

list_buckets = Oss.list_buckets(config)
if list_buckets is None:
    print("Error list buckets")
else:
    for bucket in list_buckets['Buckets']:
        print(f'  {bucket["Name"]}')

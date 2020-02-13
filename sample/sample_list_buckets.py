from ossConfig import ossConfig
import Oss

access_key = 'XXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://XXXXXXXXXXXXXXXXX.com'
config = ossConfig(access_key,secret_key,endpoint_url)

list_buckets = Oss.list_buckets(config)
if list_buckets is None:
    print("Error list buckets")
else:
    for bucket in list_buckets['Buckets']:
        print(f'  {bucket["Name"]}')

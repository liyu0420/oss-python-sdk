from ossConfig import ossConfig
import Oss

access_key = 'XXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://XXXXXXXXXXXXXXXXX.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'

#get_website_configuration
get_website_configuration = Oss.get_bucket_website(config, bucket_name)
if get_website_configuration is not None:
    print(get_website_configuration)
else:
    print("Error OR This bucket is not set website!")

#put_bucket_website
website_configuration = {
            'IndexDocument': {'Suffix': 'myindex.html'},
            'ErrorDocument': {'Key': 'myerror.html'}
        }
if Oss.put_bucket_website(config, bucket_name, website_configuration):
    print("put bucket_website sucess!")
else:
    print("put bucket_website failed!")

#delete_bucket_website
if Oss.delete_bucket_website(config, bucket_name):
    print("delete bucket_website sucess!")
else:
    print("delete bucket_website failed!")
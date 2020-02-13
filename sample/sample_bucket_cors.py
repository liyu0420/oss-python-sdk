from ossConfig import ossConfig
import Oss

access_key = 'zAlESzJWnKzQPLMW'
secret_key = 'e76HUKfiJs7BDJM0lGnixkZw5gvMz1'
endpoint_url = 'http://oss-cn-north-2.unicloudsrv.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'ddddd1'

#get_corsConfig
CORSConfiguration=Oss.get_bucket_cors(config, bucket_name)
if CORSConfiguration is False:
    print("The specified bucket does not have CORS configured")
else:
    print(CORSConfiguration)

#put_corsConfig
CORSRules = [
            {
                'AllowedHeaders': [
                    'string111',
                ],
                'AllowedMethods': [
                    'PUT',
                    'POST',
                ],
                'AllowedOrigins': [
                    'string',
                ],
                'ExposeHeaders': [
                    'string',
                ],
                'MaxAgeSeconds': 123
            },
        ]
if Oss.put_bucket_cors(config, bucket_name, CORSRules):
    print("put bucket cors succes!")
else:
    print("put bucket cors failed!")

#delete_corsConfig
if Oss.delete_bucket_cors(config, bucket_name):
    print("delete sucess!")
else:
    print("delete failed!")



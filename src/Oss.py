import boto3
import logging
from botocore.exceptions import ClientError

def oss_client(ossConfig):
    # noinspection PyUnusedLocal
    # noinspection PyShadowingNames
    oss_client = boto3.client(
        service_name=ossConfig.service_name,
        aws_access_key_id=ossConfig.access_key,
        aws_secret_access_key=ossConfig.secret_key,
        endpoint_url=ossConfig.endpoint_url,
        verify=ossConfig.verify
    )
    return oss_client

def oss_resource(ossConfig):
    # noinspection PyUnusedLocal
    # noinspection PyShadowingNames
    oss_resource = boto3.resource(
        service_name=ossConfig.service_name,
        aws_access_key_id=ossConfig.access_key,
        aws_secret_access_key=ossConfig.secret_key,
        endpoint_url=ossConfig.endpoint_url,
        verify=ossConfig.verify
    )
    return oss_resource

def create_bucket(ossConfig,bucket_name):
    try:
        client = oss_client(ossConfig)
        client.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def bucket_exists(ossConfig,bucket_name):
    try:
        client = oss_client(ossConfig)
        client.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def delete_bucket(ossConfig,bucket_name):
    try:
        client = oss_client(ossConfig)
        client.delete_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def list_buckets(ossConfig):
    try:
        client = oss_client(ossConfig)
        response = client.list_buckets()
    except ClientError as e:
        logging.error(e)
        return None
    return response

def put_object(ossConfig,bucket_name,object_name,src_data,ACL='private',StorageClass='STANDARD'):
    if isinstance(src_data, bytes):
        object_data = src_data
    elif isinstance(src_data, str):
        try:
            object_data = open(src_data, 'rb')
            # possible FileNotFoundError/IOError exception
        except Exception as e:
            logging.error(e)
            return False
    else:
        return False

    try:
        client = oss_client(ossConfig)
        client.put_object(Bucket=bucket_name, Key=object_name, Body=object_data,ACL=ACL,StorageClass=StorageClass)
    except ClientError as e:
        logging.error(e)
        return False
    finally:
        if isinstance(src_data, str):
            object_data.close()
    return True

def list_objects(ossConfig,bucket_name):
    try:
        client = oss_client(ossConfig)
        response = client.list_objects(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return None
    return response['Contents']

def copy_object(ossConfig,source_bucket,source_object,bucket_name,object_name,ACL='private'):
    try:
        client = oss_client(ossConfig)
        copy_source = {
            'Bucket' : source_bucket,
            'Key' : source_object
        }
        client.copy_object(CopySource=copy_source,Bucket=bucket_name,Key=object_name,ACL=ACL)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def object_exists(ossConfig,bucket_name,object_name):
    try:
        client = oss_client(ossConfig)
        client.head_object(Bucket=bucket_name,Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def delete_object(ossConfig,bucket_name,object_name):
    if  object_exists(ossConfig,bucket_name,object_name):
        try:
            client = oss_client(ossConfig)
            client.delete_object(Bucket=bucket_name, Key=object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
    return False

def delete_objects(ossConfig,bucket_name,object_names):
    objlist = [{'Key': obj} for obj in object_names]
    isexists = False
    for obj in  object_names:
        if object_exists(ossConfig, bucket_name, obj):
            isexists = True
        else:
            isexists = False
            break
    if isexists :
        try:
            client = oss_client(ossConfig)
            response = client.delete_objects(Bucket=bucket_name, Delete={'Objects': objlist})
            print(response)
        except ClientError as e:
            logging.error(e)
            return False
        return True
    return False

def download_object(ossConfig,bucket_name,object_name,filename):
    try:
        client = oss_client(ossConfig)
        with open(filename, 'wb') as f:
            client.download_fileobj(bucket_name, object_name, f)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def get_object(ossConfig,bucket_name,object_name):
    try:
        client = oss_client(ossConfig)
        response = client.get_object(Bucket=bucket_name, Key=object_name)
    except ClientError as e:
        logging.error(e)
        return None
    return response['Body']

def get_bucket_website(ossConfig,bucket_name):
    try:
        client = oss_client(ossConfig)
        response = client.get_bucket_website(Bucket=bucket_name)
        if 'IndexDocument' in response:
            website_configuration = {
                'IndexDocument': response['IndexDocument']
            }
            if 'ErrorDocument' in response:
                website_configuration.update(ErrorDocument= response['ErrorDocument'])
        else:
            logging.info(f'This bucket not set website!')
            return None
    except ClientError as e:
        logging.error(e)
        return None
    return website_configuration

def put_bucket_website(ossConfig,bucket_name,website_configuration):
    try:
        client = oss_client(ossConfig)
        client.put_bucket_website(Bucket=bucket_name,WebsiteConfiguration=website_configuration)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def delete_bucket_website(ossConfig,bucket_name):
    try:
        client = oss_client(ossConfig)
        client.delete_bucket_website(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def get_bucket_cors(ossConfig,bucket_name):
    try:
        client = oss_client(ossConfig)
        response = client.get_bucket_cors(Bucket=bucket_name)
    except ClientError as e:
        logging.info("The specified bucket does not have CORS configured.")
        return False
    return response['CORSRules']

def put_bucket_cors(ossConfig,bucket_name,CORSRules):
    AllowedMethods = {'PUT','GET','POST','DELETE','HEAD'}
    for Config in CORSRules:
        Methods = Config['AllowedMethods']
        for Method in Methods:
            if Method not in AllowedMethods:
                logging.error("Please enter the correct AllowedMethods!")
                return False
    try:
        client = oss_client(ossConfig)
        Source_CORSRules=get_bucket_cors(ossConfig,bucket_name)
        if Source_CORSRules is False:
            CORSConfiguration ={
                'CORSRules' : CORSRules
            }
        else:
            CORSConfiguration = {
                'CORSRules': Source_CORSRules + CORSRules
            }
        client.put_bucket_cors(Bucket=bucket_name,CORSConfiguration=CORSConfiguration)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def delete_bucket_cors(ossConfig,bucket_name):
    try:
        client = oss_client(ossConfig)
        client.delete_bucket_cors(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def PresignedURLs(ossConfig,bucket_name,object_name,expiration=3600):
    try:
        client = oss_client(ossConfig)
        response = client.generate_presigned_url('get_object',
                                        Params={'Bucket': bucket_name,
                                                'Key': object_name},
                                        ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return False
    return response

def create_multipart_upload(ossConfig,bucket_name,object_name,ACL='private',StorageClass='STANDARD'):
    try:
        client = oss_client(ossConfig)
        response = client.create_multipart_upload(Bucket=bucket_name, Key=object_name,ACL=ACL,StorageClass=StorageClass)
    except ClientError as e:
        logging.error(e)
        return False
    return response['UploadId']

def upload_part(ossConfig,bucket_name,object_name,src_data,partNumber=1,UploadId='string'):
    try:
        client = oss_client(ossConfig)
        response = client.upload_part(Bucket=bucket_name, Key=object_name,Body=src_data,PartNumber=partNumber,UploadId=UploadId)
    except ClientError as e:
        logging.error(e)
        return False
    return response

def complete_multipart_upload(ossConfig,bucket_name,object_name,MulpartUpload,UploadId='string'):
    try:
        client = oss_client(ossConfig)
        client.complete_multipart_upload(Bucket=bucket_name,Key=object_name,MultipartUpload=MulpartUpload,UploadId=UploadId)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def abort_multipart_upload(ossConfig,bucket_name,object_name,UploadId='string'):
    try:
        client = oss_client(ossConfig)
        client.abort_multipart_upload(Bucket=bucket_name,Key=object_name,UploadId=UploadId)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def list_multipart_uploads(ossConfig,bucket_name):
    try:
        client = oss_client(ossConfig)
        response = client.list_multipart_uploads(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return response

def list_parts(ossConfig,bucket_name,object_name,UploadId='string'):
    try:
        client = oss_client(ossConfig)
        response = client.list_parts(Bucket=bucket_name,Key=object_name,UploadId=UploadId)
    except ClientError as e:
        logging.error(e)
        return False
    return response

def get_bucket_acl(ossConfig,bucket_name):
    try:
        client = oss_client(ossConfig)
        response = client.get_bucket_acl(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return response

def put_bucket_acl(ossConfig,bucket_name,ACL):
    try:
        client = oss_client(ossConfig)
        client.put_bucket_acl(Bucket=bucket_name,ACL=ACL)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def get_object_acl(ossConfig,bucket_name,object_name):
    try:
        client = oss_client(ossConfig)
        response = client.get_object_acl(Bucket=bucket_name,Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return response

def put_object_acl(ossConfig,bucket_name,object_name,ACL):
    try:
        client = oss_client(ossConfig)
        client.put_object_acl(Bucket=bucket_name,Key=object_name,ACL=ACL)
    except ClientError as e:
        logging.error(e)
        return False
    return True









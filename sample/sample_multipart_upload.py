from ossConfig import ossConfig
import Oss

access_key = 'XXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://XXXXXXXXXXXXXXXXX.com'
config = ossConfig(access_key,secret_key,endpoint_url)

bucket_name = 'test1'
object_name = 'myMultipartTest'
path = 'D:\\test\\1084.iso'

UploadId = Oss.create_multipart_upload(config,bucket_name,object_name)
print(UploadId)

list_parts = Oss.list_parts(config,bucket_name,object_name,UploadId=UploadId)
print(list_parts)

list_multipart_uploads = Oss.list_multipart_uploads(config,bucket_name)
print(list_multipart_uploads)

if Oss.abort_multipart_upload(config,bucket_name,object_name,UploadId=UploadId):
    print("abort success")
else:
    print("abort fail!")

'''
chuncksize = 100*1024*1024
src = open(path,'rb')
chunckNum = 1
parts_info={'Parts':[]}
while True:
    chunk = src.read(chuncksize)
    if not chunk:
        break
    part = Oss.upload_part(config,bucket_name,object_name,chunk,partNumber = chunckNum,UploadId=UploadId)
    part_info = {
        'ETag':part['ETag'],
        'PartNumber':chunckNum,
    }
    print(part_info)
    parts_info['Parts'].append(part_info)
    chunckNum = chunckNum + 1
src.close()

print(parts_info)

if Oss.complete_multipart_upload(config,bucket_name,object_name,parts_info,UploadId=UploadId):
    print("multipart upload success!")
else:
    print("multipart upload fail!")
'''







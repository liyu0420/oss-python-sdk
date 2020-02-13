class ossConfig:
    service_name = "s3"
    access_key = ""
    secret_key = ""
    endpoint_url = ""
    verify = False

    def __init__(self, ak, sk, endpoint_url):
        self.access_key = ak
        self.secret_key = sk
        self.endpoint_url = endpoint_url



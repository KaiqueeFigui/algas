import os
import boto3
from dotenv import load_dotenv


class BucketServiceHelper:

    def __init__(self):
        load_dotenv()
        os.getenv('')
        self.s3 = boto3.resource(
            service_name='s3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
            aws_session_token=os.getenv('AWS_TOKEN')
        )

        return

    def send(self, bucketname, filename, file_key):
        self.s3.Bucket(bucketname).upload_file(Filename=filename, Key=file_key)
        return


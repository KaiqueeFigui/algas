import service.BucketServiceHelper as BucketServiceHelper
from datetime import datetime
from dotenv import load_dotenv
import os


class BucketService:

    def __init__(self):
        load_dotenv()
        os.getenv('')
        self.bucket_name_not_structured = os.getenv('BUCKET_NAME_NOT_STRUCTURED')
        self.bucket_name_structured = os.getenv('BUCKET_NAME_STRUCTURED')
        self.bucket_name_semi_structured = os.getenv('BUCKET_NAME_SEMI_STRUCTURED')
        self.bucketServiceHelper = BucketServiceHelper.BucketServiceHelper()

    def send_to_not_structured(self, filename, file_key):
        self.__send(self.bucket_name_not_structured, filename, self.__format_file_key(file_key))

    def __send(self, bucketname, filename, file_key):
        print(f"Starting send file to AWS S3 - BucketService::send")
        try:
            self.bucketServiceHelper.send(bucketname, filename, self.__format_file_key(file_key))
        except Exception as ex:
            raise Exception(f"Failed to send file {filename} to AWS S3", ex)
        finally:
            print(f"End send file to AWS S3 - BucketService::send")

    def __format_file_key(self, file_key):
        now = datetime.today().strftime('%Y-%m-%d%H:%M:%S')
        names = file_key.split('.')
        return names[0] + "_" + now + "." + names[1]
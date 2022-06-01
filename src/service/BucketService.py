import src.service.BucketServiceHelper as BucketServiceHelper
from datetime import datetime


class BucketService:

    def __init__(self):
        self.bucketServiceHelper = BucketServiceHelper.BucketServiceHelper()

    def send(self, bucketname, filename, file_key):
        self.bucketServiceHelper.send(bucketname, filename, self.__format_file_key(file_key))
        return True

    def __format_file_key(self, file_key):
        now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        names = file_key.split('.')
        return names[0] + "_" + now + "." + names[1]
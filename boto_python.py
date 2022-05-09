import boto3

class S3_crud():

        def __init__(self):
                self.s3_obj = boto3.resource('s3')
                self.s3_client = boto3.client('s3')

        def make_bucket(self, name):
                location = {'LocationConstraint': 'eu-west-1'}
                self.s3_client.create_bucket(Bucket=name, CreateBucketConfiguration=location)

        def upload_file(self, file_name):
                self.s3_obj.meta.client.upload_file(file_name, 'eng110-sam-python', file_name)

        def retrieve_file(self, file_name):
                self.s3_client.download_file('eng110-sam-python', file_name, file_name)

        def delete_content(self, file_name):
                self.s3_obj.Object('eng110-sam-python', file_name).delete()

        def delete_bucket(self, bucket_name):
                bucket = self.s3_obj.Bucket(bucket_name)
                bucket.delete()

obj = S3_crud()
#obj.make_bucket('eng110-sam-python')
#obj.upload_file('thescreenshot.png')
#obj.retrieve_file('thescreenshot.png')
#obj.delete_content('thescreenshot.png')
#obj.delete_bucket('eng110-sam-python')

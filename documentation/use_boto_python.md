# Instructions

> 1. Install boto using the command `pip3 install boto3.`

> 2. Use `sudo nano boto_python.py` to edit the contents.

> 3. Inside there is a class called `S3_crud`. This class has methods that handle creating buckets, uploading files to S3, retrieving files from S3, deleting content, and deleting buckets.

> 4. In the comments, there is an example of how to use each method in this class. Pay attention to the arguments passed into each method.

## Method details

There is already an object of the `S3_crud` class in the python file called `obj`. To call the methods associated with this class, use the syntax obj.method(). All of the arguments for these methods should be strings.

### Make a Bucket

Call the make bucket method with the syntax obj.make_bucket("bucket_name_here").

### Upload a File

Upload a file to S3 with the syntax obj.upload_file("bucket_name_here", "file_name_here"). 

### Download a file

To download a file from S3 to your EC2 instance, use the command obj.retrieve_file("bucket_name_here", "file_name_here").

### Delete a file

To delete a file stored on S3, use the command obj.delete_content("bucket_name_here", "file_name_here").

### Delete a bucket

To delete a bucket, use the command obj.delete_bucket("bucket_name_here").
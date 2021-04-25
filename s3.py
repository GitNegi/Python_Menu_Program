import boto3

def upload_s3(myphoto, upimage):
    s3 = boto3.resource("s3")
    s3.Bucket(bucket).upload_file(myphoto, upimage)

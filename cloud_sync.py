import boto3
from botocore.exceptions import NoCredentialsError

# AWS credentials
ACCESS_KEY = 'your-access-key'
SECRET_KEY = 'your-secret-key'
BUCKET_NAME = 'your-bucket-name'
FILE_NAME = 'event_log.log'

def create_mock_log_file():
    with open(FILE_NAME, 'w') as f:
        f.write("Event Log:\n")
        f.write("Timestamp, Event\n")
        f.write("2023-01-01 00:00:00, Obstacle detected\n")
        f.write("2023-01-01 00:00:02, Low battery\n")
        f.write("2023-01-01 00:00:04, Path deviation\n")

def upload_to_s3(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

if __name__ == "__main__":
    create_mock_log_file()
    uploaded = upload_to_s3(FILE_NAME, BUCKET_NAME, FILE_NAME)
    if uploaded:
        print(f"File {FILE_NAME} successfully uploaded to {BUCKET_NAME}")

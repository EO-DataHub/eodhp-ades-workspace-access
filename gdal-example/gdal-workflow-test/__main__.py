import os
import sys

import boto3
import rasterio
from rasterio.session import AWSSession

# AWS_VIRTUAL_HOSTING is set to FALSE to directly specify the bucket in the URL
os.environ["AWS_VIRTUAL_HOSTING"] = "FALSE"
aws_session = AWSSession(
    aws_unsigned=False,
    region_name="eu-west-2",
)

out_dir = os.getcwd()


def download_and_process_data(args):
    s3_endpoint = args[1]
    file_name = args[2]

    # Set the environment variable for the S3 endpoint, in the future this will be set outside of the code.
    os.environ["AWS_S3_ENDPOINT"] = s3_endpoint

    read_directly_from_access_point(s3_endpoint, file_name)
    return True


def read_directly_from_access_point(s3_endpoint, file_path):
    # /vsis3/ is a GDAL file system handler that allows on-the-fly random reading of (primarily non-public) files available in AWS S3 buckets, without prior download of the entire file
    full_path = f"/vsis3/{file_path}"

    with rasterio.Env(aws_session):
        with rasterio.open(full_path) as src:
            # Log the metadata of the loaded file
            print("Profile ::", src.profile)
            print(src.read(1))


if __name__ == "__main__":
    download_and_process_data(sys.argv)

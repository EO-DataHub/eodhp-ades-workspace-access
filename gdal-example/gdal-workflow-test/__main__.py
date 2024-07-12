import os
import sys

import boto3
import rasterio
import rioxarray
import xarray as xr

out_dir = os.getcwd()


def download_and_process_data(args):
    """
    This function downloads a file from an S3 bucket and processes it using rasterio and xarray.

    Parameters:
    args (list): A list containing the bucket name at index 1 and the file name at index 2.

    Returns:
    dict: A dictionary containing metadata from rasterio and xarray, and a status code.
    """

    s3 = boto3.client("s3")
    bucket_name = args[1]
    file_name = args[2]

    print(f"Downloading {file_name} from {bucket_name}...")

    base_name = os.path.basename(file_name)
    s3.download_file(bucket_name, file_name, base_name)
    rasterio_metadata = rasterio_example(base_name)
    xarray_metadata = xarray_example(base_name)
    return {"rasterio": rasterio_metadata, "xarray": xarray_metadata, "status": 200}


def rasterio_example(base_name):
    """
    This function opens a file using rasterio and returns its metadata.

    Parameters:
    base_name (str): The name of the file to open.

    Returns:
    dict: A dictionary containing the metadata of the file or an error message.
    """

    try:
        print(f"Rasterio version: {rasterio.__version__}")

        # Open the file using rasterio (GDAL backend)
        dataset = rasterio.open(base_name)
        if dataset is None:
            print("Error: Could not open the file")
            return {"error": "Dataset is None"}
        metadata = dataset.meta
        print(f"Metadata: {metadata}")
        return {"metadata": metadata}
    except Exception as e:
        print("Error: Could not open the file", e)
        return {"error": str(e)}


def xarray_example(base_name):
    """
    This function opens a file using xarray and returns its metadata.

    Parameters:
    base_name (str): The name of the file to open.

    Returns:
    dict: A dictionary containing the metadata of the file or an error message.
    """

    try:
        print(f"Xarray version: {xr.__version__}")
        print(f"Rioxarray version", rioxarray.__version__)

        # Open the file using rioxxarray
        dataset = rioxarray.open_rasterio(base_name)
        if dataset is None:
            print("Error: Could not open the file")
            return {"error": "Dataset is None"}
        metadata = dataset.attrs
        print(f"Metadata: {metadata}")
        return {"metadata": metadata}
    except Exception as e:
        print("Error: Could not open the file", e)
        return {"error": str(e)}


if __name__ == "__main__":
    download_and_process_data(sys.argv)

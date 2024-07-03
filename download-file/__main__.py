## A duplicate of the convert.sh file, but this time written in Python.
#  Depending on success here, this will inform potential to include OpenEO commands within the EOEPCA application package

import datetime as dt
import json
import mimetypes
import os
import sys
import time
from pathlib import Path

import boto3

out_dir = os.getcwd()


## function to determine function to be done, here only resize or invert
def do_func(args):
    s3 = boto3.client("s3")
    bucket_name = args[1]
    file_name = args[2]

    print(f"Downloading {file_name} from {bucket_name}...")

    # Use os.path to get the base name of the file
    base_name = os.path.basename(file_name)

    # Use pathlib.Path to get the name without suffix
    s3.download_file(bucket_name, file_name, base_name)
    createStacItem(base_name)
    createStacCatalogRoot(base_name)


## Need to remove ".png" from end of outName
def createStacItem(outName):
    stem = Path(outName).stem
    now = time.time_ns() / 1_000_000_000
    dateNow = dt.datetime.fromtimestamp(now)
    dateNow = dateNow.strftime("%Y-%m-%dT%H:%M:%S.%f") + "Z"
    size = os.path.getsize(f"{outName}")
    mime = mimetypes.guess_type(f"{outName}")[0]
    data = {
        "stac_version": "1.0.0",
        "id": f"{stem}-{now}",
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [[-180, -90], [-180, 90], [180, 90], [180, -90], [-180, -90]]
            ],
        },
        "properties": {
            "created": f"{dateNow}",
            "datetime": f"{dateNow}",
            "updated": f"{dateNow}",
        },
        "bbox": [-180, -90, 180, 90],
        "assets": {
            f"{stem}": {
                "type": f"{mime}",
                "roles": ["data"],
                "href": f"{outName}",
                "file:size": size,
            }
        },
        "links": [
            {"type": "application/json", "rel": "parent", "href": "catalog.json"},
            {"type": "application/geo+json", "rel": "self", "href": f"{stem}.json"},
            {"type": "application/json", "rel": "root", "href": "catalog.json"},
        ],
    }
    with open(f"{out_dir}/{stem}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def createStacCatalogRoot(outName):
    stem = Path(outName).stem
    data = {
        "stac_version": "1.0.0",
        "id": "catalog",
        "type": "Catalog",
        "description": "Root catalog",
        "links": [
            {"type": "application/geo+json", "rel": "item", "href": f"{stem}.json"},
            {"type": "application/json", "rel": "self", "href": "catalog.json"},
        ],
    }
    with open(f"{out_dir}/catalog.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    do_func(sys.argv)

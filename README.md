## ADES Workspace Data Access Demonstrator

This repository builds a docker image that can be executed as a step in a CWL script to download a file from an S3 access point and output it as part of a STAC catalog. This demonstrates the workspace data accessibility within workflows executed via the ADES.

### Using this repo

To build the docker image run `docker build -t eodhp-test-workflow-access .`.

To run the code locally run `python -m download-file <access_point> <file_path>`

You can execute the provided CWL script using the HTTP file provided. You need to include the access point you wish to use as well as specify the file you wish to download.

### Note
This is a rough repository purely for quick demonstration purposes and is not to be used in production or to serve any other function.
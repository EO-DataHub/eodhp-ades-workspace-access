## ADES Workspace Data Access Demonstrator

This repository contains two examples demonstrating workspace data accessibility within workflows executed via the ADES (Zoo Project). These examples build Docker images that can be executed as steps in CWL scripts.

### Repository Structure

- `download-example`: Demonstrates downloading a file from an S3 access point and outputting it as part of a STAC catalog.
- `gdal-example`: Demonstrates processing geospatial data using GDAL, though it does not return a STAC item. Logs in the workspace S3 access point can be used to verify that it ran successfully.

### Building and Running the Examples

To use either the `download-example` or the `gdal-example`, follow these steps:

1. Navigate to the example directory:
   `cd download-example   # or cd gdal-example`
2. Build the Docker image:
   `docker build -t eodhp-example .`
3. Tag and push the image to Docker Hub or another Docker repository (e.g., AWS ECR):
  ` docker tag eodhp-example <your-repo>/eodhp-example`
   `docker push <your-repo>/eodhp-example`
4. Update the `.cwl` file with the correct image name.
5. Execute the workflow using the provided `.http` file after setting up your environment. We recommend using the `vs-code` extension `REST Client` to execute the `.http` file.


### Note

This repository is designed for demonstration purposes and should not be used in production environments without further modifications.

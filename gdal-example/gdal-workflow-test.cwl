cwlVersion: v1.0
$namespaces:
  s: https://schema.org/
s:softwareVersion: 0.1.2
schemas:
  - http://schema.org/version/9.0/schemaorg-current-http.rdf
$graph:
  # Workflow entrypoint
  - class: Workflow
    id: gdal-workflow-test
    label: Download File App
    doc: Test GDAL Compatibility
    inputs:
      access_point:
        label: access point in S3
        doc: access point in S3
        type: string
      file_name:
        label: file to download
        doc: file to download
        type: string
    outputs:
      - id: results
        type: Directory
        outputSource:
          - gdal-workflow-test/results
    steps:
      gdal-workflow-test:
        run: "#gdal-workflow-test"
        in:
          access_point: access_point
          file_name: file_name
        out:
          - results

  # Main Python script execution
  - class: CommandLineTool
    id: gdal-workflow-test
    hints:
      DockerRequirement:
        dockerPull: public.ecr.aws/n1b3o1k2/eodhp-gdal-workflow-test:latest
    baseCommand: ["/venv/bin/python", "-m", "gdal-workflow-test"]
    inputs:
      access_point:
        type: string
        inputBinding:
          position: 1
      file_name:
        type: string
        inputBinding:
          position: 2
    outputs:
      results:
        type: Directory
        outputBinding:
          glob: .

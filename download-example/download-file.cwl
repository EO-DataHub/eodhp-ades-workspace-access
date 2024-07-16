cwlVersion: v1.0
$namespaces:
  s: https://schema.org/
s:softwareVersion: 0.1.2
schemas:
  - http://schema.org/version/9.0/schemaorg-current-http.rdf
$graph:
  # Workflow entrypoint
  - class: Workflow
    id: download-file
    label: Download File App
    doc: Download a file from an EODHP workspace
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
          - download-file/results
    steps:
      download-file:
        run: "#download-file"
        in:
          access_point: access_point
          file_name: file_name
        out:
          - results
  # convert.sh - takes input args `--url`
  - class: CommandLineTool
    id: download-file
    hints:
      DockerRequirement:
        dockerPull: public.ecr.aws/n1b3o1k2/eodhp-test-workflow-access:0.0.2
    baseCommand: ["python", "-m", "download-file"]
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

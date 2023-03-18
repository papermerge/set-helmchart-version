# set-helmchart-version

This is GitHub action for setting specific version
for "appVersion" attribute in helm charts.


## Usage


### Example workflow


```yaml
name: Set new appVersion

on: [workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master

      - name: Set new appVersion in docs helmchart
        uses: papermerge/set-helmchart-version@master
        with:
          helmchart_file: "charts/docs/Chart.yaml"
          new_app_version: "1.5.20"
```

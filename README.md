# ibma
## Nomenclature
srt - static run time

## Features
- GUI API
- GUI REST operation
- Serverless
- Faas
- on disk and on db input and output as json
- set environment variables to your runtimes
- install packages in your runtime, configure your runtime
- Use your own runtime

## Concept
- You post your input json data to <server>/srt/py37 and that will be copied to payload/py37/input directory by the django server.
- the ibma.py which watches the input directory reads the input json file as soon as it arrvives, passes the `data` to the `function` mentioned in the input json.
- The `function` in the input json after processing the `data` in the input json will write its output json to the output directory.


## Usage
1. Mount the payload directory to the root directory of a python 3.7.x container
2. ibma.py should run at startup of the python container [may be trigger with entrypoing.sh]
3. post your input json to <server>/srt/py37
4. input json will be copied to input directory and the output will be to the output directory
5. if you want the output to be also be available in the database and deleted from the output directory then do an empty post to <server>/srt/py37/id/output


### resources
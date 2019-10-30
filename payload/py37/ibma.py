import os
import json
from pathlib import Path
from functions.generic import *
import time
import datetime

INPUT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'input'))
OUTPUT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'output'))


def runner(input_jsonfile):
    '''
    parses a json file, runs the function mentioned in that json file
    by passing the data in that jsonfile as an argument to hte function
    '''
    try:
        with open(input_jsonfile, 'r') as f:
            datastore = json.load(f)
        function = datastore['function']
        data = datastore['data']
    except Exception as e:
        return e
    return eval(function)(data)


def get_input_files():
    files = [x for x in os.listdir(INPUT_DIR) if x.endswith('.json')]
    print('checking for input files')
    input_files = [os.path.join(INPUT_DIR, file) for file in files]
    return input_files


def looper():
    input_files = get_input_files()
    seconds = 2  # sleep timer
    while 1:
        for input_jsonfile in input_files:
            try:
                data = runner(input_jsonfile)
                input_filename = os.path.basename(input_jsonfile)
                output_filename = input_filename.replace(
                    '.json', '_output.json')
                outputs = os.path.abspath(os.path.join(
                    os.path.dirname(__file__), '..', '..', 'payload', 'py37', 'output'))
                file = os.path.join(outputs, output_filename)
                with open(file, 'w') as outfile:
                    json.dump(data, outfile)
                print(data)
                os.remove(input_jsonfile)
            except Exception as e:
                return e
        input_files = get_input_files()
        print(datetime.datetime.now())
        print(f'sleeping for {seconds} seconds')
        time.sleep(seconds)


looper()

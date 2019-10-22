'''
This containers Generic or demo functions.
You should create separate modules for each of the products/vendors
and import them in ibma.py as
from functions.<your module name> import *
ex: you created azure.py with azure functions adjacent to generic.py
then in ibma.py you do the following.
from functions.azure import *
'''
import os


def uppercase(data):
    '''takes a non nested dictionary and converts the values to uppercase.
    This is for demo'''
    output = {}
    for k, v in data.items():
        output[k] = v.upper()
    return output


def py37_config_pip_install(data):
    '''
    add python packages to py37 with pip.
    example POST data.
    {
        "payload": {
        "data": {
            "packageX": "package version",
            "packageY": "package version"
        },
        "function": "py37_config_pip_install"
        }
    }
    '''
    outputs = []
    for k, v in data.items():
        try:
            command = f"pip install {k}=={v}"
            output = os.system(command)
        except Exception as e:
            outputs += e
    return outputs

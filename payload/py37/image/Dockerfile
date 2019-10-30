FROM python:3.7-alpine
ADD requirements.txt /
RUN pip install -r /requirements.txt
ENTRYPOINT [ "python", "/payload/py37/ibma.py" ]
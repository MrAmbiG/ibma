from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.apps import apps

# Create your views here.
class py37View(viewsets.ModelViewSet):
    queryset = Py37.objects.all()
    serializer_class = Py37Serializer


OUTPUT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'payload', 'py37', 'output'))


def get_output_files():
    files = [x for x in os.listdir(OUTPUT_DIR) if x.endswith('.json')]
    print('checking for output file')
    output_files = [os.path.join(OUTPUT_DIR, file) for file in files]
    return output_files


@csrf_exempt
@api_view(['POST'])
def outputter(*args, **kwargs):
    '''
    Gets the unique id of the input json file.
    searches for a <uid>_output.json file in output directory and
    if found it udpates the database with the output for the uid.
    '''
    model = kwargs['model']
    Model = apps.get_model('srt', model)
    uid = kwargs['uid']

    filename = f'{uid}_output.json'
    filepath = os.path.join(OUTPUT_DIR, filename)
    status = False
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            output = json.load(f)

        obj = Model.objects.get(id=uid)
        if 'output' in obj.payload:
            if obj.payload['output'] is not output:
                obj.payload['output'] = output
                obj.save()
        else:
            obj.payload['output'] = output
            obj.save()
        status = True
        os.remove(filepath)
    return Response({
        "status": status
    })

from rest_framework import serializers
from .models import *


class Py37Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Py37
        fields = ('id', 'url', 'payload')

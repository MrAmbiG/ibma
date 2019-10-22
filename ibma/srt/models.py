from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.postgres.fields import JSONField
import json
import os


# Create your models here.
class Py37(models.Model):
    payload = JSONField()

    class Meta:
        managed = True
        db_table = 'py37'


@receiver(post_save, sender=Py37)
def write(sender, instance, created, **kwargs):
    inputs = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', '..', 'payload', 'py37', 'input'))
    data = instance.payload
    if 'output' not in data:
        id = instance.id
        file = os.path.join(inputs, f'{id}.json')
        with open(file, 'w') as outfile:
            json.dump(data, outfile)

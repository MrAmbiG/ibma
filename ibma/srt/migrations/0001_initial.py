# Generated by Django 2.2.3 on 2019-08-12 07:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Py37',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'db_table': 'py37',
                'managed': True,
            },
        ),
    ]

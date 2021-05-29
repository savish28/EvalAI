# Generated by Django 2.2.13 on 2021-05-29 22:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0083_challengephase_annotations_uploaded_using_cli"),
    ]

    operations = [
        migrations.AddField(
            model_name="challengeevaluationcluster",
            name="active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="challengeevaluationcluster",
            name="route_table_association_ids",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=256),
                blank=True,
                default=list,
                size=None,
            ),
        ),
    ]

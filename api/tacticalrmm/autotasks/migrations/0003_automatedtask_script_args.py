# Generated by Django 3.1 on 2020-08-30 05:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autotasks", "0002_auto_20200701_1615"),
    ]

    operations = [
        migrations.AddField(
            model_name="automatedtask",
            name="script_args",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=255, null=True),
                blank=True,
                default=list,
                null=True,
                size=None,
            ),
        ),
    ]

# Generated by Django 3.1 on 2020-09-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agents", "0012_auto_20200810_0544"),
    ]

    operations = [
        migrations.AddField(
            model_name="agent",
            name="patches_last_installed",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-07 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstreport', '0009_remove_report_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]

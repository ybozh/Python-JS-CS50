# Generated by Django 3.2.8 on 2021-11-07 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstreport', '0010_report_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='duration',
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-29 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatapp', '0002_flatbooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatbooking',
            name='FlatType',
        ),
    ]

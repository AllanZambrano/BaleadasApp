# Generated by Django 2.2.3 on 2019-07-24 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marker',
            old_name='point',
            new_name='geom',
        ),
    ]

# Generated by Django 3.0.7 on 2020-09-26 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publiapp_api', '0011_auto_20200926_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='Ubigeo',
            new_name='ubigeo',
        ),
    ]

# Generated by Django 3.0.7 on 2020-09-22 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publiapp_api', '0008_auto_20200922_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleanuncio',
            name='tipoAnuncio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publiapp_api.Constantes'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-07-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publiapp_api', '0003_articulo_categoria_negocio_resenia_servicio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='nivel_anunciante',
            new_name='nivel_anuncio',
        ),
        migrations.AddField(
            model_name='resenia',
            name='usuario',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
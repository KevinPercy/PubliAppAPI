# Generated by Django 3.0.7 on 2020-07-02 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publiapp_api', '0002_anuncio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_articulo', models.CharField(max_length=100)),
                ('descripcion_articulo', models.CharField(max_length=300)),
                ('precio', models.FloatField()),
                ('precio_promo', models.FloatField()),
                ('id_categoria', models.CharField(max_length=5)),
                ('id_resenia', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=40)),
                ('tipo_categoria', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_negocio', models.CharField(max_length=100)),
                ('descripcion_negocio', models.CharField(max_length=300)),
                ('precio', models.FloatField()),
                ('precio_promo', models.FloatField()),
                ('id_categoria', models.CharField(max_length=5)),
                ('id_resenia', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Resenia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=40)),
                ('puntuacion', models.IntegerField(default=0)),
                ('equipo', models.CharField(default='ND', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=100)),
                ('descripcion_servicio', models.CharField(max_length=300)),
                ('precio', models.FloatField()),
                ('precio_promo', models.FloatField()),
                ('id_categoria', models.CharField(max_length=5)),
                ('id_resenia', models.CharField(max_length=5)),
            ],
        ),
    ]
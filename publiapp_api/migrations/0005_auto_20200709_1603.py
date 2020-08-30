# Generated by Django 3.0.7 on 2020-07-09 16:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publiapp_api', '0004_auto_20200702_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='estado',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='id_articulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Articulo'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='id_negocio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Negocio'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='id_servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Servicio'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='id_categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Categoria'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='id_resenia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Resenia'),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='id_categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Categoria'),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='id_resenia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Resenia'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='id_categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Categoria'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='id_resenia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Resenia'),
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.FileField(upload_to='')),
                ('es_principal', models.BooleanField(default=False)),
                ('id_anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publiapp_api.Anuncio')),
            ],
        ),
        migrations.CreateModel(
            name='Anunciante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('apellidos', models.CharField(max_length=120)),
                ('dni', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=50)),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Rol')),
            ],
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='id_anunciante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Anunciante'),
        ),
    ]

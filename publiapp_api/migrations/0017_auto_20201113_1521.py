# Generated by Django 3.0.7 on 2020-11-13 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publiapp_api', '0016_auto_20201111_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dni',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='id_rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publiapp_api.Rol'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='Perez', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
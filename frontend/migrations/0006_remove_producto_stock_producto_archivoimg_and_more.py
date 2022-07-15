# Generated by Django 4.0.1 on 2022-06-09 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='stock',
        ),
        migrations.AddField(
            model_name='producto',
            name='archivoImg',
            field=models.CharField(default=1, max_length=256, verbose_name='Imagen Producto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default=1, verbose_name='Descripcion Producto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='rating',
            field=models.FloatField(default=1, verbose_name='Rating Producto'),
            preserve_default=False,
        ),
    ]

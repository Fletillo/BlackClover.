# Generated by Django 4.0.5 on 2022-07-08 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_remove_producto_stock_producto_archivoimg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1, verbose_name='Stock'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-11 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitioWeb', '0006_rename_categoria_subcategoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategoria',
            options={'verbose_name': 'subCategoria', 'verbose_name_plural': 'subCategorias'},
        ),
        migrations.AlterModelTable(
            name='subcategoria',
            table='subCategorias',
        ),
    ]

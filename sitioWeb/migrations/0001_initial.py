# Generated by Django 5.1.1 on 2024-10-13 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'db_table': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='EstadoDelProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Estado del Producto',
                'verbose_name_plural': 'Estados del Producto',
                'db_table': 'EstadosDelProducto',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('contraseña', models.CharField(default='00000000', max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('celular', models.CharField(blank=True, max_length=15, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estadoUsuario', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado_producto', models.BooleanField(blank=True, default=True, null=True)),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sitioWeb.estadodelproducto')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta', models.ImageField(upload_to='productos/')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='sitioWeb.producto')),
            ],
            options={
                'verbose_name': 'Imagen del Producto',
                'verbose_name_plural': 'Imágenes del Producto',
                'db_table': 'ProductImages',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provincias', to='sitioWeb.departamento')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'db_table': 'Provincias',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sitioWeb.provincia'),
        ),
        migrations.CreateModel(
            name='subCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='sitioWeb.categoria')),
            ],
            options={
                'verbose_name': 'subCategoria',
                'verbose_name_plural': 'subCategorias',
                'db_table': 'subCategorias',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='subcategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sitioWeb.subcategoria'),
        ),
        migrations.AddField(
            model_name='producto',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sitioWeb.usuario'),
        ),
        migrations.CreateModel(
            name='CarritoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios_en_carrito', to='sitioWeb.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos_en_carrito', to='sitioWeb.usuario')),
            ],
            options={
                'verbose_name': 'Producto en Carrito',
                'verbose_name_plural': 'Productos en Carrito',
                'db_table': 'Carrito_Productos',
            },
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-05 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_de_documento_identificatorio', models.CharField(max_length=200)),
                ('nr_documento_identidad', models.IntegerField()),
                ('correo_electronico_afiliado', models.EmailField(max_length=254)),
                ('tipo_de_usuario', models.CharField(max_length=200)),
                ('tipo_de_suscripcion', models.CharField(max_length=15)),
                ('nr_de_usuarios', models.IntegerField()),
                ('fecha_de_suscripcion', models.DateField()),
                ('ultima_renovacion', models.DateField()),
                ('suscripcion_automatica', models.BooleanField()),
                ('fecha_de_cancelacion', models.TextField()),
                ('solicitudes_de_investigacion', models.TextField()),
                ('rol', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-15 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('correos', models.CharField(max_length=40)),
                ('contrasena', models.CharField(max_length=20)),
            ],
        ),
    ]
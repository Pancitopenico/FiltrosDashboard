# Generated by Django 2.2 on 2019-04-19 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='jornal',
            options={'verbose_name': 'Jornal', 'verbose_name_plural': 'Jornais'},
        ),
    ]

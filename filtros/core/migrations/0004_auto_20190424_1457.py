# Generated by Django 2.2 on 2019-04-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190424_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornal',
            name='titulo',
            field=models.CharField(max_length=120),
        ),
    ]

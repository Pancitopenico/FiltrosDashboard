# Generated by Django 2.2 on 2019-04-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190424_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornal',
            name='data_publicada',
            field=models.DateTimeField(null=True),
        ),
    ]

# Generated by Django 4.1.3 on 2023-07-31 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='column2',
            field=models.IntegerField(default=0),
        ),
    ]

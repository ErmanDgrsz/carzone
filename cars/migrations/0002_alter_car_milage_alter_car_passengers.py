# Generated by Django 4.0.4 on 2022-10-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='milage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 2.1.3 on 2018-11-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandPage', '0003_auto_20181111_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='creationDate',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='partonymic',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(default='', max_length=64),
        ),
    ]

# Generated by Django 2.1.3 on 2018-11-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandPage', '0010_auto_20181112_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('shortNews', models.CharField(max_length=128)),
                ('detailedNews', models.CharField(max_length=128)),
                ('creationDate', models.DateTimeField(auto_now=True, max_length=64)),
            ],
        ),
    ]

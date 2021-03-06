# Generated by Django 2.1.3 on 2018-11-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricityMeters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=16)),
                ('date', models.DateField()),
                ('value', models.IntegerField(max_length=16)),
                ('zone', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=16)),
                ('adress', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('ava', models.ImageField(upload_to='')),
                ('total_square', models.IntegerField(max_length=32)),
                ('cnt_fiodr', models.IntegerField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=16)),
                ('title', models.CharField(max_length=64)),
                ('text', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='WaterMeters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=16)),
                ('date', models.DateField()),
                ('value', models.IntegerField(max_length=16)),
            ],
        ),
    ]

# Generated by Django 2.1.3 on 2018-11-15 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandPage', '0011_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='defaultuser',
            name='mail',
            field=models.EmailField(blank=True, max_length=128),
        ),
    ]
# Generated by Django 2.0.3 on 2019-02-14 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloglist', '0005_auto_20190213_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
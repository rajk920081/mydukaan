# Generated by Django 3.1.3 on 2021-01-20 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='userid',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

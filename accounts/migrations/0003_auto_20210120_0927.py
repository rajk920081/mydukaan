# Generated by Django 3.1.3 on 2021-01-20 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userid',
            field=models.PositiveIntegerField(auto_created=True, default=1000),
        ),
    ]

# Generated by Django 3.1.3 on 2021-01-20 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='pic.png', upload_to='accounts/uploads/images')),
                ('password', models.CharField(max_length=400)),
                ('mobile', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

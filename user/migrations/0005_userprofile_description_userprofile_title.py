# Generated by Django 5.0 on 2023-12-08 22:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_userprofile_upload_files_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
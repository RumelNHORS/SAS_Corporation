# Generated by Django 4.2.16 on 2024-09-21 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sas', '0002_businesspartner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=250, null=True)),
                ('project_image', models.FileField(blank=True, null=True, upload_to='projects/images')),
                ('project_link', models.URLField(blank=True, max_length=250, null=True)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='businesspartner',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2024, 9, 21, 9, 21, 43, 37809, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businesspartner',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='service',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2024, 9, 21, 9, 21, 51, 493461, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]

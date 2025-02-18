# Generated by Django 4.2.16 on 2024-10-03 06:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sas', '0010_ourteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurITSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criticism', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='criticism/')),
            ],
        ),
    ]

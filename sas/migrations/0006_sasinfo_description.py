# Generated by Django 4.2.16 on 2024-09-22 06:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sas', '0005_aboutus_sasinfo_webprimarycolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='sasinfo',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

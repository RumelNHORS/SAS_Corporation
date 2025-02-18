# Generated by Django 4.2.16 on 2024-09-22 07:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sas', '0006_sasinfo_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sasinfo',
            name='description',
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businesspartner',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sasinfo',
            name='address',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

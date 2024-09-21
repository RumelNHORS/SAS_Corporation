# Generated by Django 4.2.16 on 2024-09-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sas', '0003_projects_businesspartner_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SasGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('picture', models.FileField(blank=True, null=True, upload_to='gallery/images')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]

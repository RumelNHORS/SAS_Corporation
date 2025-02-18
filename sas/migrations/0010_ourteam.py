# Generated by Django 4.2.16 on 2024-10-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sas', '0009_ourclient'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('designation', models.CharField(max_length=250)),
                ('picture', models.FileField(blank=True, null=True, upload_to='team/')),
                ('facebook', models.URLField(blank=True, max_length=250, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=250, null=True)),
                ('twitter', models.URLField(blank=True, max_length=250, null=True)),
                ('github', models.URLField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]

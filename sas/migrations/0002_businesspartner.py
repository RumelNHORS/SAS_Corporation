# Generated by Django 4.2.16 on 2024-09-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='companies/images/')),
                ('description', models.TextField()),
                ('website_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]

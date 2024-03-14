# Generated by Django 4.2.10 on 2024-03-06 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('tour_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.tourcompany')),
            ],
            options={
                'verbose_name': 'Tour Image',
                'verbose_name_plural': 'Tour Images',
            },
        ),
    ]

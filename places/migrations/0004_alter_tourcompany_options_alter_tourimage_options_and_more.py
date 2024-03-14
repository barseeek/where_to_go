# Generated by Django 4.2.10 on 2024-03-09 19:28

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_tourimage_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tourcompany',
            options={'verbose_name': 'Tour Company', 'verbose_name_plural': 'Tour Companies'},
        ),
        migrations.AlterModelOptions(
            name='tourimage',
            options={'ordering': ('position',), 'verbose_name': 'Tour Image', 'verbose_name_plural': 'Tour Images'},
        ),
        migrations.AlterField(
            model_name='tourcompany',
            name='description_long',
            field=tinymce.models.HTMLField(),
        ),
    ]

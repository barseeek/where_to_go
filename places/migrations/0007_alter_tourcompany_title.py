# Generated by Django 4.2.10 on 2024-03-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_tourimage_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourcompany',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
    ]

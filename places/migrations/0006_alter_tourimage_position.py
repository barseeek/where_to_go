# Generated by Django 4.2.10 on 2024-03-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_tourcompany_options_alter_tourimage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourimage',
            name='position',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='Позиция'),
        ),
    ]
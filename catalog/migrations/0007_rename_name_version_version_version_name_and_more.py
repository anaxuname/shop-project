# Generated by Django 4.2.7 on 2023-12-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='name_version',
            new_name='version_name',
        ),
        migrations.AlterField(
            model_name='version',
            name='active_version',
            field=models.BooleanField(verbose_name='признак текущей версии'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-07 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0003_alter_datas_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datas',
            old_name='Description',
            new_name='DESCRIPTION',
        ),
    ]

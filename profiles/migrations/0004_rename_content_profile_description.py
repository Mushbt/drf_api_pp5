# Generated by Django 3.2.23 on 2023-12-01 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20231126_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='content',
            new_name='description',
        ),
    ]

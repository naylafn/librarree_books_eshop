# Generated by Django 5.1 on 2024-09-17 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_bookentry_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookEntry',
            new_name='Book',
        ),
    ]

# Generated by Django 4.2 on 2024-07-03 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_project_technologies_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Technologies',
            new_name='Technology',
        ),
    ]
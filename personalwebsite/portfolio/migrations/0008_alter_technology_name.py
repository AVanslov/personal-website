# Generated by Django 4.2 on 2024-07-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_rename_technologies_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]

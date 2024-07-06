# Generated by Django 4.2 on 2024-07-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_project_technologies_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='body_text_en',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='body_text_ru',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='name_en',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='name_ru',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='short_description_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='short_description_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='name_en',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='name_ru',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
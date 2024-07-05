# Generated by Django 4.2 on 2024-07-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_technologies_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='main_foto',
            field=models.ImageField(default='project_main_photo/unsplash-photo-1.jpg', upload_to='project_main_photo/', verbose_name='Project main photo'),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies_id',
            field=models.ManyToManyField(related_name='tag', to='portfolio.technologies'),
        ),
        migrations.AlterField(
            model_name='technologies',
            name='badge',
            field=models.ImageField(default='badges/icons8-python-48.png', upload_to='badges', verbose_name='Badge'),
        ),
    ]
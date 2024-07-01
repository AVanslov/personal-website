from django.db import models

NAME_LENGTH = 128
SHORT_DESCRIPTION_LENGTH = 250
DESCRIPTION_LENGTH = 500
BODY_MAX_LENGTH = 10000


class Technologies(models.Model):
    name = models.CharField(max_length=NAME_LENGTH)
    badge = models.ImageField(
        'Badge',
        upload_to='badges',
        default='badges/icons8-python-48.png',
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=NAME_LENGTH)
    short_description = models.CharField(max_length=SHORT_DESCRIPTION_LENGTH)
    description = models.CharField(max_length=DESCRIPTION_LENGTH)
    main_foto = models.ImageField(
        'Project main photo',
        upload_to='project_main_photo/',
        default='project_main_photo/unsplash-photo-1.jpg',
    )
    body_text = models.TextField(
        max_length=BODY_MAX_LENGTH
    )
    code_url = models.URLField()
    production_url = models.URLField()
    pub_date = models.DateField(auto_now=False, auto_now_add=False)
    technologies_id = models.ManyToManyField(Technologies, related_name='tags')

    def __str__(self):
        return self.name
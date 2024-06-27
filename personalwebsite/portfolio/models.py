from django.db import models

NAME_LENGTH = 128


class Project(models.Model):
    name = models.CharField(max_length=NAME_LENGTH)

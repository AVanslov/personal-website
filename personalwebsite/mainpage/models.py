from django.db import models

NUMBER_OF_VISIBLE_CHATACTERS = 15


class Resume(models.Model):
    text = models.TextField('Текст')
    last_edit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:NUMBER_OF_VISIBLE_CHATACTERS]

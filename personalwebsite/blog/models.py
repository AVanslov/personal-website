from django.db import models

MAXIMUM_STRING_LENGTH = 256

NUMBER_OF_VISIBLE_CHATACTERS = 15


class TitleModel(models.Model):
    """Модель абстрактного класса Заголовок."""

    name = models.CharField('Заголовок', max_length=MAXIMUM_STRING_LENGTH,)

    class Meta:
        abstract = True


class Category(TitleModel):
    """Модель таблицы Категория."""

    description = models.TextField('Описание')
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        max_length=64,
        help_text=(
            'Идентификатор страницы для URL; разрешены символы латиницы, '
            'цифры, дефис и подчёркивание.'
        ),
    )

    def __str__(self):
        return self.title[:NUMBER_OF_VISIBLE_CHATACTERS]


class Post(TitleModel):
    """Модель таблицы Публикация."""

    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем'
            ' — можно делать отложенные публикации.'
        )
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True,
    )
    main_foto = models.ImageField(
        'Фото',
        upload_to='post_images',
        blank=True,
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        default_related_name = 'posts'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title[:NUMBER_OF_VISIBLE_CHATACTERS]

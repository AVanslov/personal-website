from modeltranslation.translator import TranslationOptions, register

from .models import Category, Post


@register(Category)
class CategoryTranslationOprions(TranslationOptions):
    fields = ('name', 'description')


@register(Post)
class PostTranslationOprions(TranslationOptions):
    fields = ('name', 'text')

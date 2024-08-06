from modeltranslation.translator import TranslationOptions, register

from .models import Project, Technology


@register(Technology)
class CategoryTranslationOprions(TranslationOptions):
    fields = ('name',)


@register(Project)
class PostTranslationOprions(TranslationOptions):
    fields = (
        'name',
        'short_description',
        # 'description',
        'body_text',
    )

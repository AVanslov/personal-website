from modeltranslation.translator import TranslationOptions, register

from .models import Resume


@register(Resume)
class ResumeTranslationOprions(TranslationOptions):
    fields = ('text',)

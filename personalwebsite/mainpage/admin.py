from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Resume


@admin.register(Resume)
class ResumeAdmin(TranslationAdmin):
    """Resume."""
    list_display = (
        'text',
    )

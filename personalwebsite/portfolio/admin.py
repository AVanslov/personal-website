from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Project, Technology


@admin.register(Technology)
class TechnologyAdmin(TranslationAdmin):
    list_display = (
        'name',
        'badge',
        'slug',
    )


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = (
        'name',
        'short_description',
        'description',
        'body_text',
    )

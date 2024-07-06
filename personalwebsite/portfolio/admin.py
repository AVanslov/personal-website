# from django import forms
from django.contrib import admin
# from ckreditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

from .models import (
    Project,
    Technology,
)


# class TechnologyAdminForm(forms.ModelForm):
#     name_ru = forms.CharField(label='Название', widget=CKEditorUploadingWidget())



@admin.register(Technology)
class TechnologyAdmin(TranslationAdmin):
    list_display = (
        'name',
        'badge',
        'slug',
    )
    # form = TechnologyAdminForm


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = (
        'name',
        'short_description',
        'description',
        'body_text',
    )

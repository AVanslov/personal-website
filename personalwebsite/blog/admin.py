from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    """Category."""
    list_display = (
        'name',
        'description',
        'slug',
    )
    list_display_links = ('name',)


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    """Post."""
    list_display = (
        'name',
        'text',
        'pub_date',
        'category',
        'main_foto',
    )
    list_display_links = ('name',)

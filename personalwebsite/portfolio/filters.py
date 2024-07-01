from django import forms
import django_filters

from .models import Project, Technologies


class ProjectsFilter(django_filters.FilterSet):

    class Meta:
        model = Project
        fields = [
            'technologies_id',
        ]
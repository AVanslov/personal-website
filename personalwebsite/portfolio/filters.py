import django_filters
from django import forms

from .models import Project, Technology


class ProjectsFilter(django_filters.FilterSet):

    technologies_id = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Technology.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Project
        fields = (
            'technologies_id',
        )

from django import forms
import django_filters

from .models import Project, Technologies


class ProjectsFilter(django_filters.FilterSet):

    technologies_id = django_filters.filters.ModelMultipleChoiceFilter(
        # field_name='technologies_id__name',
        # to_field_name='name',
        queryset=Technologies.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    # name = django_filters.CharFilter(
    #     widget=forms.TextInput(
    #         attrs={'style': 'width: 20px', 'class': 'form-select form-select-sm'}
    #     )
    # )

    class Meta:
        model = Project
        fields = (
            # 'name',
            'technologies_id',
        )

from typing import Any
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Project, Technology


class PortfolioListView(ListView):
    model = Project
    ordering = '-pub_date'
    template_name = 'portfolio/project_list.html'
    context_object_name = 'page_obj'

    def get_queryset(self):
        queryset = {'projects': Project.objects.order_by('-pub_date').all(),
                    'technologies': Technology.objects.all()}
        return queryset


class PortfolioDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'


class CategoryProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'page_obj'

    def get_technology(self):
        return get_object_or_404(
            Technology,
            slug=self.kwargs['category_slug']
        )

    def get_queryset(self):
        queryset = {'projects': self.get_technology().projects.all(),
                    'technologies': Technology.objects.all()}
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['technology'] = self.get_technology()
        return context

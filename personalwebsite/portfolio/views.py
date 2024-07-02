from typing import Any
from django.views.generic import ListView

from .filters import ProjectsFilter

from .models import Project, Technologies


class PortfolioListView(ListView):
    model = Project
    ordering = '-pub_date'
    template_name = 'portfolio/project_list.html'
    paginate_by = 12
    filterset_class = ProjectsFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

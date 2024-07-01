from django.views.generic import ListView

from .filters import ProjectsFilter

from .models import Project, Technologies


class PortfolioListView(ListView):
    model = Project
    ordering = '-pub_date'
    template_name = 'portfolio/project_list.html'
    paginate_by = 12
    filterset_class = ProjectsFilter

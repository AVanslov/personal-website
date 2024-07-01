from django.views.generic import ListView

from .filters import ProjectsFilter

from .models import Project, Technologies


class PortfolioListView(ListView):
    model = Project
    ordering = 'pub_date'
    template_name = 'portfolio/project_list.html'
    context_object_name = 'page_obj'
    # paginate_by = 12
    # filterset_class = ProjectsFilter

    def get_queryset(self):
        queryset = {
            'all_technologies': Technologies.objects.all(),
            'all_projects': Project.objects.all()}
        return queryset

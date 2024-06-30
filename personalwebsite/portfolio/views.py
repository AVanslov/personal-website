from django.views.generic import ListView

from .models import Project


class PortfolioListView(ListView):
    model = Project
    ordering = 'pub_date'
    paginate_by = 8

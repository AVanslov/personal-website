import markdown
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Project, Technology


class PortfolioListView(ListView):
    model = Project
    ordering = '-pub_date'
    template_name = 'portfolio/project_list.html'
    context_object_name = 'page_obj'

    def get_queryset(self):
        queryset = {'projects': Project.objects.order_by('-pub_date'),
                    'technologies': Technology.objects.order_by('name')}
        return queryset


class PortfolioDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'

    def get_project(self):
        return get_object_or_404(
            Project,
            id=self.kwargs['pk']
        )

    def converter_to_markdown_content(self):
        post = self.get_project()
        md = markdown.Markdown(extensions=["fenced_code", "tables"])
        post.body_text = md.convert(post.body_text)
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.converter_to_markdown_content()
        return context


class CategoryProjectListView(ListView):
    model = Project
    ordering = '-pub_date'
    template_name = 'portfolio/project_list.html'
    context_object_name = 'page_obj'

    def get_technology(self):
        return get_object_or_404(
            Technology,
            slug=self.kwargs['category_slug']
        )

    def get_queryset(self):
        queryset = {
            'projects': self.get_technology().projects.all(),
            'technologies': Technology.objects.order_by('name')}
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['technology'] = self.get_technology()
        return context

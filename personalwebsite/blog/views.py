from django.views.generic import ListView, DetailView

from .models import Post, Category


class PostListView(ListView):
    model = Post
    ordering = '-pub_date'
    paginate_by = 8
    template_name = 'portfolio/project_list.html'


class PostDetailView(DetailView):
    model = Post

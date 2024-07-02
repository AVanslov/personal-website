from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    ordering = '-pub_date'
    paginate_by = 8
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = Post

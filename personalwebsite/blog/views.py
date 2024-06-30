from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post
    ordering = 'pub_date'
    paginate_by = 8
    template_name = 'portfolio/project_list.html'

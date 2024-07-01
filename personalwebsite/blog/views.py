from django.views.generic import ListView, DetailView

from .models import Post, Category


class PostListView(ListView):
    model = Post
    ordering = 'pub_date'
    # paginate_by = 8
    template_name = 'portfolio/project_list.html'
    context_object_name = 'page_obj'

    def get_queryset(self):
        queryset = {
            'all_technologies': Category.objects.all(),
            'all_projects': Post.objects.all()}
        return queryset


class PostDetailView(DetailView):
    model = Post

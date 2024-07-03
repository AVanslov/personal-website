import markdown

from django.views.generic import ListView, DetailView

from .models import (
    Category,
    Post,
)


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'page_obj'

    def converter_to_markdown_content(self):
        md = markdown.Markdown(extensions=["fenced_code"])
        all_posts = []
        for post in Post.objects.order_by('pub_date').all():
            post.text = md.convert(post.text)
            all_posts.append(post)
        return all_posts

    def get_queryset(self):
        queryset = {'posts': self.converter_to_markdown_content(),
                    'categories': Category.objects.order_by('name').all()}
        return queryset


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['posts'] = self.converter_to_markdown_content()
    #     return context


class PostDetailView(DetailView):
    model = Post

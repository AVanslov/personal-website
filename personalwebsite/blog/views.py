from django.shortcuts import get_object_or_404
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

    def converter_to_markdown_content(self, posts):
        md = markdown.Markdown(extensions=["fenced_code"])
        all_posts = []
        for post in posts:
            post.text = md.convert(post.text)
            all_posts.append(post)
        return all_posts

    def get_queryset(self):
        queryset = {'posts': self.converter_to_markdown_content(
            posts=Post.objects.order_by('pub_date').all()
        ),  # добавить пагинацию
                    'categories': Category.objects.order_by('name').all()}
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_post(self):
        return get_object_or_404(
            Post,
            id=self.kwargs['pk']
        )

    def converter_to_markdown_content(self):
        post = self.get_post()
        md = markdown.Markdown(extensions=["fenced_code"])
        post.text = md.convert(post.text)
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.converter_to_markdown_content()
        return context


class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'page_obj'

    def converter_to_markdown_content(self, posts):
        md = markdown.Markdown(extensions=["fenced_code"])
        all_posts = []
        for post in posts:
            post.text = md.convert(post.text)
            all_posts.append(post)
        return all_posts

    def get_category(self):
        return get_object_or_404(
            Category,
            slug=self.kwargs['category_slug']
        )

    def get_queryset(self):
        queryset = {
            'posts': self.converter_to_markdown_content(
                posts=self.get_category().posts.all()
            ),
            'categories': Category.objects.all()
        }
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_category()
        return context

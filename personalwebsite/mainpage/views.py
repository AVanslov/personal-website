from django.shortcuts import render

from blog.models import Post
from portfolio.models import Project


def main_page(request):
    projects = Project.objects.all().order_by('-pub_date')[1:5]
    posts = Post.objects.all().order_by('-pub_date')[1:5]

    context = {
        'projects': projects,
        'posts': posts,
    }
    return render(request, 'homepage/main.html', context)

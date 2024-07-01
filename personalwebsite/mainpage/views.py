from django.shortcuts import render

from blog.models import Post
from portfolio.models import Project, Technologies


def main(request):
    projects = Project.objects.all().order_by('-pub_date')[0:5]
    posts = Post.objects.all().order_by('-pub_date')[0:5]
    technologies = Technologies.objects.all()

    context = {
        'projects': projects,
        'posts': posts,
        'technologies': technologies
    }
    return render(request, 'homepage/main.html', context)

# написать функцию, которая будет отправлять резюме в pdf

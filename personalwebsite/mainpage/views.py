import markdown
from django.shortcuts import get_object_or_404, render

from blog.models import Post
from portfolio.models import Project, Technology

from .models import Resume


def converter_to_markdown_content(resume):
    md = markdown.Markdown(extensions=["fenced_code"])
    resume.text = md.convert(resume.text)
    return resume


def main(request):
    projects = Project.objects.order_by('-pub_date')[:5]
    posts = Post.objects.order_by('-pub_date')[:5]
    technologies = Technology.objects.order_by('name')
    resume = converter_to_markdown_content(
        resume=get_object_or_404(Resume, id=1)
    )

    context = {
        'projects': projects,
        'posts': posts,
        'technologies': technologies,
        'resume': resume
    }
    return render(request, 'homepage/main.html', context)

# написать функцию, которая будет отправлять резюме в pdf

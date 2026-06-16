from django.http import Http404
from django.shortcuts import redirect, render

from .models import Resume


def home(request):
    from portfolio.models import Project
    featured = Project.objects.filter(featured=True)
    return render(request, 'pages/home.html', {'featured': featured})

def about(request):
    from portfolio.models import Project
    projects = Project.objects.all()
    skill_set = set()
    for project in projects:
        for tech in project.tech_list():
            skill_set.add(tech.strip())
    skills = sorted(skill_set)
    return render(request, 'pages/about.html', {'skills': skills})

def contact(request):
    return render(request, 'pages/contact.html')

def resume(request):
    latest = Resume.objects.first()
    if not latest:
        raise Http404("No resume uploaded")
    return redirect(latest.file.url)

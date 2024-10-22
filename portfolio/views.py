from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
import os
from django.conf import settings
from .models import Banner, Project


def home(request):
    banner = get_object_or_404(Banner, page='home')
    context = {
        'projects': projects,
        'banner': banner,
    }
    return render(request, 'pages/home.html', context)


def about(request):
    banner = get_object_or_404(Banner, page='about')
    return render(request, 'pages/about.html', {'banner': banner})


def projects(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    banner = get_object_or_404(Banner, page='projects')
    context = {
        'projects': projects,
        'banner': banner,
    }
    return render(request, 'pages/projects.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    images = project.images.all()
    return render(request, 'pages/project_detail.html', {'project': project, 'images': images})


def skills(request):
    banner = get_object_or_404(Banner, page='skills')
    return render(request, 'pages/skills.html', {'banner': banner})


def contact(request):
    banner = get_object_or_404(Banner, page='contact')
    return render(request, 'pages/contact.html', {'banner': banner})


def download_cv(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'files/cv.pdf')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        raise Http404

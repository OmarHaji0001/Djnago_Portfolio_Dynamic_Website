from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
import os
from django.conf import settings
from .models import Banner


def home(request):
    banner = get_object_or_404(Banner, page='home')
    return render(request, 'pages/home.html', {'banner': banner})


def about(request):
    banner = get_object_or_404(Banner, page='about')
    return render(request, 'pages/about.html', {'banner': banner})


def projects(request):
    banner = get_object_or_404(Banner, page='projects')
    return render(request, 'pages/projects.html', {'banner': banner})


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

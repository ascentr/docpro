from django.shortcuts import render
from apps.projects.models import Project


def index(request):
  
  return render(request, 'index.html')
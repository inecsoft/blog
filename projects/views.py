from django.shortcuts import render
from projects.models import Project;

# Create your views here.
def  project_index(req):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(req, 'project_index.html', context)

def project_detail(req, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(req, 'project_detail.html', context)
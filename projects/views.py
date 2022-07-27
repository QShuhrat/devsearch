from django.shortcuts import render, redirect
from .models import Project, Tag
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
  
    context = {'projects': projects}
    return render(request, 'projects/project.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single project.html', {'project': projectObj,})

def CreateProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request,'projects/project_form.html',context)
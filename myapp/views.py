from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = 'Django course!!'
    return render(request, 'index.html', {
        "title": title
    })


def hello(request, username):
    return HttpResponse('<h1>Hello %s! :)</h1>' % username)


def about(request):
    return render(request, 'about.html', {
        "username": "Daniel Hernandez"
    })


def saveId(request, id):
    print(type(id))
    return HttpResponse('<h1>Your ID is saved: %s</h1>' % id)

# Return all data


def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects/projects.html', {
        "projects": projects
    })


def tasks(request):
    tasks = list(Task.objects.all())
    print(tasks)
    return render(request, 'tasks/tasks.html', {
        "tasks": tasks
    })

# Return by id


def getProject(request, id):
    project = get_object_or_404(Project, id=id)
    return HttpResponse('<h4>Your project: %s</h4>' % project.name)


def getTask(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse('<h4>Your task: %s</h4>' % task.title)

# Create


def createTask(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('tasks')


def createProject(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject
        })
    else:
        Project.objects.create(
            name=request.POST['name'])
        return redirect('projects')

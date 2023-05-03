from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('saveId/<int:id>', views.saveId, name='saveId'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('project/<int:id>', views.getProject, name='singleProject'),
    path('task/<int:id>', views.getTask, name='singleTask'),
    path('create-task/', views.createTask, name='createTask'),
    path('create-project/', views.createProject, name='createProject')
]

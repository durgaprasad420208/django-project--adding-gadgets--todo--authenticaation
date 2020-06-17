from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_home, name='todo-home'),
    path('todo/<int:id>', views.todo_retrive, name='todo-view'),
    path('todo/create', views.todo_create, name='todo-create'),
    path('todo/edit/<int:id>', views.todo_edit, name='todo-edit'),
    path('todo/delete/<int:id>', views.todo_delete, name='todo-delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/todo", views.add_todo, name="add-todo"),
    path("update/todo", views.update_todo, name="update-todo"),
    path("delete/todo/<int:todo_id>/", views.delete_todo, name="delete-todo")
    # path("update/todo", views.update_todo, name="update-todo"),
]

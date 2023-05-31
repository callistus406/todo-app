from django.urls import path
from . import views
from django.conf import settings
# from django.conf.urls.static import static
urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.fetch_all_todo, name="fetch-all-todo"),
    path("add/todo", views.add_todo, name="add-todo"),
    path("update/todo/<int:todo_id>/", views.update_todo, name="update-todo"),
    path("delete/todo/<int:todo_id>/", views.delete_todo, name="delete-todo"),
    path("fetch/todo/<int:todo_id>/", views.fetch_one_todo, name="fetch-todo")
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)

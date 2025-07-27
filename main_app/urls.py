from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("todos/", views.todo_index, name="todos-index"),
    path("todos/<int:todo_id>/", views.todo_detail, name="todo-detail"),
    path("todos/create/", views.TodoCreate.as_view(), name="todo-create"),
    path("todos/<int:pk>/update/", views.TodoUpdate.as_view(), name="todo-update"),
    path("todos/<int:todo_id>/toggle/", views.toggle_todo, name="toggle-todo"),
    path("todo/<int:pk>/delete/", views.TodoDelete.as_view(), name="todo-delete"),
    path("todos/<int:todo_id>/add-subtask/", views.add_subtask, name="add-subtask"),
    path(
        "subtasks/<int:subtask_id>/toggle/", views.toggle_subtask, name="toggle-subtask"
    ),
    path("subtasks/<int:pk>/update/", views.subtask_update, name="subtask-update"),
    path("subtasks/<int:pk>/delete/", views.subtask_delete, name="subtask-delete"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.signup, name="signup"),
    path("todos/completed/", views.completed_todos, name="completed-todos"),
]

# this file is for defining all the routes in manin_app. Because we configured the URLs in main_app and groovasana (/url.py), you only have to touch this one
## the url patterns list is where you specify each route, similar to routes grouped in controllers in express

from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('', views.home, name='home'), #defines root path and maps it to the view.home
    path('about/',views.about, name='about'),
    path('todos/', views.todo_index, name= 'todos-index'),
    path('todos/<int:todo_id>/', views.todo_detail, name='todo-detail'),
    path('todos/create/', views.TodoCreate.as_view(), name= 'todo-create'),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name="todo-update"),
    path('todo/<int:pk>/delete/', views.TodoDelete.as_view(), name ="todo-delete"),
]

#view function is similar to the route handler in express

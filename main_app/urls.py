from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/',views.about, name='about'),
    path('todos/', views.todo_index, name= 'todos-index'),
    path('todos/<int:todo_id>/', views.todo_detail, name='todo-detail'),
    path('todos/create/', views.TodoCreate.as_view(), name= 'todo-create'),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name="todo-update"),
    path('todo/<int:pk>/delete/', views.TodoDelete.as_view(), name ="todo-delete"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'), 
]

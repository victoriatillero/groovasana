from django.shortcuts import render
from .models import Todo
from django.views.generic.edit import CreateView
from .models import Todo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# # Create your views here.
# # Import HttpResponse to send text-based responses
# from django.http import HttpResponse - can remove because we're not using HttpResponse anymore

# Define the home view function
def home(request):
    # Send a simple HTML response
    # return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('<h1> About Groovasana </h1>')
    return render(request, 'about.html')

def todo_index(request):
    todos= Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})

def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todos/detail.html', {'todo': todo})

class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"

class TodoUpdate(UpdateView):
    model = Todo
    fields = ['day', 'priority', 'tags', 'esttime', 'description']

class TodoDelete(DeleteView):
    model = Todo
    success_url= '/todos/'

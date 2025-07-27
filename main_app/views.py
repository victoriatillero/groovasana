from django.shortcuts import render, redirect
from .forms import TodoForm, TodoCategoryForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def todo_index(request):
    todos= Todo.objects.filter(user=request.user)
    return render(request, 'todos/index.html', {'todos': todos})

def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        category_form = TodoCategoryForm(request.POST, instance=todo)
        if category_form.is_valid():
            category_form.save()
            return redirect('todo-detail', todo_id =todo.id)
    else:
        category_form = TodoCategoryForm(instance=todo)
    return render(request, 'todos/detail.html', {
        'todo': todo,
        'category_form':category_form
        })

class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm

class TodoDelete(DeleteView):
    model = Todo
    success_url= '/todos/'

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todos-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

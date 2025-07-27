from django.shortcuts import render, redirect
from .forms import TodoForm, TodoCategoryForm, SubtaskForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo, Subtask, Category
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def todo_index(request):
    todos= Todo.objects.filter(user=request.user, is_completed=False)
    category_name = request.GET.get('category')
    if category_name:
        todos = todos.filter(category__name=category_name)

    categories= Category.objects.all()
    return render(request, 'todos/index.html',{'todos': todos,'categories': categories})

@login_required
def completed_todos(request):
    todos= Todo.objects.filter(user=request.user, is_completed=True)
    return render(request, 'todos/completed.html', {'todos': todos})
def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        category_form = TodoCategoryForm(request.POST, instance=todo)
        if category_form.is_valid():
            category_form.save()
            return redirect('todo-detail', todo_id =todo.id)
    else:
        category_form = TodoCategoryForm(instance=todo)

    subtask_form = SubtaskForm()

    return render(request, 'todos/detail.html', {
        'todo': todo,
        'category_form':category_form,
        'subtask_form': subtask_form,
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

def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('todos-index')

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

def add_subtask(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = SubtaskForm(request.POST)
        if form.is_valid():
            new_subtask = form.save(commit=False)
            new_subtask.todo = todo
            new_subtask.save()
    return redirect('todo-detail', todo_id=todo.id)

def toggle_subtask(request, subtask_id):
    subtask = Subtask.objects.get(id=subtask_id)
    subtask.is_completed = not subtask.is_completed
    subtask.save()
    return JsonResponse({'completed':subtask.is_completed})


def subtask_update(request, pk):
    subtask= get_object_or_404(Subtask, pk=pk)

    if request.method == 'POST':
        form = SubtaskForm(request.POST, instance=subtask)
        if form.is_valid():
            form.save()
            return redirect ('todo-detail', todo_id= subtask.todo.id)
    else:
            form = SubtaskForm(instance=subtask)

    return render(request, 'subtasks/update.html', {'form': form, 'subtask':subtask})

@login_required
def subtask_delete(request,pk):
    subtask = get_object_or_404(Subtask, pk=pk)
    todo_id = subtask.todo.id
    subtask.delete()
    return redirect ('todo-detail', todo_id=todo_id)

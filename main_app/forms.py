from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'description', 'day', 'priority', 'esttime', 'category']
        widgets = {
            'day': forms.DateInput(attrs={'type':'date'})
        }
class TodoCategoryForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['category']

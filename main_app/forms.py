from django import forms
from .models import Todo, Subtask


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["name", "description", "day", "priority", "esttime"]
        labels = {"esttime": "Estimated Time"}
        widgets = {
            "day": forms.DateInput(attrs={"type": "date"}),
            "esttime": forms.TextInput(attrs={"placeholder": "hh:mm:ss"}),
        }


class TodoCategoryForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["category"]


class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ["name", "is_completed"]

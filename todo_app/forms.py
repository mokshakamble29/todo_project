from django import forms
from todo_app.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter task...', 'class': 'task-input'})
        }
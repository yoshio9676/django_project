from django import forms
from .models import TodoModel

class DateInput(forms.DateInput):
    input_type = 'date'

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ('title', 'memo', 'priority', 'duedate')
        widgets = {
            'duedate': DateInput()
        }
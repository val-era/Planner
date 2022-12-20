from .models import Tasks
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields=['title', 'task', 'teg', 'date', 'is_global', 'global_task']
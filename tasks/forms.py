
from django.forms import ModelForm
from tasks.models import Tasks


class newTask(ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_id', 'task_name', 'client', 'start_date', 'end_date', 'status', 'owner']





from django.forms import ModelForm
from tasks.models import Tasks, AccountTask


class newTask(ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_id', 'task_name', 'client', 'start_date', 'end_date', 'status', 'owner']


class user_edit_form(ModelForm):
    class Meta:
        model = AccountTask
        fields = ['time', 'user_status']


class manager_edit_task_form(ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_name', 'client', 'start_date', 'end_date', 'status', 'owner']



from django.contrib import admin

from tasks.models import Tasks

# class TasksAdmin(admin.ModelAdmin):
#     fields = ('task_id', 'task_name', 'client', 'start_date', 'end_date', 'status', 'owner')

admin.site.register(Tasks)


    
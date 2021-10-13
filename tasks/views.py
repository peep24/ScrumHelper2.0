from django.shortcuts import render, redirect
from tasks.models import Tasks, AccountTask
from django.views.decorators.http import require_http_methods
from tasks.forms import newTask
from personal.views import home_screen_view

# @require_http_methods(["POST"])
def create_task_view(request, *args, **kwargs):

    if request.POST:
        print("post triggered")
        form = newTask(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            # form.save()
        
        else:
            form = newTask()
            print("not valid")
    else: form= newTask()
    return render(request, 'new_task.html', {'form': form})



def view_all_tasks(request):
	context = {}
	if request.user.is_authenticated:
		
		context['obj'] = Tasks.objects.all()

	return render(request, "all_tasks.html", context)



def join_task(request, id):

    task = Tasks.objects.filter(task_id=id)
    entry = AccountTask()
    for i in task:
        entry.task_id = i
        entry.account_id = request.user
        entry.save()
        return redirect(home_screen_view)

    
from django.shortcuts import render
from tasks.models import Tasks
from django.views.decorators.http import require_http_methods
from tasks.forms import newTask


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
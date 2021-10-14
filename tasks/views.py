from django.shortcuts import render, redirect
from tasks.models import Tasks, AccountTask
from django.views.decorators.http import require_http_methods
from tasks.forms import newTask, user_edit_form
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
            return redirect(home_screen_view)
        
        else:
            print(form.errors)
            # form = newTask()
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


def delete_task_connection(request, id):
    connection = AccountTask.objects.filter(task_id=id, account_id=request.user)
    connection.delete()
    # return render(request, "delete_task_connection.html")
    return redirect(home_screen_view)



def user_edit_task(request, id, *args, **kwargs):
    
    if request.POST:
        form = user_edit_form(request.POST)

        if form.is_valid():

            # instance = form.save(commit=False)
            accountTask = AccountTask.objects.filter(task_id=id)
            for i in accountTask:
                i.time = form['time'].value()
                i.user_status = form['user_status'].value()
                i.save()

            return redirect(home_screen_view)
        
        else:
            print("not valid")

    else: form= user_edit_form()




    return render(request, "user_edit_task.html", {'form': form})
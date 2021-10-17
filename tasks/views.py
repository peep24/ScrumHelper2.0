from django.shortcuts import render, redirect
from tasks.models import Tasks, AccountTask
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import user_passes_test
from tasks.forms import newTask, user_edit_form, manager_edit_task_form
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
            accountTaskObj = AccountTask.objects.filter(task_id=id)
          
            for i in accountTaskObj:
                print("iteration")
                i.time = form['time'].value()
                i.user_status = form['user_status'].value()
                i.save()

            return redirect(home_screen_view)
        
        else:
            print("not valid")

    else: form= user_edit_form()

    return render(request, "user_edit_task.html", {'form': form})



@user_passes_test(lambda u: u.is_staff, login_url='/permission_not_granted/')
def manager_edit_task(request, id, *args, **kwargs):
    
    if request.POST:
        form = manager_edit_task_form(request.POST)

        if form.is_valid():

            TaskObj = Tasks.objects.get(task_id=id)


            TaskObj.task_name = form['task_name'].value()
            TaskObj.client = form['client'].value()

            TaskObj.start_date = form['start_date'].value()
            TaskObj.end_date = form['end_date'].value()
            TaskObj.status = form['status'].value()
            
            TaskObj.owner = form['owner'].value()

            TaskObj.save()

            return redirect(home_screen_view)
        
        else:
            print("not valid")

    else: 
        TaskObj = Tasks.objects.get(task_id=id)
        form= manager_edit_task_form(initial={
            'task_id': TaskObj.task_id,
            'task_name': TaskObj.task_name,
            'client': TaskObj.client,
            'start_date': TaskObj.start_date,
            'end_date': TaskObj.end_date,
            'status': TaskObj.status,
            'owner': TaskObj.owner,
            })

    return render(request, "manager_edit_task.html", {'form': form})
from django.shortcuts import render
from tasks.models import AccountTask, Tasks 

def home_screen_view(request):
	context = {}
	if request.user.is_authenticated:
		
		user = request.user
		task_ids = AccountTask.objects.filter(account_id=user).values_list('task_id', flat=True).order_by('id')
		context['obj'] = {}
		for i in task_ids:
			appendee = Tasks.objects.filter(task_id=i)
			context['obj'][i] = appendee
	return render(request, "personal/home.html", context)




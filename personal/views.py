from django.shortcuts import render
from tasks.models import AccountTask, Tasks 

def home_screen_view(request):
	context = {}
	if request.user.is_authenticated:
		
		user = request.user
		# task_ids = AccountTask.objects.filter(account_id=user).values_list('task_id', flat=True).order_by('id')
		qs = AccountTask.objects.filter(account_id=user)
		task_ids = 	qs.values_list('task_id', flat=True).order_by('id')

		context['obj'] = {}
		for i in task_ids:
			appendee = Tasks.objects.filter(task_id=i)
			context['obj'][i] = appendee

		context['link'] = {}
		index = 0
		for j in qs:
			context['link'][index] = j
			index+=1


	return render(request, "personal/home.html", context)




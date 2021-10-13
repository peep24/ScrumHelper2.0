from django.shortcuts import render
from tasks.models import Tasks 

def home_screen_view(request):
	context = {}
	if request.user.is_authenticated:
		
		user = request.user
		context['obj'] = Tasks.objects.filter(created_by=user)
		print(user)

	return render(request, "personal/home.html", context)




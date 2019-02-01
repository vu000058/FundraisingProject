from django.shortcuts import render
from tasksapp.models import Task, Section
from django.utils import timezone
from django.shortcuts import redirect

# request where the parts of the database from models.py are used
#first if for the GET that orders all the tasks by due date, default page
#elif has the POST where it creates the user input and stores it in the db
def index(request):
	if request.method == 'GET':
		objects = Task.objects.all().order_by('duedate')
		return render(request, "index.html", {'tasks':objects})
	elif request.method == 'POST':
		eventName = request.POST.get("eventName","")
		taskName = request.POST.get("task","")
		taskDesc = request.POST.get("desc","")
		assignedTo = request.POST.get("assignee","")
		date = request.POST.get("duedate","")
		reporterName = request.POST.get("reporter","")
		state = request.POST.get("status","")
		record = Task(event=eventName, name=taskName, description=taskDesc, assignee=assignedTo, duedate = date,
					reporter = reporterName, status = state,
					updatedate = timezone.now())
		record.save()
		return redirect('/')
#delete a task
def delete(request, taskId):
	record = Task(id=taskId)
	record.delete()
	return redirect('/')
#edit the tasks
def edit(request, taskId):
	task = Task.objects.get(id=taskId)
	return render(request, "update.html", {'task':task})
#when you go into the edit, the update is done here
def update(request, taskId):
	task = Task.objects.get(id=taskId)
	task.event = request.POST.get("eventName","")
	task.name = request.POST.get("task","")
	task.description = request.POST.get("desc","")
	task.assignee = request.POST.get("assignee","")
	task.duedate = request.POST.get("duedate","")
	task.reporter = request.POST.get("reporter","")
	task.status = request.POST.get("status","")
	task.updatedate = timezone.now()
	task.save()
	return redirect('/')
#search function for when you want to search by event name, task, assignee, duedate etc
def search(request):
	eventName = request.POST.get("eventName")
	taskName = request.POST.get("task")
	assignedTo = request.POST.get("assignee")
	date = request.POST.get("duedate")
	state = request.POST.get("status")
	objects = Task.objects.all()
	if eventName.strip():
		objects = objects.filter(event__icontains=eventName)
	if taskName.strip():
		objects = objects.filter(name__icontains=taskName)
	if assignedTo.strip():
		objects = objects.filter(assignee__icontains=assignedTo)
	if state.strip():
		objects = objects.filter(status=state)
	return render(request, "index.html", {'tasks':objects.order_by('duedate')})


def sections(request):
	if request.method == 'GET':
		return render(request, "section.html", {'sections': Section.objects.all()})
	elif request.method == 'POST':
		sectionName = request.POST.get("sectionName", "")
		section = Section(name=sectionName)
		section.save()
		return redirect('/sections/')

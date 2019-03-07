from django.shortcuts import render
from fundraiser.models import Event
from django.utils import timezone
from django.shortcuts import redirect

#function to get the goal set for the event
def getGoal(events) :
	goal = 0
	if events:
		for x in events:
			goal=x.eventGoal;
			break;
	return goal;

#function to get the total funds
def getTotalFunds(events) :
	total = 0;
	for x in events:
		total=total + float(x.eventAmount);
	return total;
#same idea as the webapp db views.py file. has info for the fundraiser
def index(request):
	if request.method == 'GET':
		objects = Event.objects.all().order_by('eventCreated')
		return render(request, "fundraiser.html", {'events':objects, 'goal':getGoal(objects), 'totalFunds':getTotalFunds(objects)})
	elif request.method == 'POST':
		eventName = request.POST.get("eventName","")
		eventDescription = request.POST.get("eventDescription","")
		eventAmount = request.POST.get("eventAmount","")
		eventGoal = request.POST.get("eventGoal", "")
		record = Event(eventName=eventName, eventDescription=eventDescription, eventAmount=eventAmount,
					   eventGoal=eventGoal,eventCreated = timezone.now())
		record.save()
		return redirect('/fundraiser')


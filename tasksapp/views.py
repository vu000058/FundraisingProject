from django.shortcuts import render
from tasksapp.models import Task, Section, UserProfile, Goal, Event
from django.utils import timezone
from django.shortcuts import redirect
from .forms import SectionForm, RegistrationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.urls import reverse
import uuid
# request where the parts of the database from models.py are used
#first if for the GET that orders all the tasks by due date, default page
#elif has the POST where it creates the user input and stores it in the db
def index(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('due_date')
        return render(request, "index.html", {'tasks': tasks})

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


def add_edit_task(request, id=0):
    if request.method == "GET":
        task = Task.objects.get(id=id) if id > 0 else Task()
        sections = Section.objects.all()
        return render(request, "update.html", {'task': task, 'sections': sections})
    else:
        event = request.POST.get("eventName", "")
        name = request.POST.get("task", "")
        description = request.POST.get("desc", "")
        assignee = request.POST.get("assignee", "")
        due_date = request.POST.get("duedate", "")
        # creator = request.POST.get("reporter", "")
        status = request.POST.get("status", "")
        update_date = timezone.now()

        if id > 0:
            task = Task.objects.get(id=id)
            task.event = event
            task.name = name
            task.description = description
            # task.assignee = request.POST.get("assignee", "")
            task.due_date = assignee
            # task.creator = request.user
            task.status = status
            task.update_date = timezone.now()
            task.save()
        else:
            task = Task(
                event=event,
                name=name,
                description=description,
                status=status
            )
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
        section = SectionForm()
        return render(request, "section.html", {'sections': Section.objects.all(), 'form': section})
    elif request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SectionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            term = form.cleaned_data['term']
            year = form.cleaned_data['year']
            section = Section(name=name, term=term, year=year)
            section.save()
        return redirect('/sections')


def delete_section(request, id):
    Section.objects.get(id=id).delete()
    return redirect('/sections')


def users(request):
    return render(request, "users.html", {'users': UserProfile.objects.all()})


def goals(request):
    if request.method == "POST":
        amount = request.POST.get("amount", "")
        note = request.POST.get("note", "")
        section = request.POST.get("section")
        goal = Goal(amount=amount, note=note, section=Section.objects.get(id=section))
        goal.save()

    return render(request, "goals.html", {'goals': Goal.objects.all(),
                                          'sections': Section.objects.all()})


def goal_details(request, id):
    goal = Goal.objects.get(id=id)

    if request.method == 'GET':
        events = Event.objects.all()
        return render(request, "fundraiser.html", {'events': events, 'goal': goal})
    elif request.method == 'POST':
        event_name = request.POST.get("name", "")
        event_description = request.POST.get("description", "")
        raised_amount = request.POST.get("raised_amount", "")
        deducted_amount = request.POST.get("deducted_amount", "")
        event = Event(
            goal=goal,
            name=event_name,
            description=event_description,
            raised_amount=raised_amount,
            deducted_amount=deducted_amount
        )
        event.save()

        return redirect('/fundraiser')


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            email.strip()
            user = User(
                username=username,
                email=email,
                is_active=True,
                is_staff=True
            )
            user.set_password(password)
            user.save()
            token = uuid.uuid4()
            profile = UserProfile(user=user, name=name, activation_code=token)
            profile.save()
            url = request.build_absolute_uri(
                '/activate?email=%s&code=%s' % (email, token)
            )
            try:
                message = EmailMessage(
                    'FAM1255 Account Activation',
                    'Please click on the link bellow to activate your account:\n' + url,
                    to=[email])
                message.send()
            except Exception:
                pass
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def activate(request):
    email = request.GET['email']
    code = request.GET['code']
    user = User.objects.filter(email=email).first()
    if not user or user.profile.activation_code != code:
        return render(request, 'accountactivation.html')

    user.is_active = True
    user.save()
    return render(request, 'accountactivation.html')


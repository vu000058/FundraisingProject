from django.shortcuts import render
from tasksapp.models import Task, Section, UserProfile, Goal, Event
from django.utils import timezone
from django.shortcuts import redirect
from .forms import SectionForm, RegistrationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.urls import reverse
import uuid


task_statuses = ["Unassigned", "Assigned", "Ongoing", "On Hold", "Cancelled", "Finished"]
# request where the parts of the database from models.py are used
#first if for the GET that orders all the tasks by due date, default page
#elif has the POST where it creates the user input and stores it in the db

def index(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('due_date')
        return render(request, "index.html", {'tasks': tasks, 'statuses': task_statuses})


def delete_task(request, id):
    Task.objects.get(id=id).delete()
    return redirect('/')


def add_edit_task(request, id=0):
    if request.method == "GET":
        task = Task.objects.get(id=id) if id > 0 else Task()
        sections = Section.objects.all()
        users = User.objects.all()
        print(task.__dict__)
        return render(request, "update.html", {
            'task': task,
            'sections': sections,
            'users': users,
            'taskId': id,
            'statuses': task_statuses})
    else:
        event = request.POST.get("eventName", "")
        name = request.POST.get("task", "")
        description = request.POST.get("desc", "")
        assignee = request.POST.get("assignee", "")
        due_date = request.POST.get("duedate", "")
        # creator = request.POST.get("reporter", "")
        status = request.POST.get("status", "")
        section = Section.objects.get(id=request.POST.get("section"))
        update_date = timezone.now()

        if id > 0:
            task = Task.objects.get(id=id)
            task.event = event
            task.name = name
            task.description = description
            # task.assignee = request.POST.get("assignee", "")
            task.due_date = due_date
            task.status = status
            task.update_date = timezone.now()
            task.save()
        else:
            task = Task(
                event=event,
                name=name,
                description=description,
                status=status,
                creator=request.user,
                section=section,
                due_date=due_date
            )
            task.save()

        return redirect('/')



#search function for when you want to search by event name, task, assignee, duedate etc
def search(request):
    eventName = request.POST.get("eventName")
    taskName = request.POST.get("task")
    assignedTo = request.POST.get("assignee")
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
    return render(request, "index.html", {'tasks': objects.order_by('due_date'), 'statuses': task_statuses})


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
    return render(request, "users.html", {'user_profiles': UserProfile.objects.all()})


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


def create_test_users():
    for num in range(1, 5):
        try:
            user = User(
                username='student' + str(num),
                is_staff=True,
                is_active=True
            )
            user.set_password('password')
            user.save()
            profile = UserProfile(name='Student ' + str(num), user=user)
            profile.save()
        except Exception:
            pass

    try:
        user = User(
            username='instructor',
            is_staff=True,
            is_active=True
        )
        user.set_password('password')
        user.save()
        profile = UserProfile(name='Student ' + str(num), user=user, is_instructor=True)
        profile.save()
    except Exception:
        pass


def activate_user(request, id):
    user = UserProfile.objects.get(id=id).user
    user.is_active = True
    user.save()

    return redirect('/users')


def deactivate_user(request, id):
    user = UserProfile.objects.get(id=id).user
    user.is_active = False
    user.save()

    return redirect('/users')

create_test_users()



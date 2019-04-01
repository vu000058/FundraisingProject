from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    term = models.CharField(max_length=10)
    event = models.CharField(max_length=100)
    event_due = models.DateField(null=True)
    agency = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s %s' % (str(self.year), str(self.term), self.name)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    section = models.ForeignKey(Section, related_name='users', null=True, on_delete=models.SET_NULL)
    is_instructor = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    activation_code = models.CharField(max_length=100, null=True)


class Task(models.Model):
    section = models.ForeignKey(Section, related_name='tasks', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, null=True, related_name='tasks_created', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    assignee = models.ForeignKey(User, related_name='tasks_assigned', null=True, on_delete=models.SET_NULL)
    due_date = models.DateField(null=True)
    delegator = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=20)
    update_date = models.DateField(auto_now_add=True)


class FundraisingGoal(models.Model):
    section = models.ForeignKey(Section, related_name='goals', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=500)


class Donation(models.Model):
    goal = models.ForeignKey(FundraisingGoal, related_name='events', on_delete=models.CASCADE)
    task_name = models.CharField(max_length=150)
    description = models.CharField(max_length=500, null=True)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    deducted_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_date = models.DateField(auto_now_add=True)





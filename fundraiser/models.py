from django.db import models

#schema of the fundraiser db
class Event(models.Model):
	eventName = models.CharField(max_length=150)
	eventDescription = models.CharField(max_length=500, default='No Description Available')
	eventAmount = models.CharField(max_length=10,default ='0')
	eventGoal = models.CharField(max_length=10,default ='0')
	eventCreated = models.DateField(auto_now_add=True)

	class Meta:
		db_table = "eventsdb"
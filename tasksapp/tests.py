from django.test import TestCase
from tasksapp.models import Task
from tasksapp.views import update
from tasksapp.views import delete
from tasksapp.views import search
from django.utils import timezone
from django.http import HttpRequest
from django.test import SimpleTestCase


# Create your tests here.

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(event="General Event", name="Fundraising Task", description="Collect money for an event",
                            assignee="Bob", duedate="2018-12-30", reporter="Alice", status="Assigned",
                            updatedate=timezone.now())
        Task.objects.create(event="Social Event", name="Decorate Hall", description="Organize event and food",
                            assignee="Alice", duedate="2018-11-29", reporter="Alex", status="Ongoing",
                            updatedate=timezone.now())

    def test_update_task(self):
        task = Task.objects.get(event="Social Event")
        self.assertEqual(task.name, "Decorate Hall")
        request = HttpRequest()
        request.method = 'POST'
        request.POST["eventName"] = "Old age people event"
        request.POST["task"] = "decorate their houses"
        request.POST["duedate"] = "2018-12-31"
        update(request, task.id)
        self.assertEqual(task.name, "Decorate Hall")

    def test_delete_task(self):
        task = Task.objects.get(event="General Event")
        self.assertEqual(len(Task.objects.all()), 2)
        delete(request=None, taskId=task.id)
        self.assertEqual(len(Task.objects.all()), 1)


class IndexTests(SimpleTestCase):
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1 class="h2">Fundraising Tasks Management</h1>')

    def test_about_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')



# #Test Models
#
# class ModelTest(TestCase):
#     @classmethod
#     # Set up non-modified objects used by all test methods
#     def setUpTestData(cls):
#         Task.objects.create(event="General Event", name="Fundraising Task", description="Collect money for an event",
#                             assignee="Bob", duedate="2018-12-30", reporter="Alice", status="Assigned",
#                             updatedate=timezone.now())
#     # Test for description length
#     def test_description_max_length(self):
#         task = Task.objects.get(id=1)
#         max_length = task._meta.get_field('description').max_length
#         self.assertEquals(max_length, 300)
#
#     # Test for Due date >= today's date
#
#     def test_duedate_greater_than_today(self):
#         task = Task.objects.get(id=1)
#         today = datetime.date.today()
#         if today > task._meta.get_field('duedate'):
#             print ("duedate can't be the past")
#         else:
#             print ("right duedate")

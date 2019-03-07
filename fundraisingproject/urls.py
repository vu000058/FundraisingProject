"""fundraisingproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webapp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('login/', views.log_in, 'log_in'),
    path('signup/', views.sign_up, name='signup'),
    path('activate/', views.activate, name='activate'),
    path('delete_task/<int:id>', views.delete_task, name='deleteTask'),
    path('addedit/<int:id>', views.add_edit_task, name='addEditTask'),
    path('search/', views.search, name='searchTask'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('fundraiser/', include('fundraiser.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('sections/', views.sections, name='sections'),
    path('delete_section/<int:id>', views.delete_section, name='delete_section'),
    path('goals/', views.goals, name='goals'),
    path('goal_details/<int:id>', views.goal_details, name='goal_details'),
    path('users/', views.users, name='users'),
    path('activate_user/<int:id>', views.activate_user, name='activate_user'),
    path('deactivate_user/<int:id>', views.deactivate_user, name='deactivate_user'),
    path('delete_user/<int:id>', views.delete_user, name='delete_user'),
    path('set_user_section/', views.set_user_section, name='set_user_section'),
    path('set_user_role/', views.set_user_role, name='set_user_role'),
    path('delete_event/<int:id>', views.delete_event, name='delete_event'),
    path('change_password/', views.change_password, name='change_password'),
    path('add_edit_section/<int:id>', views.add_edit_section, name='add_edit_section'),
    path('add_edit_goal/<int:id>', views.add_edit_goal, name='add_edit_goal'),
    path('assignees/', views.assignees, name='assignees'),
    path('delete_goal/<int:id>', views.delete_goal, name='delete_goal')
]

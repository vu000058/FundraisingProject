"""mytasks URL Configuration

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
from tasksapp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('delete/<int:taskId>', views.delete, name='removeTask'),
    path('edit/<int:taskId>', views.edit, name='editTask'),
    path('update/<int:taskId>', views.update, name='updateTask'),
    path('search/', views.search, name='searchTask'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('fundraiser/', include('fundraiser.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('sections/', views.sections, name='sections')
]

from django.urls import path

from fundraiser import views

urlpatterns = [
    path('', views.index, name='fundraiser'),
    # path('', views.index, name='fundraiser')
]
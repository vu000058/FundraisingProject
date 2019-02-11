from django.urls import path

from . import views

urlpatterns = [

    path('signup2/', views.SignUp.as_view(), name='signup2'),

    path('password/', views.change_password, name='changepassword'),
]
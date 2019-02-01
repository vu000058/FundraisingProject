from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('signup2/', views.SignUp.as_view(), name='signup2'),
    path('activate/', views.activate, name='activate'),
    path('password/', views.change_password, name='changepassword'),
]
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [

    path('signup2/', views.SignUp.as_view(), name='signup2'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('password/', views.change_password, name='changepassword'),
]
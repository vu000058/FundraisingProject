from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .forms import ChangePasswordForm, RegistrationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.urls import reverse

#signup view
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            valid_password = request.user.check_password(form.data['current_password'])
            if valid_password:
                user.set_password(form.data['new_password'])
            else:
                messages.success(request, 'Usuario actualizado exitosamente.')
            return render(request, 'changepassword.html')
            # return HttpResponseRedirect(reverse('home:listar_usuarios'))
    else:
        form = ChangePasswordForm()
    context = {
        'form': form,
    }
    return render(request, 'changepassword.html', context)
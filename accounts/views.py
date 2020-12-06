from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            user.save()
            return HttpResponseRedirect(reverse('requests'))
        else:
            return render(request, 'accounts/register.html', context={'form': form})
    else:
        return render(request, 'accounts/register.html', context={'form': RegistrationForm()})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

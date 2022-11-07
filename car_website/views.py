from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def login(request):
    return render(request, 'login.html')

def register(request):
    #form = UserCreationForm()
    if request.method=="POST":
        if request.POST.get('password1')==request.POST.get('password2'):
            try:
                saveuser=User.objects.create.user(request.POST.get('username'), password=request.POST.get('password1'))
                saveuser.save()
                return render(request, 'register.html', {'form': UserCreationForm(), 'info': 'The User '+request.POST.get('username')+ 'is saved successfully'})
            except:
                return render(request, 'register.html', {'form': UserCreationForm(), 'error': 'The User '+request.POST.get('username')+ 'is saved successfully'})
        else:
            return render(request, 'register.html', {'form': UserCreationForm(), 'error': 'Passwords Do Not Match'})
    else:
        return render(request, 'register.html', {'form': UserCreationForm})

class Profileview(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    print(request.user)
    return render(request, 'index.html')

#def forums(request):
    #return render(request, 'forums.html')


def used(request):
    return render(request, 'used.html')

def contact(request):
    return render(request, 'contact.html')


from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(response):
    form = UserCreationForm()
    return render(response, 'users/register.html',{'form': form })


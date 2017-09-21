# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request, 'factory/home.html', {})
    else:
        # Return an 'invalid login' error message.
        return render(request, 'login/help.html', {})

def logout_view(request):
    logout(request)
    return render(request, 'login/logout.html', {})

def home(request):
    return render(request, 'factory/home.html', {})

def news(request):
    return render(request, 'TAB/blog_index_page.html', {})

def article(request):
    return render(request, 'TAB/blog_page.html', {})

def login(request):
    return render(request, 'login/index.html', {})

def logout(request):
    return render(request, 'login/logout.html', {})

def help(request):
    return render(request, 'login/help.html', {})

def register(request):
    return render(request, 'login/register.html', {})

def loginreset(request):
    return render(request, 'login/reset.html', {})

def contact(request):
    return render(request, 'login/contact.html', {})

def messages(request):
    return render(request, 'messages/messages.html', {})

def Universal_House_of_Justice(request):
    return render(request, 'messages/uhj.html', {})

def National_Spiritual_Assembly(request):
    return render(request, 'messages/nsa.html', {})

def Feast(request):
    return render(request, 'messages/feast.html', {})
    
def Special(request):
    return render(request, 'messages/special.html', {})

def letter(request):
    return render(request, 'messages/letter.html', {})
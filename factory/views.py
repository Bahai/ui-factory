# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


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

def reset(request):
    return render(request, 'login/password_reset.html', {})

def home(request):
    return render(request, 'factory/home.html', {})

def news(request):
    return render(request, 'TAB/blog_index_page.html', {})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def messages(request):
    return render(request, 'messages/messages.html', {})

@login_required(login_url='/login/')
def Universal_House_of_Justice(request):
    return render(request, 'messages/uhj.html', {})

@login_required(login_url='/login/')
def National_Spiritual_Assembly(request):
    return render(request, 'messages/nsa.html', {})

@login_required(login_url='/login/')
def Feast(request):
    return render(request, 'messages/feast.html', {})
    
@login_required(login_url='/login/')
def Special(request):
    return render(request, 'messages/special.html', {})

@login_required(login_url='/login/')
def letter(request):
    return render(request, 'messages/letter.html', {})
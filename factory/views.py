# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'factory/home.html', {})

def TAB_index(request):
    return render(request, 'TAB/blog_index_page.html', {})

def TAB_article(request):
    return render(request, 'TAB/blog_page.html', {})

def TAB_base(request):
    return render(request, 'TAB/tabindex.html')

def login(request):
    return render(request, 'login/index.html', {})

def help(request):
    return render(request, 'login/help.html', {})

def register(request):
    return render(request, 'login/register.html', {})

def loginreset(request):
    return render(request, 'login/reset.html', {})

def contact(request):
    return render(request, 'login/contact.html', {})
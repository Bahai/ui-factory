from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tabhome', views.TAB_index, name='TAB'),
    url(r'^tabarticle', views.TAB_article, name='TAB_article'),
    url(r'^login', views.login, name='login'),
    url(r'^loginhelp', views.login, name='loginhelp'),
    url(r'^register', views.login, name='register'),
    url(r'^passwordreset', views.login, name='loginreset'),
]
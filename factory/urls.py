from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tabhome', views.TAB_index, name='TAB'),
    url(r'^article', views.TAB_article, name='TAB_article'),
    url(r'^basetab', views.TAB_base, name='basetab'),
    url(r'^login', views.login, name='login'),
    url(r'^help', views.help, name='help'),
    url(r'^register', views.register, name='register'),
    url(r'^passwordreset', views.loginreset, name='loginreset'),
    url(r'^contact', views.contact, name='contact'),
]
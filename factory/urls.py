from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_reset


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^news', views.news, name='news'),
    url(r'^article', views.article, name='article'),
    # url(r'^login', views.login, name='login'),
    # url(r'^logout', views.logout, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'login/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login/logout.html'}, name='logout'),
<<<<<<< HEAD
    url(r'^reset/$', password_reset, {'template_name': 'login/reset.html'}, name='reset'),
    url(r'^password_reset_done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'post_reset_redirect' : '/accounts/password_done/'}, name='password_reset_confirm'),
    url(r'^password_done/$', auth_views.password_reset_complete, name='password_done'),
=======
    # url(r'^logout/$', auth_views.logout, {'template_name': 'login/logout.html'}, {'next_page': 'login/login.html'}, name='logout'),
>>>>>>> 9e5cf401871443b1de2660f612381c5853404526
    url(r'^help', views.help, name='help'),
    url(r'^register', views.register, name='register'),
    url(r'^passwordreset', views.loginreset, name='loginreset'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^messages', views.messages, name='messages'),
    url(r'^Universal_House_of_Justice', views.Universal_House_of_Justice, name='Universal_House_of_Justice'),
    url(r'^National_Spiritual_Assembly', views.National_Spiritual_Assembly, name='National_Spiritual_Assembly'),
    url(r'^Feast', views.Feast, name='Feast'),
    url(r'^Special', views.Special, name='Special'),
    url(r'^letter', views.letter, name='letter'),
]
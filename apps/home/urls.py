from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_up/$', views.signup, name='sign_up'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register_process$', views.register_process, name='register_process'),
    url(r'^login_process$', views.login_process, name='login_process'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/$', views.logout, name='logout'),

]

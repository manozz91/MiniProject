from django.conf.urls import url,include
from homePage import views
from django.contrib.auth import views as auth_views

from homePage import views as core_views

urlpatterns = [
    url(r'^home/$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    #url(r'^$', core_views.post_list, name='post_list'),
    url(r'^mainPage/$', core_views.post_list, name='post_list'),
    ]

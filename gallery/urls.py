from django.conf.urls import url
from . import views
from gallery import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^media/$', views.all_media, name="All media"),
    url(r'^users/$', views.all_users, name="All users"),
]

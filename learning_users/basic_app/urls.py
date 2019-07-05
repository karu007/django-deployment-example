from django.conf.urls import url
from basic_app import views


# TEMPLATE URL
app_name = 'basic_app'

urlpatterns = [
    url('^register/$', views.register, name='register'),
    url('^login/$', views.user_login, name='user_login'),
    url('^logout/$', views.user_logout, name='user_logout'),
    url('^special/$', views.special, name='special'),
]

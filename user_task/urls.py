from django.http import HttpResponseRedirect
from django.urls import path

from . import views

urlpatterns = [
    path('download', views.get_users, name='getusers'),
    path('downloadtodos', views.get_todos, name='gettodos'),
]
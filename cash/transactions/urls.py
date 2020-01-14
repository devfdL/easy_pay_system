from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='transactions'),
    path('send_command$', views.send_command, name='send_command'),
]
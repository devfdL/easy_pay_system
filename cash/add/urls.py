from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='add'),
    path('addfund/', views.add_fund, name='addfund'),
]
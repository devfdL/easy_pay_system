from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
    path('',views.index, name='home'),
    path('transactions/', include('transactions.urls'), name= 'transactions'),
    path('add/', include('add.urls'), name= 'add'),
    path('addfund/', include('add.urls'), name= 'addfund'),
    path('pay/', include('pay.urls'), name= 'pay'),
]

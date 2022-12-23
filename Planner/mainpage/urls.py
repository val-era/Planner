from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path(r'archive/<parameter>', views.archive, name='archive'),
    path(r'del/<parameter>', views.delite, name='del'),
]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path(r'archive/<parameter>/<parameter2>', views.archive, name='archive'),
    path(r'del/<parameter>/<parameter2>', views.delite, name='del'),
    path('archive_tasks', views.archive_tasks, name='archive_tasks'),
    path(r'del_archive/<parameter>', views.delite_archive, name='del_archive'),
    path('tomorrow', views.tomorrow, name='tomorrow'),
    path('week', views.week, name='week'),
    path('month', views.month, name='month'),
    path(r'tags/<parameter>/<parameter2>', views.tags, name='tags'),
]
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
    path('global_projects/<parameter>', views.global_projects, name='global_projects'),
    path('notifications', views.notifications, name='notifications'),
    path('del_notif/<parameter>', views.del_notifications, name='del_notif'),
    path('upd_notif/<parameter>/<parameter2>', views.upd_notifications, name='upd_notif'),
]

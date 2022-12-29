import datetime
from .models import Tasks


def save(title, task, teg, date):
    Tasks.objects.create(
        title=title,
        task=task,
        teg=teg,
        date=date,
        is_global=False,
        is_archive=False
    )


def update_global(select, global_task, gl_id):
    if select != "" and global_task == "":
        Tasks.objects.filter(id=gl_id).update(global_task=select)
        Tasks.objects.filter(id=gl_id).update(is_global=True)
    elif select != "" and global_task != "":
        Tasks.objects.filter(id=gl_id).update(global_task=global_task)
        Tasks.objects.filter(id=gl_id).update(is_global=True)
    elif select == "" and global_task != "":
        Tasks.objects.filter(id=gl_id).update(global_task=global_task)
        Tasks.objects.filter(id=gl_id).update(is_global=True)
    else:
        pass

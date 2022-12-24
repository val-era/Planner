import datetime

from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskForm, DateForm, GlobalForm


def save(title, task, teg, date):
    Tasks.objects.create(
        title=title,
        task=task,
        teg=teg,
        date=date,
        is_global=False,
        is_archive=False
    )


def main(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form["title"].value()
            task = form["task"].value()
            teg = form["teg"].value()
            date = form["date"].value()
            save(title, task, teg, date)
            return redirect('main')
        else:
            pass

        time_form = DateForm(request.POST)
        id = time_form["id"].value()
        date = time_form["date"].value()
        Tasks.objects.filter(id=id).update(date=date)

        glob_form = GlobalForm(request.POST)
        gl_id = glob_form["idtask"].value()
        select = glob_form["sel"].value()
        global_task = glob_form["global_add"].value()
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


    task = Tasks.objects.order_by("date").filter(date=datetime.date.today())
    global_tasks = set([i.global_task for i in Tasks.objects.order_by("date")])
    form = TaskForm()
    dateform = DateForm()
    globform = GlobalForm()
    return render(request, 'mainpage/plan.html', {'task': task, 'form': form, 'dateform': dateform,
                                                  'globform': globform, 'global_tasks': global_tasks})


def archive(request, parameter):
    Tasks.objects.filter(id=parameter).update(is_archive=True)
    return redirect('main')


def delite(request, parameter):
    Tasks.objects.filter(id=parameter).delete()
    return redirect('main')

def archive_tasks(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        id = form["id"].value()
        date = form["date"].value()
        Tasks.objects.filter(id=id).update(date=date)
        Tasks.objects.filter(id=id).update(is_archive=False)

    tasks = Tasks.objects.order_by("date").filter(is_archive=True)
    start_date = datetime.date(2022, 11, 30)
    end_date = datetime.date.today() - datetime.timedelta(days=1)
    date_last = Tasks.objects.order_by("date").filter(date__range=[start_date, end_date])
    task = [tasks, date_last]
    dateform = DateForm()
    return render(request, 'mainpage/archive_tasks.html', {'task': task, 'dateform': dateform})

def delite_archive(request, parameter):
    Tasks.objects.filter(id=parameter).delete()
    return redirect('archive_tasks')


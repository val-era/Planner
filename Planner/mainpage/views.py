import datetime

from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskForm, DateForm, GlobalForm
from .scripts import save, update_global


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
        update_global(select, global_task, gl_id)

    task = Tasks.objects.order_by("date").filter(date=datetime.date.today())
    global_tasks = set([i.global_task for i in Tasks.objects.order_by("date")])
    form = TaskForm()
    dateform = DateForm()
    globform = GlobalForm()
    return render(request, 'mainpage/plan.html', {'task': task, 'form': form, 'dateform': dateform,
                                                  'globform': globform, 'global_tasks': global_tasks, 'day': 'today'})


def archive(request, parameter, parameter2):
    if parameter2 == 'today':
        Tasks.objects.filter(id=parameter).update(is_archive=True)
        return redirect('main')
    elif parameter2 == 'week':
        Tasks.objects.filter(id=parameter).update(is_archive=True)
        return redirect('week')
    elif parameter2 == 'month':
        Tasks.objects.filter(id=parameter).update(is_archive=True)
        return redirect('month')
    else:
        Tasks.objects.filter(id=parameter).update(is_archive=True)
        return redirect('tomorrow')


def delite(request, parameter, parameter2):
    if parameter2 == 'today':
        Tasks.objects.filter(id=parameter).delete()
        return redirect('main')
    elif parameter2 == 'week':
        Tasks.objects.filter(id=parameter).delete()
        return redirect('week')
    elif parameter2 == 'month':
        Tasks.objects.filter(id=parameter).delete()
        return redirect('month')
    else:
        Tasks.objects.filter(id=parameter).delete()
        return redirect('tomorrow')


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


def tomorrow(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form["title"].value()
            task = form["task"].value()
            teg = form["teg"].value()
            date = form["date"].value()
            save(title, task, teg, date)
            return redirect('tomorrow')
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
        update_global(select, global_task, gl_id)

    task = Tasks.objects.order_by("date").filter(date=(datetime.date.today() + datetime.timedelta(1)))
    global_tasks = set([i.global_task for i in Tasks.objects.order_by("date")])
    form = TaskForm()
    dateform = DateForm()
    globform = GlobalForm()
    return render(request, 'mainpage/plan.html', {'task': task, 'form': form, 'dateform': dateform,
                                                  'globform': globform, 'global_tasks': global_tasks, 'day': 'tomorrow'})


def week(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form["title"].value()
            task = form["task"].value()
            teg = form["teg"].value()
            date = form["date"].value()
            save(title, task, teg, date)
            return redirect('week')
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
        update_global(select, global_task, gl_id)
    tasks = Tasks.objects.order_by("date").filter(date__range=[datetime.date.today(), datetime.date.today() + datetime.timedelta(7)])
    tasks = tasks.filter(is_archive=False)
    task = {}
    for i in tasks:
        if i.date not in task:
            task[i.date] = [i]
        else:
            task[i.date].append(i)
    global_tasks = set([i.global_task for i in Tasks.objects.order_by("date")])
    form = TaskForm()
    dateform = DateForm()
    globform = GlobalForm()
    return render(request, 'mainpage/days.html', {'task': task, 'form': form, 'dateform': dateform,
                                                  'globform': globform, 'global_tasks': global_tasks,
                                                  'day': 'week'})


def month(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form["title"].value()
            task = form["task"].value()
            teg = form["teg"].value()
            date = form["date"].value()
            save(title, task, teg, date)
            return redirect('month')
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
        update_global(select, global_task, gl_id)
    tasks = Tasks.objects.order_by("date").filter(date__range=[datetime.date.today(), datetime.date.today() + datetime.timedelta(31)])
    tasks = tasks.filter(is_archive=False)
    task = {}
    for i in tasks:
        if i.date not in task:
            task[i.date] = [i]
        else:
            task[i.date].append(i)
    global_tasks = set([i.global_task for i in Tasks.objects.order_by("date")])
    form = TaskForm()
    dateform = DateForm()
    globform = GlobalForm()
    return render(request, 'mainpage/days.html', {'task': task, 'form': form, 'dateform': dateform,
                                                  'globform': globform, 'global_tasks': global_tasks,
                                                  'day': 'month'})


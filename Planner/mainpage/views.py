import datetime

from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskForm, DateForm


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

    task = Tasks.objects.order_by("date").filter(date=datetime.date.today())
    form = TaskForm()
    dateform = DateForm()
    return render(request, 'mainpage/plan.html', {'task': task, 'form': form, 'dateform': dateform})


def archive(request, parameter):
    Tasks.objects.filter(id=parameter).update(is_archive=True)
    return redirect('main')


def delite(request, parameter):
    Tasks.objects.filter(id=parameter).delete()
    return redirect('main')



import datetime

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskForm

def save(title, task, teg, date):
    Tasks.objects.create(
        title=title,
        task=task,
        teg=teg,
        date=date,
        is_global=False
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
    task = Tasks.objects.order_by("date").filter(date=datetime.date.today())
    form = TaskForm()
    return render(request, 'mainpage/plan.html', {'task': task, 'form': form})

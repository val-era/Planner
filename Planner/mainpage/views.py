import datetime

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskForm


def main(request):
    task = Tasks.objects.order_by("date").filter(date=datetime.date.today())
    form = TaskForm()
    return render(request, 'mainpage/plan.html', {'task': task, 'form': form})

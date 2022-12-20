import datetime

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tasks


def main(request):
    task = Tasks.objects.order_by("date").filter(date=datetime.date.today())
    return render(request, 'mainpage/main.html', {'task': task})

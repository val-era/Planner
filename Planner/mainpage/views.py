from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'mainpage/main.html')

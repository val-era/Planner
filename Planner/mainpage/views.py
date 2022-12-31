import datetime

from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskForm, DateForm, GlobalForm, TagsForm, GlobalProjectsForm
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


def tags(request, parameter, parameter2):
    if request.method == 'POST':
        form_tag = TagsForm(request.POST)
        tag = form_tag["teg"].value()
        date = form_tag['date'].value()
        if date != "" and tag != "":
            return redirect('tags', tag, date)
        elif date == "" and tag != "":
            return redirect('tags', tag, "all")
        elif date != "" and tag == "":
            return redirect('tags', "more", date)
        else:
            return redirect('tags', "more", "all")

    if parameter2 == "all":
        if parameter == "more":
            tasks = Tasks.objects.order_by("date").filter(
                date__range=[datetime.date.today(), datetime.date.today() + datetime.timedelta(120)])
        else:
            task = Tasks.objects.order_by("date").filter(
                date__range=[datetime.date.today(), datetime.date.today() + datetime.timedelta(120)])
            tasks = task.filter(teg=parameter)
    else:
        if parameter == "more":
            tasks = Tasks.objects.order_by("date").filter(date=parameter2)
        else:
            task = Tasks.objects.order_by("date").filter(date=parameter2)
            tasks = task.filter(teg=parameter)

    form = TagsForm()
    return render(request, 'mainpage/tags.html', {'tasks': tasks, 'form': form})


def global_projects(request, parameter):
    if request.method == 'POST':
        form = GlobalProjectsForm(request.POST)
        value = form['globform'].value()
        if value == "":
            return redirect('global_projects', "all")
        else:
            return redirect('global_projects', value)

    form = GlobalProjectsForm()
    tasks_obj = Tasks.objects.order_by("date").filter(is_global=True)
    all_tasks = tasks_obj.filter(
        date__range=[datetime.date.today(), datetime.date.today() + datetime.timedelta(120)])
    if parameter != 'all':
        tasks = all_tasks.filter(global_task=parameter)
    else:
        tasks = all_tasks
    task = {}
    for i in tasks:
        if i.global_task not in task:
            task[i.global_task] = [i]
        else:
            task[i.global_task].append(i)

    all_task = {}
    for i in all_tasks:
        if i.global_task not in all_task:
            all_task[i.global_task] = [i]
        else:
            all_task[i.global_task].append(i)

    return render(request, 'mainpage/global.html', {'task': task, 'form': form, 'all_task': all_task})
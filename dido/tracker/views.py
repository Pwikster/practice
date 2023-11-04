from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from .forms import TaskForm


def main(request):
    # Initialize the form
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")  # Redirect to a named URL pattern, not a template

    # Fetch tasks regardless of whether it was GET or POST
    tasks = reversed(Task.objects.all())
    context = {"tasks": tasks, "form": form}
    return render(request, "main.html", context)


@require_POST
def mark_task_done(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = True
    task.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("main")
    else:
        form = TaskForm(instance=task)
    return render(request, "edit_task.html", {"form": form})

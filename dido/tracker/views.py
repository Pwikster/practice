from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def main(request):
    # Initialize the form
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  # Redirect to a named URL pattern, not a template

    # Fetch tasks regardless of whether it was GET or POST
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'form': form}
    return render(request, "main.html", context)

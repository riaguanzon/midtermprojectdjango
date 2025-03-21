from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Task

# View to list all tasks with optional search functionality
def task_list(request):
    query = request.GET.get('q', '')  # Get search query from the request (default to empty string)
    tasks = Task.objects.filter(title__icontains=query) if query else Task.objects.all()  # Filter tasks by title if a query is provided

    return render(request, 'tasks/tasks_list.html', {'tasks': tasks, 'query': query})


# View to create a new task
def task_create(request):
    if request.method == "POST":
        title = request.POST.get('title')  # Get task title from the form
        description = request.POST.get('description', '')  # Get optional description
        due_date = request.POST.get('due_date')  # Get due date

        if title and due_date:  # Ensure required fields are provided
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date()  # Convert date string to a date object
            except ValueError:
                return HttpResponse("Invalid date format", status=400)  # Return an error if the date format is incorrect

            Task.objects.create(title=title, description=description, due_date=due_date)  # Create and save the task
            return redirect('task_list')  # Redirect to task list after successful creation

    return render(request, 'tasks/task_form.html')  # Render the task creation form


# View to update an existing task
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Retrieve the task or return a 404 error if not found

    if request.method == "POST":
        task.title = request.POST.get('title')  # Update title
        task.description = request.POST.get('description', '')  # Update description
        due_date = request.POST.get('due_date')  # Get new due date

        if task.title and due_date:  # Ensure required fields are provided
            try:
                task.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()  # Convert date string to a date object
            except ValueError:
                return HttpResponse("Invalid date format", status=400)  # Return an error if the date format is incorrect

            task.save()  # Save changes to the task
            return redirect('task_list')  # Redirect to task list after successful update

    return render(request, 'tasks/task_form.html', {'task': task})  # Render the task update form


# View to delete a task
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Retrieve the task or return a 404 error if not found

    if request.method == "POST":
        task.delete()  # Delete the task from the database
        return redirect('task_list')  # Redirect to task list after successful deletion

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})  # Render confirmation page before deletion

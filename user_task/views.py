from django.shortcuts import render
from django.http import HttpResponse
import requests
import csv
from .models import Users, Todos

# Create your views here.


def get_users(request):
    users = Users()
    counter_new, counter_total = users.get_users_to_db()
    return HttpResponse("{}/{}".format(counter_new, counter_total))


def get_todos(request):
    todos = Todos()
    counter_new, counter_total = todos.get_users_to_db()
    return HttpResponse("{}/{}".format(counter_new, counter_total))


def csv_file(request):
    # Create the HttpResponse object with the appropriate CSV header.
    todos = Todos.objects.all()
    users = Users.objects.all()
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="user_task.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['name', 'city', 'title', 'completed'])
    for j in todos:
        for i in users:
            if i.user_id == j.user_id:
                writer.writerow([i.name, i.address_city, j.title, j.completed])

    return response

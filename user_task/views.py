from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Users

# Create your views here.


def get_users(request):
    users = Users()
    counter_new, counter_total = users.get_users_to_db()
    return HttpResponse("{}/{}".format(counter_new, counter_total))


def get_todos(request):
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.request("GET", url)
    todos_response = response.json()

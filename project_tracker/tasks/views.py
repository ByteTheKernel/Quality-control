from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    another_page_url = reverse('tasks:another_page')
    quality_control_app_url = 'quality_control/'
    html = (f"<h1>Страница приложения tasks</h1>"
            f"<p><a href='{another_page_url}'>Перейти на другую страницу</a></p>"
            f"<p><a href='{quality_control_app_url}'>Quality Control</a></p>")
    return HttpResponse(html)


def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")


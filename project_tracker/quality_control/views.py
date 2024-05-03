from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    bugs_list_url = reverse('quality_control:bugs_list')
    features_list_url = reverse('quality_control:features_list')
    html = (f"<h1>Система контроля качества</h1>"
            f"<p><a href='{bugs_list_url}'>Список всех багов</a></p>"
            f"<p><a href = '{features_list_url}'>Запросы на улучшение</a></p>")
    return HttpResponse(html)


def bugs_list(request):
    return HttpResponse("Cписок отчетов об ошибках")


def bug_id_detail(request, id):
    return HttpResponse(f"Детали бага {id}")


def features_list(request):
    return HttpResponse("Список запросов на улучшение")


def feature_id_detail(request, id):
    return HttpResponse(f"Детали улучшения {id}")

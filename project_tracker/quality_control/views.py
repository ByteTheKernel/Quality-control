from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.views import View
from django.views.generic import ListView, DetailView


def index(request):
    bugs_list_url = reverse('quality_control:bugs_list')
    features_list_url = reverse('quality_control:features_list')
    html = (f"<h1>Система контроля качества</h1>"
            f"<p><a href='{bugs_list_url}'>Список всех багов</a></p>"
            f"<p><a href = '{features_list_url}'>Запросы на улучшение</a></p>")
    return HttpResponse(html)


def bugs_list(request):
    bug_reports = BugReport.objects.all()
    bug_reports_html = '<h1>Список баг репортов</h1><ul>'
    for bug_report in bug_reports:
        bug_reports_html += (f"<li><a href='{bug_report.id}/'>{bug_report.title}</a>"
                             f" - {bug_report.get_status_display()}</li>")
    bug_reports_html += f'</ul>'
    return HttpResponse(bug_reports_html)


def features_list(request):
    feature_requests = FeatureRequest.objects.all()
    feature_request_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature_request in feature_requests:
        feature_request_html += (f"<li><a href='{feature_request.id}/'>{feature_request.title}</a> "
                                 f" - {feature_request.get_status_display()}</li>")
    feature_request_html += f"</ul>"
    return HttpResponse(feature_request_html)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_list_url = reverse('quality_control:bugs_list')
        features_list_url = reverse('quality_control:features_list')
        html = (f"<h1>Система контроля качества</h1>"
                f"<p><a href='{bugs_list_url}'>Список всех багов</a></p>"
                f"<p><a href = '{features_list_url}'>Запросы на улучшение</a></p>")
        return HttpResponse(html)


class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_report_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug_report = self.object
        response_html = (f"<h1>{bug_report.title}</h1>"
                         f"<p><strong>Описание:</strong> {bug_report.description}</p>"
                         f"<p><strong>Статус:</strong> {bug_report.get_status_display()}</p>"
                         f"<p><strong>Приоритет:</strong> {bug_report.priority}</p>"
                         f"<p><strong>Проект:</strong> {bug_report.project.name}</p>"
                         f"<p><strong>Задача:</strong> {bug_report.task.name}</p>")
        return HttpResponse(response_html)


class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_request_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature_request = self.object
        response_html = (f"<h1>{feature_request.title}</h1>"
                         f"<p><strong>Описание:</strong> {feature_request.description}</p>"
                         f"<p><strong>Статус:</strong> {feature_request.get_status_display()}</p>"
                         f"<p><strong>Приоритет:</strong> {feature_request.priority}</p>"
                         f"<p><strong>Проект:</strong> {feature_request.project.name}</p>"
                         f"<p><strong>Задача:</strong> {feature_request.task.name}</p>")
        return HttpResponse(response_html)

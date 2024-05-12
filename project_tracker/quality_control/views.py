from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from tasks.models import Project, Task
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import BugReportForm, FeatureRequestForm


def index(request):
    return render(request, 'quality_control/index.html')


def bugs_list(request):
    bug_reports = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bug_reports': bug_reports})


def features_list(request):
    feature_requests = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'feature_requests': feature_requests})


def create_bug_report(request, project_id=None):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


def create_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


def get_tasks_for_project(request, project_id):
    tasks = list(Task.objects.filter(project_id=project_id).values('id', 'name'))
    return JsonResponse(tasks, safe=False)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_report_id'
    template_name = 'quality_control/bug_id_detail.html'


class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_request_id'
    template_name = 'quality_control/feature_id_detail.html'

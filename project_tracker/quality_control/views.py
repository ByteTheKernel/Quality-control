from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.views import View
from django.views.generic import ListView, DetailView


def index(request):
    return render(request, 'quality_control/index.html')


def bugs_list(request):
    bug_reports = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bug_reports': bug_reports})


def features_list(request):
    feature_requests = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'feature_requests': feature_requests})


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

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from .models import BugReport, FeatureRequest
from tasks.models import Project, Task
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


def update_bug_report(request, bug_report_id):
    bug_report = get_object_or_404(BugReport, pk=bug_report_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug_report)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_id_detail', bug_report_id=bug_report_id)
    else:
        form = BugReportForm(instance=bug_report)
    return render(request, 'quality_control/bug_report_form_update.html',
                  {'form': form, 'bug_report': bug_report})


def update_feature_request(request, feature_request_id):
    feature_request = get_object_or_404(FeatureRequest, pk=feature_request_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature_request)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_id_detail', feature_request_id=feature_request_id)
    else:
        form = FeatureRequestForm(instance=feature_request)
    return render(request, 'quality_control/feature_request_form_update.html',
                  {'form': form, 'feature_request': feature_request})


def delete_bug_report(request, bug_report_id):
    bug_report = get_object_or_404(BugReport, pk=bug_report_id)
    bug_report.delete()
    return redirect('quality_control:bugs_list')


def delete_feature_request(request, feature_request_id):
    feature_request = get_object_or_404(FeatureRequest, pk=feature_request_id)
    feature_request.delete()
    return redirect('quality_control:features_list')


def get_tasks_for_project(request, project_id):
    tasks = list(Task.objects.filter(project_id=project_id).values('id', 'name'))
    return JsonResponse(tasks, safe=False)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


class BugsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugs_list.html'
    context_object_name = 'bug_reports'


class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_report_id'
    template_name = 'quality_control/bug_id_detail.html'


class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bugs_list')


class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form_update.html'
    pk_url_kwarg = 'bug_report_id'
    success_url = reverse_lazy('quality_control:bugs_list')
    context_object_name = 'bug_report'


class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_report_id'
    success_url = reverse_lazy('quality_control:bugs_list')
    template_name = 'quality_control/bug_report_confirm_delete.html'


class FeatureRequestListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/features_list.html'
    context_object_name = 'feature_requests'


class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_request_id'
    template_name = 'quality_control/feature_id_detail.html'


class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:features_list')


class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form_update.html'
    pk_url_kwarg = 'feature_request_id'
    success_url = reverse_lazy('quality_control:features_list')
    context_object_name = 'feature_request'


class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_request_id'
    success_url = reverse_lazy('quality_control:features_list')
    template_name = 'quality_control/feature_request_confirm_delete.html'

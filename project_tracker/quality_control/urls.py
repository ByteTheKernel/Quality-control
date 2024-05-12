from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index),
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.bugs_list, name='bugs_list'),
    path('bugs/<int:bug_report_id>/', views.BugReportDetailView.as_view(), name='bug_id_detail'),
    path('features/', views.features_list, name='features_list'),
    path('features/<int:feature_request_id>/', views.FeatureRequestDetailView.as_view(), name='feature_id_detail'),
    path('bugs/new/', views.create_bug_report, name='create_bug_report'),
    path('ajax/get-tasks-for-project/<int:project_id>/', views.get_tasks_for_project, name='get_tasks_for_project'),
    path('features/new/', views.create_feature_request, name='create_feature_request'),
]

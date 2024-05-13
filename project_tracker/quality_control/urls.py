from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index),
    path('', views.IndexView.as_view(), name='index'),
    # path('bugs/', views.bugs_list, name='bugs_list'),
    path('bugs/', views.BugsListView.as_view(), name='bugs_list'),
    path('bugs/<int:bug_report_id>/', views.BugReportDetailView.as_view(), name='bug_id_detail'),
    # path('features/', views.features_list, name='features_list'),
    path('features/', views.FeatureRequestListView.as_view(), name='features_list'),
    path('features/<int:feature_request_id>/', views.FeatureRequestDetailView.as_view(), name='feature_id_detail'),
    # path('bugs/new/', views.create_bug_report, name='create_bug_report'),
    path('bugs/new/', views.BugReportCreateView.as_view(), name='create_bug_report'),
    path('ajax/get-tasks-for-project/<int:project_id>/', views.get_tasks_for_project, name='get_tasks_for_project'),
    # path('features/new/', views.create_feature_request, name='create_feature_request'),
    path('features/new/', views.FeatureRequestCreateView.as_view(), name='create_feature_request'),
    # path('bugs/<int:bug_report_id>/update/', views.update_bug_report, name='update_bug_report'),
    path('bugs/<int:bug_report_id>/update/', views.BugReportUpdateView.as_view(), name='update_bug_report'),
    # path('features/<int:feature_request_id>/update/', views.update_feature_request, name='update_feature_request'),
    path('features/<int:feature_request_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_feature_request'),
    # path('bugs/<int:bug_report_id>/delete/', views.delete_bug_report, name='delete_bug_report'),
    path('bugs/<int:bug_report_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug_report'),
    # path('features/<int:feature_request_id>/delete/', views.delete_feature_request, name='delete_feature_request'),
    path('features/<int:feature_request_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature_request'),
]

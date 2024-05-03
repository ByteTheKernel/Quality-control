from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    path('bugs/', views.bugs_list, name='bugs_list'),
    path('bugs/<int:id>/', views.bug_id_detail, name='bug_id_detail'),
    path('features/', views.features_list, name='features_list'),
    path('features/<int:id>', views.feature_id_detail, name='feature_id_detail'),
]

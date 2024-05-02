from django.contrib import admin
from .models import BugReport, FeatureRequest


def change_status_to_new(modeladmin, request, queryset):
    queryset.update(status='New')


def change_status_to_in_progress(modeladmin, request, queryset):
    queryset.update(status='In_progress')


def change_status_to_completed(modeladmin, request, queryset):
    queryset.update(status='Completed')


change_status_to_new.short_description = 'Изменить статус на "Новая"'
change_status_to_in_progress.short_description = 'Изменить статус на "В работе"'
change_status_to_completed.short_description = 'Изменить статус на "Завершена"'


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('project', 'task', 'status', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    actions = [change_status_to_new, change_status_to_in_progress, change_status_to_completed]

    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Project and Task', {
            'fields': ('project', 'task')
        }),
        ('Status and Priority', {
            'fields': ('status', 'priority')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('project', 'task', 'status', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Project and Task', {
            'fields': ('project', 'task'),
            'classes': ('wide',),
        }),
        ('Status and Priority', {
            'fields': ('status', 'priority'),
            'classes': ('wide',),
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

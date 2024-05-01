from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    STATUS_CHOICE = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]

    PRIORITY_CHOICE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICE,
        default='New'
    )

    priority = models.IntegerField(
        choices=PRIORITY_CHOICE,
        default=1
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    project = models.ForeignKey(
        Project,
        related_name='quality_control',
        on_delete=models.CASCADE
    )

    task = models.ForeignKey(
        Task,
        related_name='quality_control',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    STATUS_CHOICE = [
        ('Review', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Declined', 'Отклонено'),
    ]

    PRIORITY_CHOICE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICE,
        default='Review'
    )

    priority = models.IntegerField(
        choices=PRIORITY_CHOICE,
        default=1
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



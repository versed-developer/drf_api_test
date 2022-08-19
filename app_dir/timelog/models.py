from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now

from app_dir.project.models import Project


class TimeLog(models.Model):
    project = models.ForeignKey(
        Project,
        null=False,
        on_delete=models.CASCADE
    )
    description = models.TextField(
        pgettext_lazy('TimeLog Description Field', 'description'),
        blank=True,
        null=True
    )
    start_time = models.DateTimeField(
        pgettext_lazy('TimeLog start field', 'start time'),
        default=now
    )
    end_time = models.DateTimeField(
        pgettext_lazy('TimeLog end field', 'end time'),
        default=now
    )
    created_at = models.DateTimeField(
        pgettext_lazy('TimeLog field', 'created at'),
        default=now,
        editable=False
    )
    updated_at = models.DateTimeField(
        pgettext_lazy('TimeLog field', 'updated at'),
        default=now
    )

    class Meta:
        app_label = 'timelog'

    def __str__(self):
        return self.description

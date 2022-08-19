from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now


class Project(models.Model):
    name = models.CharField(
        pgettext_lazy('Project Name Field', 'name'),
        unique=True,
        max_length=128
    )
    description = models.TextField(
        pgettext_lazy('Project Description Field', 'description'),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        pgettext_lazy('Project field', 'created at'),
        default=now,
        editable=False
    )
    updated_at = models.DateTimeField(
        pgettext_lazy('Project field', 'updated at'),
        default=now
    )

    class Meta:
        app_label = 'project'

    def __str__(self):
        return self.name

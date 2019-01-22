from django.db import models as django_models
from djongo import models as djongo_models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Sprint(djongo_models.Model):
    """Development iteration period."""

    name = djongo_models.CharField(max_length=100, blank=True, default='')
    description = djongo_models.TextField(blank=True, default='')
    end = djongo_models.DateField(unique=True)

    def __str__(self):
        return self.name or _('Sprint Ending %s') % self.end


class Task(djongo_models.Model):
    """Unit of work to be done for the sprint."""

    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO, _('Not Started')),
        (STATUS_IN_PROGRESS, _('In Progress')),
        (STATUS_TESTING, _('Testing')),
        (STATUS_DONE, _('Done')),
    )

    name = djongo_models.CharField(max_length=100)
    description = djongo_models.TextField(blank=True, default='')
    sprint = djongo_models.ForeignKey(Sprint, blank=True, null=True, on_delete=djongo_models.CASCADE)
    status = djongo_models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    order = djongo_models.SmallIntegerField(default=0)
    assigned = djongo_models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=djongo_models.SET_NULL)
    started = djongo_models.DateField(blank=True, null=True)
    due = djongo_models.DateField(blank=True, null=True)
    completed = djongo_models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name



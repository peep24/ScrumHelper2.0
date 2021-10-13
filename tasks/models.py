from django.db import models
from account.models import Account
from django.core.validators import MinLengthValidator

STATUS_CHOICES = (
    ('active','Active'),
    ('With client', 'With Client'),
    ('blocked','BLOCKED'),
    ('complete','COMPLETE'),
)


class Tasks(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    task_id = models.CharField(max_length=14, validators=[MinLengthValidator(8)], primary_key=True, blank=False, null=False)
    task_name = models.TextField(blank=True, null=True)
    client = models.CharField(max_length=40, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='active')
    owner = models.CharField(max_length=40, blank=True, null=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    # Metadata
    class Meta:
        ordering = ['-task_id']
        verbose_name_plural = "Tasks"


class AccountTask(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    user_status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='active')
    user_blocked = models.BooleanField(default=False)


    # Metadata
    class Meta:
        ordering = ['-task_id']
        verbose_name_plural = "AccountTasks"


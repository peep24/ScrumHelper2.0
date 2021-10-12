from django.db import models

STATUS_CHOICES = (
    ('active','Active'),
    ('With client', 'With Client'),
    ('blocked','BLOCKED'),
)


class Tasks(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    task_id = models.AutoField(primary_key=True)
    task_name = models.TextField(blank=True, null=True)
    client = models.CharField(max_length=40, blank=True, null=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='active')
    owner = models.CharField(max_length=40, blank=True, null=True)

    # Metadata
    class Meta:
        ordering = ['-task_id']
        verbose_name_plural = "Tasks"





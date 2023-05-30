from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(default="pending", max_length=12)
    priority = models.CharField(max_length=10, default="normal")
    start_date = models.DateField()
    end_date = models.DateField()

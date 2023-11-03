from django.db import models

# Create your models here.
class Task(models.Model):
    item = models.CharField(max_length=50, null=False)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

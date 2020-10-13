from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=50,default="")
    date1 = models.DateField(null=True)
    labels = models.CharField(max_length=50,default="")
    status = models.CharField(max_length=50,default="")
    priority = models.CharField(max_length=10,default="")
    name=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.task


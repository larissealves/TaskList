from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.title

class Description(models.Model):
    description = models.TextField()
    rel = models.OneToOneField(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

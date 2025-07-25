from django.db import models
from django.urls import reverse

class Todo(models.Model):
        name = models.CharField(max_length=30)
        description = models.TextField()
        day = models.DateField()
        priority = models.CharField(max_length=20)
        tags = models.CharField(max_length=50 )
        esttime =models.DurationField()

        def __str__(self):
                return self.name
        def get_absolute_url(self):
                return reverse('todo-detail', kwargs={'todo_id': self.id})

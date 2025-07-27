from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORIES= (
        ('WO', 'Work'),
        ('LE', 'Learning'),
        ('CR', 'Creative'),
        ('TR', 'Travel'),
        ('HO', 'Home'),
        ('WE', 'Wellness'),
        ('HE', 'Health'),
        ('FO', 'Food'),
        ('SO', 'Social'),
        ('FA', 'Family'),
        ('RE', 'Relationship'),
)

PRIORITY_CHOICES = (
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
        (4, 'None'),
)

class Todo(models.Model):
        name = models.CharField(max_length=30)
        description = models.TextField()
        day = models.DateField()
        priority = models.IntegerField(
                choices=PRIORITY_CHOICES,
                default= 4
                )
        esttime =models.DurationField()
        category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True )
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        def __str__(self):
                return self.name

        def get_absolute_url(self):
                return reverse('todo-detail', kwargs={'todo_id': self.id})

        class Meta:
                ordering = ['priority', 'day']

class Category(models.Model):
        name= models.CharField(max_length=2, choices=CATEGORIES)
        image= models.CharField(max_length=255)

        def __str__(self):
                return self.get_name_display()

from django.contrib.auth.models import User

from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # generate a date at the time of the creation of the task
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # function for returning the title of the to do item in the list of items
    def __str__(self):
        return self.title

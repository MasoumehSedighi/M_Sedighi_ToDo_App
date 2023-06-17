from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Task(models.Model):
    '''
    a model for tasks
    '''
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name


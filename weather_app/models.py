from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    username = models.EmailField(primary_key=True)
    feedback_message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


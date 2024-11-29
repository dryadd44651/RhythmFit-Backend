from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    max1RM = models.IntegerField()
    group = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="exercises")

    def __str__(self):
        return self.name

class Workout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="workout")
    currentCycle = models.CharField(max_length=50, default="light")
    trainedGroups = models.JSONField(default=list)  # Stores trained muscle groups as a list

    def __str__(self):
        return f"{self.user.username}'s Workout"

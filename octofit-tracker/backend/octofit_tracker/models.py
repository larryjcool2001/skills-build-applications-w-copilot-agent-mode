# File: /octofit-tracker/octofit-tracker/backend/octofit_tracker/models.py

from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # Duration in minutes
    distance = models.FloatField()  # Distance in kilometers
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} by {self.user.username} on {self.date}"

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_distance = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username}: {self.total_distance} km"
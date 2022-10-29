from django.db import models

# Create your models here.

class UserInfo(models.Model):
    slackUsername = models.CharField(max_length=20)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.username

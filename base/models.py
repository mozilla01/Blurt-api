from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.CharField(max_length=25)
    content = models.TextField(max_length=500)
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user + " " + str(self.id)

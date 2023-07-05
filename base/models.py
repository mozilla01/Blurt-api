from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.CharField(max_length=25)
    content = models.TextField(max_length=500)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user + " " + str(self.id)


class Like(models.Model):
    user = models.CharField(max_length=25)
    post = models.ManyToManyField(Post, blank=True, related_name="posts")


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.CharField(max_length=25)
    content = models.TextField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

from django.db import models
from django.utils import timezone


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class Post(models.Model):
    user = models.CharField(max_length=25)
    content = models.TextField(max_length=500)
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

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

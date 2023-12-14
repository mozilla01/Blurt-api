from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class Post(models.Model):

    class Type(models.TextChoices):
        REPLY = 'R', _('Reply')
        POST = 'P', _('Post')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(
            max_length=1,
            choices=Type.choices,
            default=Type.POST,
            )
    user = models.CharField(max_length=25)
    content = models.TextField(max_length=500)
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.user + " " + str(self.id)


class Like(models.Model):
    user = models.CharField(max_length=25)
    post = models.ManyToManyField(Post, blank=True, related_name="posts")


from django.db import models
from django.utils import timezone


class Post(models.Model):
    #ffff
    #comment from testbrach
    #new comment
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=100)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
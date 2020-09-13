from django.conf import settings
from django.db import models
from django.utils import timezone


class Item(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def post(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
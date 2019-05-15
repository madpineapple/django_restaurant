from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class dMenu(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main-dMenu', kwargs={'pk':self.pk})

class bMenu(models.Model):
    bTitle = models.CharField(max_length=100)
    bDescription = models.TextField()
    bPrice = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone


class Team(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    designation = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='Photos/%Y/%M/%D', null=True)
    facebook_link = models.URLField(max_length=100, null=True)
    twitter_link = models.URLField(max_length=100, null=True)
    google_plus_link = models.URLField(max_length=100, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name

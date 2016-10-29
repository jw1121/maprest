from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserVote(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    loc_label = models.CharField(max_length=150, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    Longitude = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    ip = models.CharField(max_length=150, blank=True, null=True)


    def natural_key(self):
        return (self.latitude, self.Longitude)
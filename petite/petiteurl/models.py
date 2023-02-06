from django.db import models

# Create your models here.
from django.db import models


class Urls(models.Model):
    hash_value = models.CharField(max_length=8, blank=True, default='')
    url = models.URLField(max_length=600)
    exp_date = models.DateTimeField(null=True, blank=True)
    added_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.url}"

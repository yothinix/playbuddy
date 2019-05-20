from django.db import models


class Movie(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256)

    def __str__(self):
        return self.name

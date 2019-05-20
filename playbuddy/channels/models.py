from django.db import models


class Channel(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256)
    display_name = models.CharField(null=True, blank=True, max_length=256)

    def __str__(self):
        return f'{self.display_name} ({self.name})'

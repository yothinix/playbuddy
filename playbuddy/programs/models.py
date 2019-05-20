from django.db import models

import pendulum

from channels.models import Channel
from movies.models import Movie


class Program(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, null=True, blank=True, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()

    @property
    def movie_name(self):
        return self.movie.name

    @property
    def channel_name(self):
        return self.channel.display_name

    @property
    def now_showing(self):
        now = pendulum.now()

        if now.date() == self.date:
            return self.start_time < now.time() < self.end_time
        else:
            return False

    def __str__(self):
        return f'{self.movie.name} [{self.date}] {self.start_time} - {self.end_time}'


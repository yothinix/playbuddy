from django.db import models

from movies.models import Movie


class Program(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()

    @property
    def name(self):
        return self.movie.name

    def __str__(self):
        return f'{self.movie.name} [{self.date}] {self.start_time} - {self.end_time}'


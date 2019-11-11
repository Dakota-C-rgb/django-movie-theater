from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    rating = models.FloatField()
    genre = models.TextField()
    runtime = models.DateField()

class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    showtime = models.DateTimeField()

class Ticket(models.Model):
    name = models.TextField()
    purchased_at = models.DateField()
    showing = models.ForeignKey(Showing, on_delete=models.PROTECT)
 
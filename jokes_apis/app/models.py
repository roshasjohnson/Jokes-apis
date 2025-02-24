from django.db import models

# Create your models here.


class Joke(models.Model):
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    joke = models.TextField(null=True, blank=True)
    setup = models.TextField(null=True, blank=True)
    delivery = models.TextField(null=True, blank=True)
    nsfw = models.BooleanField()
    political = models.BooleanField()
    sexist = models.BooleanField()
    safe = models.BooleanField()
    lang = models.CharField(max_length=10)

    def __str__(self):
        return self.joke if self.joke else f"{self.setup} - {self.delivery}"
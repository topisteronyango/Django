from django.db import models

# Create your models here.
class Schools(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self) -> str:
        return self.name


class Church(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self) -> str:
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self) -> str:
        return self.name

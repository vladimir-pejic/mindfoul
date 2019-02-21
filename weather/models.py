from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

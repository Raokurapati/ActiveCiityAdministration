from django.db import models


class CitizenModel(models.Model):
    name = models.CharField(max_length=100)



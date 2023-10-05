from django.db import models

class StreamElement(models.Model):
    value = models.IntegerField()
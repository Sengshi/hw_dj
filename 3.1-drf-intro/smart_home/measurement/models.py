import datetime

from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pk)


class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', related_name='measurements', on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=datetime.datetime.now())
    image = models.ImageField(upload_to='media/', blank=True, null=True)

from django.db import models


class socketioTable(models.Model):
    uniqueID = models.CharField(max_length=10)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    timestamp = models.CharField(max_length=30)

    def __str__(self):
        return self.uniqueID

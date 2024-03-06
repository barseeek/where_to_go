from django.db import models


class TourCompany(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.DecimalField(max_digits=20, decimal_places=15)
    lat = models.DecimalField(max_digits=20, decimal_places=15)

    def __str__(self):
        return self.title
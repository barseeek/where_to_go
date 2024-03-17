from django.db import models
from tinymce.models import HTMLField


class TourCompany(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', unique=True)
    short_description = models.TextField(blank=True, verbose_name='Краткое описание', default='')
    long_description = HTMLField(blank=True, verbose_name='Подробное описание', default='')
    lng = models.DecimalField(max_digits=20, decimal_places=15, verbose_name='Долгота')
    lat = models.DecimalField(max_digits=20, decimal_places=15, verbose_name='Широта')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.title


class TourImage(models.Model):
    tour_company = models.ForeignKey(TourCompany, related_name='images', on_delete=models.CASCADE, verbose_name='Локация')
    image = models.ImageField(verbose_name='Фото')
    position = models.PositiveIntegerField(verbose_name='Позиция', db_index=True, blank=True, default=0)

    class Meta:
        verbose_name = 'Фото локации'
        verbose_name_plural = 'Фото локаций'
        ordering = ('position',)

    def __str__(self):
        return f"{self.position} {self.tour_company.title}"

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField(blank=True)
    day = models.TextField(blank=True)
    month = models.TextField(blank=True)
    ftx = models.TextField(blank=True)
    waves = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Отчет'
        ordering = ['-created_at']



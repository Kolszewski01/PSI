from django.db import models
from django.utils import timezone

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        formatted_date = self.date.strftime('%Y-%m-%d %H:%M')
        return (f"[[CITY: {self.city.upper()}] [TEMPERATURE: {self.temperature}℃]"
                f" [HUMIDITY: {self.humidity}%] [CHANCE OF PRECIPITATION: {self.precipitation}%] "
                f"[{formatted_date}]]")
from django.db import models
from django.utils import timezone

class AirQuality(models.Model):
    quality_choices = [
        ('very_good', 'Very good'),
        ('good', 'Good'),
        ('moderate', 'Moderate'),
        ('sufficient', 'Sufficient'),
        ('poor', 'Poor'),
        ('very_poor', 'Very poor'),
    ]
    city = models.CharField(max_length=100)
    quality = models.CharField(max_length=20, choices=quality_choices, default='poor')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_date = self.date.strftime('%Y-%m-%d %H:%M')
        return f"[CITY: {self.city.upper()}] [AIR QUALITY: {self.get_quality_display().upper()}] [{formatted_date}]"
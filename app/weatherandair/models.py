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
        return (f"City: {self.city}, Temp: {self.temperature}°C, "
                f"Humidity: {self.humidity}%, Precipitation: {self.precipitation}%, Date: {formatted_date}")

class AirQuality(models.Model):
    quality_choices = [
        ('very_good', 'Very good'),
        ('good', 'Good'),
        ('moderate', 'Moderate'),
        ('sufficient', 'Sufficient'),
        ('poor', 'Poor'),
        ('very_poor', 'Very poor'),
    ]

    weather = models.OneToOneField(
        Weather,
        on_delete=models.CASCADE,
        related_name='air_quality',
        null=True,
        blank=True
    )
    quality = models.CharField(max_length=20, choices=quality_choices, default='poor')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        weather_info = f"Weather in: {self.weather.city}" if self.weather else "No Weather Info"
        return f"{weather_info}, Air Quality: {self.get_quality_display()}, Date: {self.date.strftime('%Y-%m-%d %H:%M')}"


    weather = models.OneToOneField(Weather, on_delete=models.CASCADE, related_name='air_quality')
    quality = models.CharField(max_length=20, choices=quality_choices, default='poor')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather in: {self.weather.city}, Air Quality: {self.get_quality_display()}, Date: {self.date.strftime('%Y-%m-%d %H:%M')}"

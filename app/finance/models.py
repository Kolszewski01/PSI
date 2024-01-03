from django.db import models
from django.utils import timezone

class Currency(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        formatted_datetime = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        return f"Currency: {self.name}, Rate: {self.rate} PLN, Date and Time: {formatted_datetime}"

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        formatted_datetime = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        return f"Cryptocurrency: {self.name}, Rate: {self.rate} PLN, Date and Time: {formatted_datetime}"

class Commodity(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        formatted_datetime = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        return f"Commodity: {self.name}, Rate: {self.rate} PLN, Date and Time: {formatted_datetime}"

class Stock(models.Model):
    company_name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        formatted_datetime = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        return f"Stock: {self.company_name}, Rate: {self.rate} PLN, Date and Time: {formatted_datetime}"

class Inflation(models.Model):
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        formatted_datetime = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        return f"Current Inflation Rate: {self.rate}% as of {formatted_datetime}"

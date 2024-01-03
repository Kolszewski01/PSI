from django.contrib import admin
from .models import Currency,Cryptocurrency,Commodity,Stock, Inflation

admin.site.register(Currency)
admin.site.register(Cryptocurrency)
admin.site.register(Commodity)
admin.site.register(Stock)
admin.site.register(Inflation)
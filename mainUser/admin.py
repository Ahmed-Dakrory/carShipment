from django.contrib import admin


from .models import profile
from .models import cars

# Register your models here.
admin.site.register(profile)
admin.site.register(cars)
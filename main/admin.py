from django.contrib import admin

from main.models import doctor, hospital, appointment

# Register your models here.
admin.site.register(hospital)
admin.site.register(doctor)
admin.site.register(appointment)

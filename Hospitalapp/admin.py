from django.contrib import admin
from Hospitalapp.models import Patient,Appointment,member

# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(member)
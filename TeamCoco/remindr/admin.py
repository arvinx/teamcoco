from django.contrib import admin
from remindr.models import Senior, Appointment, ReminderTime, Medication, Dosage

admin.site.register(Senior)
admin.site.register(Appointment)
admin.site.register(ReminderTime)
admin.site.register(Medication)
admin.site.register(Dosage)
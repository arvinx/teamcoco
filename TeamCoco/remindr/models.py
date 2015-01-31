from django.db import models


class Senior(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.IntegerField(default=0)


class Appointment(models.Model):
    time_added = models.DateTimeField('date added')
    time_to_take = models.DateTimeField('date to take medication')
    message = models.CharField(max_length=500)
    senior = models.ForeignKey(Senior, null=True)


class Medication(models.Model):
    name = models.CharField(max_length=40)
    dosage = models.IntegerField(default=0)
    # when the repeat starts
    start_time = models.DateTimeField(auto_now=True)
    # when the repeat ends? can it be null?
    end_time = models.DateTimeField(auto_now=False)
    frequency = models.IntegerField(default=0)
    #freq evenly spread out on freq_unit
    frequency_unit = models.CharField(default="hour", max_length=10)
    appointment = models.ForeignKey(Appointment)


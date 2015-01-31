from django.db import models


class Senior(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.IntegerField(default=0)


class Appointment(models.Model):
    message = models.CharField(max_length=500)
    senior = models.ForeignKey(Senior, null=True)

    # when the repeat starts
    start_date = models.DateField(auto_now=True)
    # when the repeat ends? can it be null?
    end_date = models.DateField(auto_now=False)
    #freq evenly spread out on freq_unit
    frequency_unit = models.CharField(default="hour", max_length=10)


class ReminderTime(models.Model):
    #derived from start_date + user input in form for list of times
    time_to_take = models.DateTimeField('date to take medication')
    appointment = models.ForeignKey(Appointment)


class Medication(models.Model):
    name = models.CharField(max_length=40)
    dosage_amount = models.IntegerField(default=0)
    dosage_unit = models.CharField(max_length=10)
    senior = models.ForeignKey(Senior, null=True)

    def __str__(self):
        return self.name

class Dosage(models.Model):
    appointment = models.ForeignKey(Appointment)
    medication = models.ForeignKey(Medication)



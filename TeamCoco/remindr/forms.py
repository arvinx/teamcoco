from django import forms

from remindr.models import Medication

class SeniorForm(forms.Form):
    name = forms.CharField(label='name', max_length=40)
    phone_number = forms.CharField(label='phone_number')

class MedicationForm(forms.Form):
    name = forms.CharField(label='name', max_length=40)
    dosage_amount = forms.IntegerField(label='dosage_amount')
    dosage_unit = forms.CharField(label='dosage_unit', max_length=10)


class AppointmentForm(forms.Form):
    time_to_take = forms.TimeField()
    message = forms.CharField()

    medications = forms.ModelMultipleChoiceField(queryset=Medication.objects.all())
    recurring = forms.BooleanField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    FREQUENCY_CHOICES = (('Daily', 'Daily'), ('Hourly', 'Hourly'),)
    frequency_unit = forms.ChoiceField(choices=FREQUENCY_CHOICES)

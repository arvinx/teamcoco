from django import forms

from remindr.models import Medication
from widgets import SelectTimeWidget
from django.forms.extras.widgets import SelectDateWidget

class SeniorForm(forms.Form):
    name = forms.CharField(label='name', max_length=40)
    phone_number = forms.CharField(label='phone_number')

class MedicationForm(forms.Form):
    name = forms.CharField(label='name', max_length=40)
    dosage_amount = forms.IntegerField(label='dosage_amount')
    dosage_unit = forms.CharField(label='dosage_unit', max_length=10)


class AppointmentForm(forms.Form):
    time_to_take = forms.TimeField(widget=SelectTimeWidget(twelve_hr=True, minute_step=10))
    message = forms.CharField()

    medications = forms.ModelMultipleChoiceField(queryset=Medication.objects.all())
    recurring = forms.BooleanField()
    start_date = forms.DateField(widget=SelectDateWidget)
    end_date = forms.DateField(widget=SelectDateWidget)
    FREQUENCY_CHOICES = (('Daily', 'Daily'), ('Weekly', 'Weekly'),)
    frequency_unit = forms.ChoiceField(choices=FREQUENCY_CHOICES)

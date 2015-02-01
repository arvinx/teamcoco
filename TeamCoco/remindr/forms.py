from django import forms

from remindr.models import Medication
from widgets import SelectTimeWidget
from django.forms.extras.widgets import SelectDateWidget

class SeniorForm(forms.Form):
    name = forms.CharField(label='name', max_length=40, widget=forms.TextInput(attrs={'class':'xwide text input'}))
    phone_number = forms.CharField(label='phone_number', widget=forms.TextInput(attrs={'class':'xwide text input'}))

class MedicationForm(forms.Form):
    name = forms.CharField(label='name', max_length=40,  widget=forms.TextInput(attrs={'class':'xwide text input'}))
    dosage_amount = forms.IntegerField(label='dosage_amount', widget=forms.NumberInput(attrs={'class':'xwide text input'}))
    dosage_unit = forms.CharField(label='dosage_unit', max_length=10, widget=forms.TextInput(attrs={'class':'xwide text input'}))


class AppointmentForm(forms.Form):
    time_to_take = forms.TimeField(widget=SelectTimeWidget(twelve_hr=True, minute_step=10, attrs={'class':'yolo'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class':'xwide text input'}))
    medications = forms.ModelMultipleChoiceField(queryset=Medication.objects.all(), widget=forms.SelectMultiple(attrs={'class':'medication'}))
    recurring = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    start_date = forms.DateField(widget=SelectDateWidget())
    end_date = forms.DateField(widget=SelectDateWidget(), required=False)
    FREQUENCY_CHOICES = (('Daily', 'Daily'), ('Weekly', 'Weekly'),)
    frequency_unit = forms.ChoiceField(choices=FREQUENCY_CHOICES, widget=forms.Select(), required=False)
    REMINDER_METHODS = (('Phone', 'Phone'), ('Text', 'Text'), ('Both', 'Both'))
    reminder_method = forms.ChoiceField(choices=REMINDER_METHODS, widget=forms.Select(), required=False)

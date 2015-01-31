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
    message = forms.Textarea()

    medications = forms.ModelMultipleChoiceField(queryset=Medication.objects.all())
    start_time = forms.DateTimeField(label='start_time')
    end_time = forms.DateTimeField(label='end_time')
    frequency = forms.IntegerField(label='frequency')
    frequency_unit = forms.CharField(label='frequency_unit')
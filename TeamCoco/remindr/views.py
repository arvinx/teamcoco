from django.conf import settings

import twilio
from twilio.rest import TwilioRestClient
import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from forms import SeniorForm, MedicationForm, AppointmentForm

from remindr.models import Senior, Appointment, Medication, ReminderTime, Dosage


def senior_index(request):
    senior_lst = Senior.objects.all()
    form = SeniorForm()
    context = {'senior_lst': senior_lst, 'form': form}
    return render(request, 'remindr/index.html', context)

def senior(request, senior_id=None):

    if request.method == 'GET':
        senior = get_object_or_404(Senior, pk=senior_id)
        medicationForm = MedicationForm()
        appointmentForm = AppointmentForm()
        return render(request, 'remindr/senior.html', {'medicationForm': medicationForm,
                                                       'appointmentForm' : appointmentForm,
                                                     'senior': senior,
                                                     'appointments_lst': senior.appointment_set.all(),
                                                     'medication_lst': senior.medication_set.all()})
    else:
        pass
        #delete

def add_senior(request):
    if request.method == 'POST':
        form = SeniorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            senior = Senior(name=name, phone_number=phone_number)
            senior.save()

            client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

            # Make the call
            client.messages.create(
                body="Welcome to Med-member, %s! - Team CoCo" % name,
                to=senior.phone_number,
                from_=settings.TWILIO_PHONE_NUMBER)

            return HttpResponseRedirect('/remindr/')

def add_medication(request, senior_id = None):
    if request.method == 'POST':
        #senior_id = request.POST['senior_id']
        senior = get_object_or_404(Senior, pk=senior_id)
        form = MedicationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dosage_amount = form.cleaned_data['dosage_amount']
            dosage_unit = form.cleaned_data['dosage_unit']
            medication = Medication(name=name, dosage_amount=dosage_amount, dosage_unit=dosage_unit, senior=senior)
            medication.save()
    return HttpResponseRedirect('/remindr/')

def add_appointment(request, senior_id=None):
    if request.method == 'POST':
        senior = get_object_or_404(Senior, pk=senior_id)
        form = AppointmentForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            frequency_unit = form.cleaned_data['frequency_unit']
            newAppointment = Appointment(message=message, senior=senior, start_date=start_date, end_date=end_date,
                                         frequency_unit=frequency_unit)
            newAppointment.save()


            for medication in form.cleaned_data['medications']:
                newDosage = Dosage(appointment=newAppointment, medication=medication)
                newDosage.save()

            curr_date = start_date
            time_to_take = form.cleaned_data['time_to_take']

            if form.cleaned_data['recurring']:
                if frequency_unit == 'Daily':
                    timestep = datetime.timedelta(days=1)
                elif frequency_unit == 'Weekly':
                    timestep = datetime.timedelta(weeks=1)

                while curr_date <= end_date:
                    reminderT = datetime.datetime(year=curr_date.year, month=curr_date.month, day=curr_date.day,
                                                  hour=time_to_take.hour, minute=time_to_take.minute)
                    newReminderTime = ReminderTime(time_to_take=reminderT, appointment=newAppointment)
                    newReminderTime.save()
                    curr_date += timestep
            else:
                newReminderTime = ReminderTime(time_to_take=datetime.datetime(year=curr_date.year, month=curr_date.month, day=curr_date.day,
                                                  hour=time_to_take.hour, minute=time_to_take.minute), appointment=newAppointment)
                newReminderTime.save()

    return HttpResponseRedirect('/remindr/')

# def senior_delete(request, senior_id):
#     pass
#
#
# def senior_edit(request, senior_id):
#     pass

def completed(request):
    sent = send_twilio_message('6473399467', 'ayyy')
    return HttpResponse("status " + sent.status)

def appointment(request, senior_id=None, appointment_id=None):

    return HttpResponse("appointment page")



def send_twilio_message(to_number, body):
    client = twilio.rest.TwilioRestClient(
        settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    return client.messages.create(
        body=body,
        to=to_number,
        from_=settings.TWILIO_PHONE_NUMBER
    )
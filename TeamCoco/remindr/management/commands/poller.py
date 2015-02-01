import datetime
import urllib
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from twilio.rest import TwilioRestClient
from remindr.models import ReminderTime, Appointment


class Command(BaseCommand):
    def makeCall(self, reminder):
        # time to send twilio request
        slow_msg = ". ".join(reminder.appointment.message.split())
        menu_msg = ". Please press 1 to call to Nathan if you need help taking your medication"
        slow_msg += menu_msg
        params = urllib.urlencode(
            {'Message': slow_msg, "Options[1]": "http://twimlets.com/forward?PhoneNumber=6473399467"})
        twimlets_url = urllib.urlopen("http://twimlets.com/menu?%s" % params).url
        client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        # Make the call
        call = client.calls.create(to=reminder.appointment.senior.phone_number,  # Any phone number
                                   from_=settings.TWILIO_PHONE_NUMBER,  # Must be a valid Twilio number
                                   url=twimlets_url)


    def sendText(self, reminder):
        client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(to=reminder.appointment.senior.phone_number, from_=settings.TWILIO_PHONE_NUMBER,
                                     body=reminder.appointment.message)


    def handle(self, *args, **options):
        cur_time = datetime.datetime.now()
        reminders = ReminderTime.objects.filter(time_to_take__lte=cur_time)

        for reminder in reminders:
            if reminder.method == 'Phone':
                self.makeCall(reminder)
            if reminder.method == 'Text':
                self.sendText(reminder)
            if reminder.method == 'Both':
                self.makeCall(reminder)
                self.sendText(reminder)
            reminder.delete()


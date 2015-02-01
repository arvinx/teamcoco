import datetime
import urllib
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from twilio.rest import TwilioRestClient
from remindr.models import ReminderTime, Appointment


class Command(BaseCommand):
    def handle(self, *args, **options):
        cur_time = datetime.datetime.now()
        reminders = ReminderTime.objects.filter(time_to_take__lte=cur_time)

        for reminder in reminders:
            #time to send twilio request
            slow_msg = ". ".join(reminder.appointment.message.split())
            params = urllib.urlencode({'Message[0]': slow_msg})
            twimlets_url = urllib.urlopen("http://twimlets.com/message?%s" % params).url
            print twimlets_url
            # Download the library from twilio.com/docs/libraries


            client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

            # Make the call
            call = client.calls.create(to=reminder.appointment.senior.phone_number,  # Any phone number
                                       from_=settings.TWILIO_PHONE_NUMBER, # Must be a valid Twilio number
                                       url=twimlets_url)

            reminder.delete()



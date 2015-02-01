from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_twilio.views import message

from remindr import views

urlpatterns = patterns('',
    url(r'^$', views.senior_index, name='senior_index'),
    url(r'^senior/add/$', views.add_senior, name='add_senior'),
    url(r'^senior/(?P<senior_id>\d+)/$', views.senior, name='senior'),
    url(r'^senior/(?P<senior_id>\d+)/appointment/add/$', views.add_appointment, name='add_appointment'),
    url(r'^senior/(?P<senior_id>\d+)/appointment/(?P<appointment_id>\d+)/$', views.appointment, name='appointment'),
    url(r'^senior/(?P<senior_id>\d+)/medication/add/$', views.add_medication, name='add_medication'),
    url(r'^senior/reminders/json/$', views.getReminderTimes, name='get_reminders'),
    url(r'^senior/medications/json/$', views.getMedication, name='get_medication'),
    url(r'^reminder/details/$', views.getReminderDetails, name="get_reminder_details"),
    url(r'^reminder/(?P<reminder_id>\d+)/delete$', views.deleteReminder, name='delete_reminder'),
    # url(r'^(?P<senior_id>\d+)/senior/edit/$', views.senior_edit, name='senior_edit'),
    url(r'^message/completed/$', views.completed, name='completed'),
    url(r'^message/$', 'django_twilio.views.message', {
        'message': 'Yo!',
        'to': '6473399467',
        'status_callback': '/message/completed/',
    }),

)

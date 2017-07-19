from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from members.models import Member
from events.models import EventAttendance

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#check everyday at noon
class Command(BaseCommand):
	help = 'Checks if memebrship is expiring and emails member'

	def handle(self, *args, **options):

		now = timezone.now().date()
		start = now + timezone.timedelta(days=3)
		end = now + timezone.timedelta(days=4)
		
		#print(days)
		attendance_list = EventAttendance.objects.filter(event__start__range=(start,end)) 

		for attendee in attendance_list:

			print(attendee)

			
			subject = "Upcoming Event Reminder"
			message = render_to_string("events/event_reminder_email.html", {'attendee': attendee})
			subject, from_email, to = subject, settings.DEFAULT_FROM_EMAIL, attendee.member.user.email
			
			html_content = message
			text_content = strip_tags(message)
			
			msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			
		
			try:
				if settings.DEBUG:
					self.stdout.write(self.style.SUCCESS('DEBUG: Event Reminder Email Sent to: "%s"' % member))
				else:
					msg.send()
					self.stdout.write(self.style.SUCCESS('Event Reminder Email Sent to: "%s"' % attendee.member))
			except Exception as e:
				print(e)
				self.stdout.write(self.style.ERROR('Event Reminder Email FAILED: "%s"' % e))
			

			
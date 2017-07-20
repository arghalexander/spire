from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from members.models import Member
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

		now = timezone.now()
		members = Member.objects.filter(membership_expiration__gte=now, membership_expiration__lte=now + timezone.timedelta(days=30), membership_level__expires=True)

		for member in members:
			print(member)
			days_left = member.membership_expiration - now
			days_left += timezone.timedelta(days=1)

			#only send reminder if 30 and 7 days remaining
			if(days_left.days == 30 or days_left.days == 7):

				subject = "Your membership will expire soon"
				message = render_to_string("members/membership_expiration_email.html", {'days': days_left.days})
				subject, from_email, to = subject, settings.DEFAULT_FROM_EMAIL, member.user.email
				
				html_content = message
				text_content = strip_tags(message)
				

				msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
				msg.attach_alternative(html_content, "text/html")
				
			
				try:
					if settings.DEBUG:
						self.stdout.write(self.style.SUCCESS('DEBUG: Membership Expiration Email Sent to: "%s"' % member))
					else:
						#msg.send()
						self.stdout.write(self.style.SUCCESS('Membership Expiration Email Sent to: "%s"' % member))
				except Exception as e:
					print(e)
					self.stdout.write(self.style.ERROR('Membership Expiration Email FAILED: "%s"' % e))
			
			

			
from __future__ import unicode_literals
import logging

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ValidationError

from core.models import TimeStampedModel
from mailinglist.models import MailContact

# Get an instance of a logger
logger = logging.getLogger(__name__)

@python_2_unicode_compatible  # only if you need to support Python 2
class Fact(TimeStampedModel):

	fact_title = models.CharField(max_length=200)
	fact_text = models.CharField(max_length=2000)
	pub_date = models.DateTimeField('date published')
	send_email_on_save = models.BooleanField(default=False)

	def __str__(self):
		return self.fact_title

	def clean(self):
		if self.send_email_on_save and self.pub_date > timezone.now():
			raise ValidationError('We cannot send emails for future publication dates, as the fact will not be publicly visible.')
		

	def save(self, *args, **kwargs):
		"""
		Overide save to include option to send an email all mailing list members.
		"""
		super(Fact, self).save(*args, **kwargs) # Call the "real" save() method.
		
		if self.send_email_on_save and self.pub_date < timezone.now():
			self.send_email_on_save = False # Set to true to disable emails on future saves (unless user overides)
			recipients = MailContact.objects.values_list('email', flat=True) # get all mailing list recipients as a list.
			for recipient in recipients:
				subject, from_email, to = 'New fact of the week', 'from@example.com', recipient
				text_content = "Hi, We've just published a new fact. Check it out here {}".format("http://factoftheweek.com")
				html_content = "<p>Hi, We've just published a new fact. Check it out here {}</p>".format("http://factoftheweek.com")
				msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
				msg.attach_alternative(html_content, "text/html")
				try:
					msg.send()
					logger.info('Email sent to mailing list recipients for fact: {}.'.format(self.fact_title))
				except:
					logger.error('Email cannot be sent for fact: {}.'.format(self.fact_title))
				
			
		
		
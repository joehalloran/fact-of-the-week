from __future__ import unicode_literals
from datetime import timedelta
import logging

from django.db import models
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from core.models import TimeStampedModel
from .validators import validate_terms_accepted

# Get an instance of a logger
logger = logging.getLogger(__name__)

@python_2_unicode_compatible  # only if you need to support Python 2
class MailContact(TimeStampedModel):

	first_name = models.CharField(max_length=60)
	second_name = models.CharField(max_length=60)
	email = models.EmailField(unique=True)
	terms_accepted = models.BooleanField(default=False, blank=False, validators=[validate_terms_accepted])
	delete_key = models.CharField(max_length=32, blank=True, null=True)
	delete_timestamp = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return "{} {}".format(self.first_name, self.second_name)

	def delete(self, *args, **kwargs):
		"""
		Overide to send confirmation email to users.
		"""
		super(MailContact, self).delete(*args, **kwargs) # Call the "real" save() method.		
		recipient = self.email
		try:
			send_mail(
				"We are sorry to see you go", 
				"Hi {}, we have removed you from our mailing list.".format(self.first_name),
				'from@example.com',
				[recipient],
			)
			logger.info('Email was sent to user to confirm mailing list removal.')
		except:
			logger.error('Email could not be sent to user to confirm mailing list removal.')

	def recent_delete_ts(self):
		"""
		Check if delete_timestamp was created in the last 30mins
		"""
		if self.delete_key and self.delete_timestamp:
			return self.delete_timestamp > (timezone.now() - timedelta(minutes=10))

from __future__ import unicode_literals
import logging

from django.db import models
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.utils.encoding import python_2_unicode_compatible

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
				"Please don't go", 
				"Hi {}, we have removed you from our mailing list.".format(self.first_name),
				'from@example.com',
				[recipient],
			)
			logger.info('Email was sent to user to confirm mailing list removal.')
		except:
			logger.error('Email could not be sent to user to confirm mailing list removal.')
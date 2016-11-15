from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.core.mail import send_mass_mail

from core.models import TimeStampedModel
from mailinglist.models import MailContact

@python_2_unicode_compatible  # only if you need to support Python 2
class Fact(TimeStampedModel):
    fact_title = models.CharField(max_length=200)
    fact_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    send_email_on_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.fact_title

    def save(self, *args, **kwargs):
    	if self.send_email_on_publish and self.pub_date < timezone.now():
    		self.send_email_on_publish = True 
    		recipients = MailContact.objects.values_list('email', flat=True)
    		print recipients # TO DO CHECK THIS IS CORRECT FORMAT
    		message = (
    			'New fact of the week', 
    			"Hi, We've just published a new fact. Check it out here {}".format("http://factofthweek.com"),
    			'from@example.com',
    			recipients)
    		send_mass_mail((message), fail_silently=False)
    	super(Fact, self).save(*args, **kwargs) # Call the "real" save() method.
        
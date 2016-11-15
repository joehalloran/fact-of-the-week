from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

from core.models import TimeStampedModel
from .validators import validate_terms_accepted

@python_2_unicode_compatible  # only if you need to support Python 2
class MailContact(TimeStampedModel):

    first_name = models.CharField(max_length=60)
    second_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    terms_accepted = models.BooleanField(default=False, blank=False, validators=[validate_terms_accepted])

    def __str__(self):
        return "{} {}".format(self.first_name, self.second_name)

    def get_absolute_url(self):
    	return reverse("mailinglist:thanks")
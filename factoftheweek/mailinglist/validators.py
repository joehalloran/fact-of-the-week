from django.core.exceptions import ValidationError

def validate_terms_accepted(value):
	"""Raise a validation error if terms and condinitions not accepted.
	"""

	if not value == True:
		msg = u"Please accept the terms and conditions to proceed."
		raise ValidationError(msg)

from datetime import timedelta

from django.core import mail
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from .models import Fact
from mailinglist.models import MailContact

# models test
class FactsModelsTest(TestCase):

	def create_fact(
			self, 
			fact_title = "only a test", 
			fact_text = "yes, this is only a test",
			pub_date = timezone.now(),
			send_email = False ):
		return Fact.objects.create(
				fact_title = fact_title,
				fact_text = fact_text,
				pub_date = pub_date,
				send_email_on_save = send_email )

	def create_past_fact_with_email(self):
		return self.create_fact(pub_date = (timezone.now() - timedelta(days=30)), send_email = True )

	def create_future_fact_with_email(self):
		return self.create_fact(pub_date = (timezone.now() + timedelta(days=30)), send_email = True )

	def create_mail_recipient(self):
		return MailContact.objects.create(
				first_name='Joe',
				second_name='Bloggs',
				email='from@example.com',
				terms_accepted=True )

	def test_fact_creation(self):
		f = self.create_fact()
		self.assertTrue(isinstance(f, Fact))
		self.assertEqual(f.__unicode__(), f.fact_title)

	def test_future_fact_validation(self):
		f = self.create_future_fact_with_email()
		self.assertRaises(ValidationError, f.clean)

	def test_past_fact_send_email(self):
		g = self.create_mail_recipient()
		f = self.create_past_fact_with_email()
		self.assertEqual(len(mail.outbox), 1)
		self.assertIn('New fact', mail.outbox[0].subject)
		self.assertIn('factoftheweek.com', mail.outbox[0].body)
	
	def test_past_fact_set_send_to_false(self):
		f = self.create_past_fact_with_email()
		self.assertEqual(f.send_email_on_save, False)
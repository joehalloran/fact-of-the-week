from datetime import timedelta

from django.core import mail
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from .models import MailContact

# models test
class MailContactModelsTest(TestCase):

	def setUp(self):
		MailContact.objects.create(
			first_name="Joe", 
			second_name="Bloggs",
			email="joebloggs@example.com", 
			terms_accepted = True)

	def test_mail_contact_creation(self):
		p = MailContact.objects.get(first_name="Joe")
		self.assertTrue(isinstance(p, MailContact))
		self.assertEqual(p.__unicode__(), "{} {}".format(p.first_name, p.second_name))

	def test_mail_contact_email_on_delete(self):
		p = MailContact.objects.get(first_name="Joe")
		p.delete()
		self.assertEqual(len(mail.outbox), 1)
		self.assertIn("see you go", mail.outbox[0].subject)
		self.assertIn('removed you from our mailing list', mail.outbox[0].body)
	
	def test_mail_terms_accepted_validation(self):
		p = MailContact.objects.get(first_name="Joe")
		p.terms_accepted = False
		self.assertRaises(ValidationError, p.full_clean)

	def test_recent_delete_ts_no_values(self):
		p = MailContact.objects.get(first_name="Joe")
		self.assertFalse(p.recent_delete_ts())

	def test_recent_delete_ts_with_timestamp_and_no_dk(self):
		p = MailContact.objects.get(first_name="Joe")
		p.delete_timestamp = timezone.now()
		p.save()
		self.assertFalse(p.recent_delete_ts())

	def test_recent_delete_ts_valid_timestamp_and_dk(self):
		p = MailContact.objects.get(first_name="Joe")
		p.delete_key = "placeholderString"
		p.delete_timestamp = timezone.now()
		p.save()
		self.assertTrue(p.recent_delete_ts())

	def test_recent_delete_ts_old_timestamp_and_dk(self):
		p = MailContact.objects.get(first_name="Joe")
		p.delete_key = "placeholderString"
		p.delete_timestamp = timezone.now() - timedelta(minutes=11)
		p.save()
		self.assertFalse(p.recent_delete_ts())



		
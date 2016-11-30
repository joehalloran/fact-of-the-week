from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError


from .models import MailContact
from .forms import Unsubscribe

# forms test
class MailingListFormsTest(TestCase):

	def setUp(self):
		MailContact.objects.create(
			first_name="Joe", 
			second_name="Bloggs",
			email="joebloggs@example.com", 
			terms_accepted = True)

	def test_unsubscribe_form(self):
		"""
		Test validation for unsubscribe form - valid email.
		"""
		form_data = {'email': 'joebloggs@example.com'}
		form = Unsubscribe(data=form_data)
		self.assertTrue(form.is_valid())

	def test_unsubscribe_form_wrong_email(self):
		"""
		Test validation for unsubscribe form - invalid email.
		"""
		form_data = {'email': 'something'}
		form = Unsubscribe(data=form_data)
		self.assertFalse(form.is_valid())
		self.assertIsNotNone(form.errors['email'])

	def test_mail_create_view_redirect(self):
		"""
		Test create view form accepts input and redirect with success message.
		"""
		form_data = {
			'first_name':'Jane', 
			'second_name':'Bloggs',
			'email':"janebloggs@example.com",
			'terms_accepted':True
			}
		response = self.client.post(reverse('mailinglist:join'), form_data, follow=True)
		self.assertRedirects(response, reverse('home'))
		self.assertContains(response, 'was created successfully')
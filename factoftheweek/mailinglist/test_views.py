from django.test import TestCase
from django.urls import reverse

from .models import MailContact

# views test
class MailingListViewsTest(TestCase):

	def setUp(self):
		MailContact.objects.create(
			first_name="Joe", 
			second_name="Bloggs",
			email="joebloggs@example.com", 
			terms_accepted = True)

	def test_mailing_list_join_view(self):
		"""
		Test join mailing form contains all fields.
		"""
		url = reverse('mailinglist:join')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "First name")
		self.assertContains(response, "Second name")
		self.assertContains(response, "Email")
		self.assertContains(response, "Terms accepted")
		
	def test_mailing_list_unsubscribe(self):
		"""
		Test unsubscribe view returns and contains field title.
		"""
		url = reverse('mailinglist:unsubscribe')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Unsubscribe")


	def test_mailing_list_unsubscribe_confirm_email_exists(self):
		"""
		Test unsubscribe confirm for valid user id
		"""
		p = MailContact.objects.get(first_name="Joe")
		url = reverse('mailinglist:unsubscribe-confirm', kwargs={'pk':p.id})
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Unsubscribe")

	def test_mailing_list_unsubscribe_user_does_not_exist(self):
		"""
		Test unsubscribe confirm for invalid user id
		"""
		url = reverse('mailinglist:unsubscribe-confirm', kwargs={'pk':1000})
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)

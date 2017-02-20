from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Fact

#Fact views test
class FactsViewsTest(TestCase):

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

	def create_many_facts(self):
		for i in range(10):
			self.create_fact(fact_title = "only a test " + str(i), pub_date = timezone.now() - timedelta(days=i) )
		self.create_fact(fact_title = 'future fact',  pub_date = timezone.now() + timedelta(days=1) )
		
	def test_fact_home_view(self):
		self.create_many_facts()
		url = reverse('home')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "only a test 3")
		self.assertNotContains(response, "only a test 4")
		self.assertNotContains(response, "future fact")
		
	def test_fact_index_view(self):
		self.create_many_facts()
		url = reverse('facts:index')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "only a test 9")
		self.assertNotContains(response, "future fact")

	def test_fact_detail_view(self): 
		self.create_fact()
		f= Fact.objects.get(fact_title="only a test")
		url = reverse('facts:detail', args=[f.id])
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "only a test")
	
	def test_future_fact_detail_view(self): 
		self.create_many_facts()
		url = reverse('facts:detail', args=[11])
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)


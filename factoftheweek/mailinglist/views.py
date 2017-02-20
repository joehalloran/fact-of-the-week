from os import urandom

from django.views.generic import CreateView, DeleteView, FormView
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_admins
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils import timezone

from .models import MailContact
from .forms import MailContactCreateForm, Unsubscribe

class Join(SuccessMessageMixin, CreateView):
	template_name = 'mailinglist/mailcontact_form.html'
	form_class = MailContactCreateForm
	success_url = reverse_lazy('home')
	success_message = "Thank you. Your application to join our mailing list will be reviewed by the Fact of the week team."

	def form_valid(self, form):
		"""
		Email admins to inform them of the new mailing list application.
		"""
		mail_admins(subject = "New mailing list application", message = "Someone has applied to join to Fact of the week mailing list.")
		return super(Join, self).form_valid(form)

class Unsubscribe(FormView):
	template_name = 'mailinglist/unsubscribe.html'
	form_class = Unsubscribe

	def form_valid(self, form):
		"""
		Find email address (existence in db validated by .forms.unsubscribe.clean_email),
		get contact from db, and redirects to Unsubscribe Confirm with contact id
		"""
		email = form.cleaned_data['email']
		contact = MailContact.objects.get(email= email)
		contact.delete_key = urandom(12).encode('hex') # Generate random delete key
		contact.delete_timestamp = timezone.now()
		contact.save()
		# Generate unique link using delete_key as query paramenter value
		return HttpResponseRedirect(reverse('mailinglist:unsubscribe-confirm', kwargs={'pk':contact.id})+'?dk='+contact.delete_key)
		
class UnsubscribeConfirm(DeleteView):
	model = MailContact
	success_url = reverse_lazy('home')
	success_message = "Your contact details were deleted successfully."

	def get(self, request, *args, **kwargs):
		"""
		Ensure url is valid by matchine object dk (delete_key) that of query parameter value and checking recent timestamp
		"""
		self.object = self.get_object()
		dk = request.GET.get('dk')
		if self.object.delete_key != dk and self.object.recent_delete_ts():
			raise Http404
		return super(UnsubscribeConfirm, self).get(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		"""
		Work around as SuccessMessageMixin does not work with DeleteView
		"""	
		messages.success(self.request, self.success_message)
		return super(UnsubscribeConfirm, self).delete(request, *args, **kwargs)



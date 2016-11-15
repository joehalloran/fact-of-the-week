from django.views.generic import CreateView, DeleteView, FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import MailContact
from .forms import MailContactCreateForm, Unsubscribe

class Join(SuccessMessageMixin, CreateView):
	template_name = 'mailinglist/mailcontact_form.html'
	form_class = MailContactCreateForm
	success_url = reverse_lazy('home')
	success_message = "%(email)s was created successfully"

class Unsubscribe(FormView):
	template_name = 'mailinglist/unsubscribe.html'
	form_class = Unsubscribe
	success_url = reverse_lazy('mailinglist:thanks')

	def form_valid(self, form):
		"""Find email address (existence in db confirmed by .forms.unsubscribe.clean_email),
		get contact from db, and redirects to Unsubscribe Confirm with contact id
		"""
		email = form.cleaned_data['email']
		contact = MailContact.objects.get(email= email)
		return HttpResponseRedirect(reverse('mailinglist:unsubscribe-confirm', args=(contact.id,)))
		
class UnsubscribeConfirm(DeleteView):
	model = MailContact
	success_url = reverse_lazy('home')
	success_message = "Your contact details were deleted successfully."

	def delete(self, request, *args, **kwargs):
		# SuccessMessageMixin does not work with DeleteView
		messages.success(self.request, self.success_message)
		return super(UnsubscribeConfirm, self).delete(request, *args, **kwargs)
from django import forms
from django.utils.translation import string_concat
from django.core.urlresolvers import reverse_lazy

from .models import MailContact

class MailContactCreateForm(forms.ModelForm):
   
    class Meta:
        model = MailContact
        fields = ['first_name', 'second_name', 'email' ,'terms_accepted']
        widgets = {
           
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'terms_accepted': forms.CheckboxInput(attrs = {'required': True}) 
        }
        help_texts = {
            # Using string_concat to allow reverse_lazy (otherwise reverse_lazy tries to resolve before django loads urls config)
        	'terms_accepted': string_concat( 
                u'I agree to the  <a href="', 
                reverse_lazy("mailinglist:terms"),
                u'">terms of service</a>',
            )
        }

class Unsubscribe(forms.Form):
   
    email = forms.CharField(
    		label='Your email', 
			max_length=100, 
            # .form-control is for Bootstrap framework css
	    	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    	)

    def clean_email(self):
		email = self.cleaned_data['email']
		try:
			MailContact.objects.get(email= email)
		except MailContact.DoesNotExist:
			msg = u"This email address is not registered."
			raise forms.ValidationError(msg)
		return email
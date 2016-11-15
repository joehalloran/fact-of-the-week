from django import forms
from django.utils.safestring import mark_safe

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
        	'terms_accepted': mark_safe('I agree to the <a href="{}">terms of service</a>'.format('../thanks/'))
        }

class Unsubscribe(forms.Form):
   
    email = forms.CharField(
    		label='Your email', 
			max_length=100, 
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
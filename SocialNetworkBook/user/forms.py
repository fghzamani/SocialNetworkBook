from django.forms import ModelForm, forms
from .models import Profile


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError('@ not in email')
        return email

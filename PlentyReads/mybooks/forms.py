import re
from django import forms
# from django.contrib.auth.models import User
from .models import User
from django.utils.translation import ugettext_lazy as _
import datetime

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'name', 'email','password'}
        # fields = "__all__"
    #     exclude = {'ActiveYN', 'create_date'}
    # name = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    # email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    # ActiveYN = 'Y'
    # create_date = datetime.datetime.now()

    def __unicode__(self):
            return self.email

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("The email already exists. Please try another one."))
 
    # def clean(self):
    #     if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
    #         if self.cleaned_data['password1'] != self.cleaned_data['password2']:
    #             raise forms.ValidationError(_("The two password fields did not match."))
    #     return self.cleaned_data

class LoginForm(forms.Form):
    
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput())
    
    def __unicode__(self):
            return self.name

    def clean_username(self):
        try:
            email = User.objects.get(username__iexact=self.cleaned_data['email'])
        except email.DoesNotExist:
            return "Email not registered"
 
class ProfileForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = {'password'}
    
    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
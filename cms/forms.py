from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from cms.models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ["category", "subject", "details"]

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label="Existing Password")
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label="Confirm Password")

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError("Existing password is incorrect.")
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("New passwords do not match.")
        return cleaned_data

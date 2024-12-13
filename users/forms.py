from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from allauth.account.forms import SignupForm
from .models import User


"""
Form for editing own profile.
"""
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'avatar']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Profile'))


"""
Custom form for sugning up with possibility to attach an avatar.
"""
class CustomSignupForm(SignupForm):
    avatar = forms.ImageField(
        required=False, 
        label="Avatar (optional)"
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.avatar = self.cleaned_data.get('avatar')
        user.save()
        return user
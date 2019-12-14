from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
# from PostCity.models import PostCity #added
from apps.accounts.models import User, Location



# Add a Location ----------------------------------------------------------

class NewLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('city', 'us_state', 'country')


####### auto generated classes below ###########

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'bio',
            'phone',
        )

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'phone',
            'password1',
            'password2',
        )

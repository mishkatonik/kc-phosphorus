from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
# from PostCity.models import PostCity #added
from apps.accounts.models import User



# class PostCity(forms.ModelForm):
#     class Meta():
#         model = PostCity
#         fields = '__all__'


####### auto generated classes below ###########

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'bio',
        )

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

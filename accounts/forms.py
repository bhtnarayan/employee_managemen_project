from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from django import forms 


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email")


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            
            
        }




from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms  #ata holo tarjonno jeta amra shobgulo widget nie kaj korte hole lage 


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'reqiured'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'reqiured'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'reqiured'}))
    class Meta:
        model = User
        # fields = '__all__'  (ata dile from ar shob ashbe)
        fields = ['username', 'first_name', 'last_name', 'email']

class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']        
from typing import Any
from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="Full Name: ", help_text="Total length must be within 70.", required=False, widget=forms.Textarea(attrs={'id':'text_area', 'class':'class1' 'class2', 'placeholder':'Enter yours name '}) )
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # wight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    check = forms.BooleanField()
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICE = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICE, widget=forms.RadioSelect)
    MEAL = [('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    # file = forms.FileField()

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)
 # valitation dui babe kora jay first 1st :
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 character.")
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must be contain .com")
    #     return valemail

 # valitation dui babe kora jay seconde 2nd:
    # def clean(self):
    #     clean_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 character.")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must be contain .com")
    
    
#some Built in Form validators
class student_Data(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10, message='Enter a name with maximum 10 character.')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34,message='age must be under the 34.'), validators.MinValueValidator(24, message='age must be at least 24.')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a vlaid Email.')]) 
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message='File extention must be accurete.')])   
            
class passwordvalidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)           
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    # def clean(self):
    #     clean_data = super().clean()
    #     val_pass = self.cleaned_data["password"]
    #     val_conpas = self.cleaned_data['confirm_password']
    #     val_name = self.cleaned_data['name']
    #     if val_conpas != val_pass:
    #         raise forms.ValidationError("password doesn't match")
    #     if len(val_name) > 20:
    #         raise forms.ValidationError("nam bul")
    def clean(self):
        clean = super().clean()
        val_nam = self.cleaned_data['name']
        val_pas = self.cleaned_data['password']
        val_conpas = self.cleaned_data['confirm_password']
        if len(val_nam) > 20:
            raise forms.ValidationError("erorr name")
        if val_conpas != val_pas:
            raise forms.ValidationError("erorr")
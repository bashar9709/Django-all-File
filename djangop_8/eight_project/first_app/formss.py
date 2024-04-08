from django import forms
from first_app.models import StudentModel

class studentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name':'Student Name',
            'roll':'Student Roll'
        }
        widgets = {
            'name': forms.TextInput(),
        }
        help_texts = {
            'name':"Write your full name",
        }
        erorr_messages = {
            'name': {'required':'your name is required'}
        }
        
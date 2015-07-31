from contacts_list.models import *
from django.forms import forms, ModelForm
class ContactFrom(forms.Form):
    class Meta:
        model = Contact
        fields = ('name','sex')
SS = forms.M
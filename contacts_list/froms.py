from contacts_list.models import *
from django.forms import forms
class ContactFrom(forms.Form):
    class Meta:
        model = Contact
        fields = ('name','sex')

from django.contrib import admin
from contacts_list.models import Contact


class ContactAdmin(admin.ModelAdmin):
    ss ='1'

admin.site.register(Contact, ContactAdmin)

from django.shortcuts import render, HttpResponse, get_object_or_404
from contacts_list.models import Contact

# Create your views here.

def index(request):
    return HttpResponse('hello, this page is index')

def login(request):
    return HttpResponse('hello, this page is login')

def logout(request):
    return HttpResponse('hello, this page is logout')

def list(request):
    contacts = Contact.objects.all()
    context= {'contacts':contacts}
    return render(request, 'contacts/list.html', context)

def detail(request,contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request,'contacts/detail.html', {'contact':contact})

def edit(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request,'contacts/edit.html', {'contact':contact})

def edit_save(request):
    return HttpResponse('hello, this page is edit_save')

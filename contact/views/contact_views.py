from django.shortcuts import render
from contact import models

# Create your views here.
def index(request):
    #filter = where#
    contacts=models.Contact.objects.filter(show=True)
    context={
        'contacts':contacts 
    }
    #Procura na pasta templates
    return render(request,'contact/index.html',context)

def contact(request,contact_id):
    #filter = where#
    single_contact=models.Contact.objects.get(pk=contact_id,show=True)
    context={
        'contact':single_contact
    }
    #Procura na pasta templates
    return render(request,'contact/contact.html',context)
     

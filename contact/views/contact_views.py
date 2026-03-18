from django.shortcuts import render,redirect,get_object_or_404
from contact import models
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    #filter = where#
    contacts=models.Contact.objects.filter(show=True)
    paginator=Paginator(contacts,25)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    context={
        'page_obj':page_obj
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
     
def search(request):
    search_value=request.GET.get('q','').strip()
    if search_value == "":
        return redirect("contact:index")
    print(search_value)
    #filter = where#
    contacts=models.Contact.objects.filter(show=True). \
    filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value))
    paginator=Paginator(contacts,25)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    context={
        'page_obj':page_obj
    }

    
    #Procura na pasta templates
    return render(request,'contact/index.html',context)
    
def delete(request,contact_id):
    contact=get_object_or_404(models.Contact,pk=contact_id,show=True)
    # "no" é o valor default #
    confirmation=request.POST.get("confirmation","no")

    if confirmation == "yes":
        contact.delete()
        return redirect("contact:index.html")
    return render(request,'contact/contact.html',{
        'contact':contact,  
        'confirmation':confirmation
    })
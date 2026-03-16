from django.shortcuts import render,redirect
from contact import models
from django import forms
class ContactForm(forms.ModelForm):
    #Definir como são as caract. do forms
    class Meta:
        model=models.Contact
        fields=(
            'first_name','last_name','phone',
        )
    ...
def create(request):
    if request.method == "POST":
        context={
        "form":ContactForm(request.POST)

        }
        return render(request,"contact/create.html",context)

    context={
        "form":ContactForm()

    }
    return render(request,"contact/create.html",context)

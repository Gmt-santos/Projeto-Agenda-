from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError
from contact import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
class ContactForm(forms.ModelForm):


    #Definir como são as caract. do forms
    picture=forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':"image/*"
            }
        )
    )
    class Meta:

        model=models.Contact
        fields=(
            'first_name','last_name','phone','email','description',
            'category','picture'
            
        )
        widgets={
            # 'Nome do campo' : tipo #
            'first_name':forms.TextInput(
                attrs={
                    'placeholder':"Nome",
                }
            )
        }
    # def clean(self):
    #     self.cleaned_data=self.cleaned_data
    #     self.add_error("first_name",ValidationError(
    #         "Erro",code="invalid"
    #     )
    #     )
    #     return super().clean()
    #clean_nomedocampo
    def clean_first_name(self):
        first_name=self.cleaned_data.get('first_name')
        if first_name == "ABC":
            #self.add_error("campo",erro)
            self.add_error('first_name',ValidationError('Mensagem de erro',code="Invalid"))
        return first_name
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields=(
            'first_name',"last_name","email",
            'username','password1',"password2"
        )
    def clean_email(self):
        # pega o dado do campo email #
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',ValidationError("E-mail já cadastrado",code="invalid")
            )
        return email
    ...
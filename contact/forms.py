from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError
from contact import models
from django import forms
class ContactForm(forms.ModelForm):
    #Definir como são as caract. do forms
    class Meta:
        model=models.Contact
        fields=(
            'first_name','last_name','phone','email','description',
            'category',
            
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
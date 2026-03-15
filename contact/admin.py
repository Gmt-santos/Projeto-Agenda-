from django.contrib import admin
from contact import models
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display='first_name','last_name'
    ...
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


# Register your models here.

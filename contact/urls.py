from django.urls import path
from contact import views
app_name="contact"
urlpatterns = [
    #caso a url seja vazia,chame o views.index com nome index#
    path('',views.index,name='index'),
    #caso a url seja apenas um int,chame o views.contact com nome contact#
    path('contact/<int:contact_id>/detail/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    path('contact/create/',views.create,name='create'),
]

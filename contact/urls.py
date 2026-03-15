from django.urls import path
from contact import views
app_name="contact"
urlpatterns = [
    #caso a url seja vazia,chame o views.index com nome index#
    path('',views.index,name='index'),
    #caso a url seja apenas um int,chame o views.contact com nome contact#
    path('<int:contact_id>/',views.contact,name='contact')
]
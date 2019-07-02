from django.conf.urls import url
from app import views

app_name = 'app'
urlpatterns=[
    url(r'^portraits/$',views.portraits,name='Portraits'),
    url(r'^contact/$',views.contact,name='Contacts')

]
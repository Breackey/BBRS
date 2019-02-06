from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bookbus/', views.bookbus, name='bookbus'),
    path('ticketdetails/', views.ticketdetails, name='ticketdetails'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
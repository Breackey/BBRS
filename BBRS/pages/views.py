from django.shortcuts import render

def index(request):
    return render(request, "index.html",{})

def bookbus(request):
    return render(request, "bookbus.html",{})

def ticketdetails(request):
    return render(request, "ticketdetails.html",{})

def about(request):
    return render(request, "about.html",{})

def contact(request):
    return render(request, "contact.html",{})

def login(request):
    return render(request, "login.html",{})


from django.shortcuts import render

def home(request):
    return render(request, "home.html",{})

def bookbus(request):
    return render(request, "bookbus.html",{})

def ticketdetails(request):
    return render(request, "ticketdetails.html",{})

def about(request):
    return render(request, "about.html",{})

def contact(request):
    return render(request, "contact.html",{})


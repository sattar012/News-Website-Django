
from news.models import Contact
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *


def index(request):
    return render(request, 'pluto/index.html')


def Contactdet(request):
    data = Contact.objects.all()
    return render(request, 'pluto/Contact1.html', {'data': data})


def deleteissue(request, pk):
    categ = Contact.objects.get(id=pk)
    categ.delete()
    return redirect('Contactdet')

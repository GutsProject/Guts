from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Student

    
def index(request): 
    return HttpResponse("Seja bem-vindo.")

def details(request, id):
    list_student = Student.objects.all()
    context = {
        "students" : list_student
    }
    return render(request, "reperguts/details.html", context)
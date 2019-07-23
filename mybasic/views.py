from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def index(request):
    return HttpResponse("Hello, this is my first app in django")

def create(request):
    person = Person()
    person.first_name = "testing"
    person.last_name = "account"
    person.save()
    return HttpResponse("This is create view")

def read(request):
    persons = Person.objects.all()
    for person in persons:
        text = person.first_name +" "+person.last_name
        return HttpResponse(text)

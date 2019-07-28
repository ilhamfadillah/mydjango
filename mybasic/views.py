from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.utils.crypto import get_random_string

def index(request):
    persons = Person.objects.all()
    output = Person.objects.all().values_list()
    return HttpResponse(output)

def create(request):
    person = Person()
    person.first_name = get_random_string(5)
    person.last_name = "account"
    person.save()
    result = str(person.id) + " | " + person.first_name + " | " + person.last_name
    return HttpResponse(result)

def read(request, id):
    try:
        person = Person.objects.get(id=id)
        result = person.first_name+" "+person.last_name
    except Person.DoesNotExist:
        result = "data does not exist"
    return HttpResponse(result)

def update(request, id):
    person = Person.objects.get(id=id)
    person.first_name = get_random_string(5)
    person.save()
    return HttpResponse(person.first_name + " " + person.last_name)

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponse("data already deleted")

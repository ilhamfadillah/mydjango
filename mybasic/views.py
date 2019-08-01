from .models import Person
from django.shortcuts import render, redirect
from django.template import loader
from .models import Person
from django.views.generic import TemplateView
from .forms import PersonForm


def index(request):
    persons = Person.objects.all()
    return render(request, 'mybasic/index.html', {
        'persons': persons,
    })


def create(request):
    form = PersonForm()
    return render(request, 'mybasic/create.html', {'form': form})


def store(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = Person()
            person.first_name = request.POST['first_name']
            person.last_name = request.POST['last_name']
            person.save()
    return redirect(index)

def edit(request, id):
    person = Person.objects.get(id=id)
    form = PersonForm(initial={
        'first_name': person.first_name,
        'last_name': person.last_name
    })
    return render(request, 'mybasic/edit.html', {
        'form': form,
        'person': person
    })

def update(request, id):
    person = Person.objects.get(id=id)
    person.first_name = request.POST['first_name']
    person.last_name = request.POST['last_name']
    person.save()
    return redirect(index)

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect(index)
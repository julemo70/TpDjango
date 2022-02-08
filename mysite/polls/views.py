from django.shortcuts import render
from polls.formulaire import *
from polls.models import *
from django.forms import *
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

# Create your views here.
def update_person(request, *args, **kwargs):
    template_name = 'update-person.html'
    obj = get_object_or_404(
        Person,
        pk=kwargs.get('pk')
    )
    if request.method =='GET':
        form = PersonForm(
            initial={
                'name':obj.name,
                'age':obj.age,
            }
        )
        context={
            'form': form
        }
        return render(
            request= request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form= PersonForm(
            request.POST,
            request.FILES,
            initial={
                'name':obj.name,
                'age':obj.age
            }
        )
        context = {
            'form':form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.sex = form.cleaned_data.get('sex')
            obj.age = form.cleaned_data.get('age')
            obj.country = form.cleaned_data.get('country')
            obj.save()
            redirect('home')
        return render(
            request=request,
            template_name=template_name,
            context=context
        )

def createProduit(request, *args, **kwargs):
    template_name = 'create-produit.html'
    obj = Produit()
    if request.method =='GET':
        form = ProduitForm(
            initial={
                'name':obj.name,
                'price':obj.price,
            }
        )
        context={
            'form': form
        }
        return render(
            request= request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form= ProduitForm(
            request.POST,
            request.FILES,
            initial={
                'name':obj.name,
                'price':obj.price
            }
        )
        context = {
            'form':form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.price = form.cleaned_data.get('price')
            obj.country = form.cleaned_data.get('country')
            obj.save()
            redirect('home')
        return render(
            request=request,
            template_name=template_name,
            context=context
        )

def createMagasin(request, *args, **kwargs):
    template_name = 'create-magasin.html'
    obj = Magasin()
    if request.method =='GET':
        form = MagasinForm(
            initial={
                'name':obj.name
            }
        )
        context={
            'form': form
        }
        return render(
            request= request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form= MagasinForm(
            request.POST,
            request.FILES,
            initial={
                'name':obj.name
            }
        )
        context = {
            'form':form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.save()
            redirect('home')
        return render(
            request=request,
            template_name=template_name,
            context=context
        )

def createProfileMagasin(request, *args, **kwargs):
    template_name = 'create-profileMag.html'
    obj = ProfileMagasin()
    if request.method =='GET':
        form = ProfileMagasinForm(
            initial={
                'name':obj.name
            }
        )
        context={
            'form': form
        }
        return render(
            request= request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form= ProfileMagasinForm(
            request.POST,
            request.FILES,
            initial={
                'name':obj.name
            }
        )
        context = {
            'form':form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.email = form.cleaned_data.get('email')
            obj.phone = form.cleaned_data.get('phone')
            obj.save()
            redirect('home')
        return render(
            request=request,
            template_name=template_name,
            context=context
        )

def isMajor(age:int) -> str:
    return 'Majeur' if age>18 else 'Mineur'

def index(request, *args, **kwargs):
    template_name = 'index.html'
    age = 18
    name = 'Ali'
    sex = 'masculin' 
    country = 'senegal'
    major = isMajor(age)
    persons = Person.objects.all()
    persons_gt_twenty = Person.objects.filter(age__gt=20)
    persons_with_a= Person.objects.filter(name__contains="a").filter(age__gt=20)
    #put data in a template
    context = {'age':age,
                'name':name,
                'sex':sex,
                'country':country,
                'isMajor':major,
                'persons':persons,
                'personsA':persons_with_a,
                'personsM':persons_gt_twenty}
    #return the http request instance
    return render(request=request,template_name=template_name,context=context)

def update_produit(request, *args, **kwargs):
    template_name = 'update.html'
    obj = get_object_or_404(
        Produit,
        pk=kwargs.get('pk')
    )
    if request.method =='GET':
        form = ProduitForm(
            initial={
                'name':obj.name,
                'age':obj.price,
            }
        )
        context={
            'form': form
        }
        return render(
            request= request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form= ProduitForm(
            request.POST,
            request.FILES,
            initial={
                'name':obj.name,
                'age':obj.price
            }
        )
        context = {
            'form':form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.price = form.cleaned_data.get('price')
            obj.country = form.cleaned_data.get('country')
            obj.save()
            redirect('home')
        return render(
            request=request,
            template_name=template_name,
            context=context
        )

def update_magasin(request, *args, **kwargs):
    template_name = 'update.html'
    obj = get_object_or_404(
        Magasin,
        pk=kwargs.get('pk')
    )
    if request.method =='GET':
        form = MagasinForm(
            initial={
                'name':obj.name,
                'age':obj.country,
            }
        )
        context={
            'form': form
        }
        return render(
            request= request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form= MagasinForm(
            request.POST,
            request.FILES,
            initial={
                'name':obj.name,
                'age':obj.country
            }
        )
        context = {
            'form':form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.save()
            redirect('home')
        return render(
            request=request,
            template_name=template_name,
            context=context
        )

def update_magasinProfile(request, *args, **kwargs):
    template_name = 'update.html'
    obj = get_object_or_404(
        ProfileMagasin,
        pk=kwargs.get('pk')
    )
    if request.method =='GET':
        form = ProfileMagasinForm(
            initial={
                'name':obj.name,
                'age':obj.country,
            }
        )
        context={
            'form': form
        }
        return render(
            request= request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form= ProfileMagasinForm(
            request.POST,
            request.FILES,
            initial={
                'name':obj.name,
                'age':obj.country
            }
        )
        context = {
            'form':form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.save()
            redirect('home')
        return render(
            request=request,
            template_name=template_name,
            context=context
        )